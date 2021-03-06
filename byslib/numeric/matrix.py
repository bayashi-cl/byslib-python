# @title Matrix
from collections import UserList
from typing import Generic, Iterable, Optional, TypeVar, Union

_T = TypeVar("_T", int, float)


class Vector(UserList, Generic[_T]):
    def __init__(self, initlist: Optional[Iterable[_T]]) -> None:
        super().__init__(initlist=initlist)

    def __add__(self, other: Union[Iterable[_T], _T]) -> "Vector[_T]":
        if isinstance(other, float) or isinstance(other, int):
            return Vector(map(lambda x: x + other, self))
        elif isinstance(other, Vector):
            if len(other) != len(self):
                raise ValueError

            for i in range(len(self)):
                self[i] += other[i]
            return self
        else:
            raise ValueError


class Matrix:
    ...
