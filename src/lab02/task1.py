# task1.py

from typing import List, Any, Union, Tuple

Number = Union[int, float]

def min_max(nums: List[Number]) -> Tuple[Number, Number]:
    if not nums:
        raise ValueError("Пустой список")
    return min(nums), max(nums)

def unique_sorted(nums: List[Number]) -> List[Number]:
    seen = {}
    for x in nums:
        k = float(x)
        if k not in seen:
            seen[k] = x
    return [seen[k] for k in sorted(seen.keys())]

def flatten(mat: List[Union[List[Any], tuple]]) -> List[Any]:
    out = []
    for row in mat:
        if isinstance(row, str):
            raise TypeError("строка не строка строк матрицы")
        if not isinstance(row, (list, tuple)):
            raise TypeError("элемент матрицы не является списком/кортежем")
        out.extend(row)
    return out

if __name__ == "__main__":
    cases = [
        ("min_max", [3, -1, 5, 5, 0]),
        ("min_max", [42]),
        ("min_max", [-5, -2, -9]),
        ("min_max", []),
        ("min_max", [1.5, 2, 2.0, -3.1]),

        ("unique_sorted", [3, 1, 2, 1, 3]),
        ("unique_sorted", []),
        ("unique_sorted", [-1, -1, 0, 2, 2]),
        ("unique_sorted", [1.0,1,2.5,2.5,0]),

        ("flatten", [[1,2],[3,4]]),
        ("flatten", [[1,2], (3,4,5)]),
        ("flatten", [[1], [], [2,3]]),
        ("flatten", [[1,2], "ab"]),
    ]

    funcs = {"min_max": min_max, "unique_sorted": unique_sorted, "flatten": flatten}

    for fname in ("min_max", "unique_sorted", "flatten"):
        print(fname)
        for name, inp in cases:
            if name != fname:
                continue
            try:
                res = funcs[name](inp)
                print(f"{inp!r} -> {res!r}")
            except Exception as e:
                print(f"{inp!r} -> {type(e).__name__}: {e}")
        print()  # пустая строка между функциями

