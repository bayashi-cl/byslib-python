import typing


class Grid:
    DeltaItr = typing.Iterable[typing.Tuple[int, int]]
    h: int
    w: int

    def __init__(self, h: int, w: int) -> None:
        self.h = h
        self.w = w

    def __contains__(self, ij: typing.Tuple[int, int]) -> bool:
        return 0 <= ij[0] < self.h and 0 <= ij[1] < self.w

    def area(self) -> int:
        return self.h * self.w

    def index(self, i: int, j: int) -> int:
        if (i, j) not in self:
            raise ValueError("index out of grid")
        return self.w * i + j

    def coord(self, ind: int) -> typing.Tuple[int, int]:
        if ind < 0 or self.area() <= ind:
            raise ValueError("index out of grid")
        return divmod(ind, self.w)

    def delta(self, i: int, j: int, d: DeltaItr) -> DeltaItr:
        if (i, j) not in self:
            raise ValueError("index out of grid")
        for di, dj in d:
            ni, nj = i + di, j + dj
            if (ni, nj) in self:
                yield (ni, nj)

    def delta2(self, i: int, j: int) -> DeltaItr:
        return self.delta(i, j, ((0, 1), (1, 0)))

    def delta4(self, i: int, j: int) -> DeltaItr:
        return self.delta(i, j, ((-1, 0), (0, 1), (1, 0), (0, -1)))

    def delta8(self, i: int, j: int) -> DeltaItr:
        d = []
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == 0 and dj == 0:
                    continue
                d.append((di, dj))
        return self.delta(i, j, d)
