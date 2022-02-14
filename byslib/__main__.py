"""\
source expander

Original:
    https://github.com/not522/ac-library-python/blob/master/atcoder/__main__.py
    * __future__ 系に対応するために import a を置き換えるように変更
    * 指定されたモジュールのファイルも展開できるように

* __init__.py に何か書かれていないと壊れる
* ソースの中にの三重引用符のネストがあると壊れる
"""

import argparse
import ast
import importlib
import inspect
import re
import sys
from typing import Dict, List, Optional, cast

expand_module_patterns: List[re.Pattern] = []


class ImportInfo:
    def __init__(
        self,
        lineno: int,
        end_lineno: int,
        import_from: Optional[str] = None,
        name: Optional[str] = None,
        asname: Optional[str] = None,
    ) -> None:
        self.lineno = lineno
        self.end_lineno = end_lineno
        self.import_from = import_from
        self.name = name
        self.asname = asname


def iter_child_nodes(
    node: ast.AST, import_info: Optional[ImportInfo] = None
) -> List[ImportInfo]:
    result = []

    if isinstance(node, ast.alias):
        if import_info:
            result.append(
                ImportInfo(
                    import_info.lineno,
                    import_info.end_lineno,
                    import_info.import_from,
                    node.name,
                    node.asname,
                )
            )
        return result

    if isinstance(node, ast.Import):
        for name in node.names:
            if any(pat.match(name.name) for pat in expand_module_patterns):
                if hasattr(node, "end_lineno"):
                    end_lineno = cast(int, node.end_lineno)  # type: ignore
                else:
                    end_lineno = node.lineno
                import_info = ImportInfo(node.lineno, end_lineno)
    elif isinstance(node, ast.ImportFrom):
        if any(pat.match(cast(str, node.module)) for pat in expand_module_patterns):
            if hasattr(node, "end_lineno"):
                end_lineno = cast(int, node.end_lineno)  # type: ignore
            else:
                end_lineno = node.lineno
            import_info = ImportInfo(node.lineno, end_lineno, node.module)

    for child in ast.iter_child_nodes(node):
        result += iter_child_nodes(child, import_info)
    return result


class ModuleImporter:
    def __init__(self) -> None:
        self.imported_modules: List[str] = []

    def import_module(
        self, import_from: Optional[str], name: str, asname: Optional[str] = None
    ) -> str:
        result = ""

        if import_from is None:
            module_name = name
        else:
            try:
                module_name = import_from + "." + name
                importlib.import_module(module_name)
            except ImportError:
                module_name = import_from

        if module_name not in self.imported_modules:
            self.imported_modules.append(module_name)

            module = importlib.import_module(module_name)
            source = inspect.getsource(module)
            source = source.replace("'''", '"""')
            lines = source.split("\n")
            imports = iter_child_nodes(ast.parse(source))

            import_lines = []
            for import_info in imports:
                result += self.import_module(
                    import_info.import_from,
                    cast(str, import_info.name),
                    import_info.asname,
                )
                for line in range(import_info.lineno - 1, import_info.end_lineno):
                    import_lines.append(line)

            for lineno, line_str in enumerate(lines):
                if lineno not in import_lines:
                    continue
                lines[lineno] = "# " + line_str  # TODO(not): indent

            modules = module_name.split(".")
            for i in range(len(modules) - 1):
                result += self.import_module(None, ".".join(modules[: i + 1]))

            code = "_" + module_name.replace(".", "_") + "_code"
            result += f"{code} = '''\n"
            result += "\n".join(lines)
            result += "'''\n\n"
            result += f"{module_name} = types.ModuleType('{module_name}')\n"

            # TODO(not): asname
            imported = []
            for import_info in imports:
                if import_info.import_from is None:
                    modules = cast(str, import_info.name).split(".")
                    for i in range(len(modules)):
                        import_name = ".".join(modules[: i + 1])
                        if import_name in imported:
                            continue
                        imported.append(import_name)
                        result += (
                            f"{module_name}.__dict__['{import_name}']"
                            f" = {import_name}\n"
                        )
                else:
                    result += (
                        f"{module_name}.__dict__['{import_info.name}']"
                        f" = {import_info.import_from}.{import_info.name}\n"
                    )

            result += f"exec({code}, {module_name}.__dict__)\n"

        if import_from is None:
            if asname is None:
                if name != module_name:
                    result += f"{name} = {module_name}\n"
            else:
                result += f"{asname} = {module_name}\n"
        else:
            if asname is None:
                if name != import_from + "." + name:
                    result += f"{name} = {import_from}.{name}\n"
            else:
                result += f"{asname} = {import_from}.{name}\n"

        return result + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="Source code")
    parser.add_argument("-o", "--output", help="Single combined code")
    parser.add_argument(
        "-m", "--modules", nargs="*", default="atcoder", help="list of expand module"
    )
    args = parser.parse_args()

    global expand_module_patterns
    expand_module_patterns = [
        re.compile(f"^{m}\\.?") for m in cast(List[str], args.modules)
    ]

    with open(args.src) as f:
        lines = f.readlines()
    imports = iter_child_nodes(ast.parse("".join(lines)))

    importer = ModuleImporter()
    import_end_lineno_code: Dict[int, str] = {}
    import_lines = []
    result_stack = []

    for import_info in imports:
        import_end_lineno_code[import_info.end_lineno - 1] = importer.import_module(
            import_info.import_from, cast(str, import_info.name), import_info.asname
        )
        for line in range(import_info.lineno - 1, import_info.end_lineno):
            import_lines.append(line)

    import_types = False

    for lineno, line_str in enumerate(lines):
        if lineno in import_lines:
            result_stack.append("# " + line_str)
        else:
            result_stack.append(line_str)

        if lineno in import_end_lineno_code:
            if not import_types:
                result_stack.append("import types\n\n")
                import_types = True
            result_stack.append(import_end_lineno_code[lineno])

    result = "".join(result_stack)
    try:
        compile(result, "<string>", "exec")
    except Exception as e:
        print(
            "[\033[31mERROR\033[0m] Failed to generate executable source\n",
            file=sys.stderr,
        )
        raise e

    if args.output:
        with open(args.output, "w") as f:
            f.write(result)
    else:
        print(result, end="")


if __name__ == "__main__":
    main()