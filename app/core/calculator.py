from __future__ import annotations
from typing import Union


OPERATIONS = {
    'divmod': lambda x, y: divmod(x, y)[0],
    '**': int.__pow__,
    '//': int.__floordiv__,
    '/': int.__truediv__,
    '%': int.__mod__,
    '+': int.__add__,
    '*': int.__mul__,
    '-': int.__sub__,
}


def calculate(a: int, b: int, op: str = '+') -> Union[int, float]:
    if op in ('/', '//', '%', 'divmod') and not b:
        raise ValueError("DIVISION BY ZERO")
    return OPERATIONS.get(op, OPERATIONS['+'])(a, b)
