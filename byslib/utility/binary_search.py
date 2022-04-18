# @title Binary search
from typing import Callable


def meguru_bisect(ok: int, ng: int, is_ok: Callable[..., bool], *args) -> int:
    """Binary Search

    Parameters
    ----------
    ok
        Inital value s.t. is_ok(ok) == True
    ng
        Inital value s.t. is_ok(ng) == False
    is_ok
        Judge function

    Returns
    -------
        number of is_ok(x) == True and is_ok(x ± 1) == False

    Notes
    -----
    Time complexity

    O(log(abs(ok-ng)))

    References
    ----------
    ..[1] https://twitter.com/meguru_comp/status/697008509376835584

    Examples
    --------
    """
    assert is_ok(ok, *args)
    assert not is_ok(ng, *args)

    while abs(ok - ng) > 1:
        mid = (ok + ng) >> 1
        if is_ok(mid, *args):
            ok = mid
        else:
            ng = mid
    return ok
