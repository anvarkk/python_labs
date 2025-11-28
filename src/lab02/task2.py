# task2.py

from typing import List, Union

Number = Union[int, float]


def _check_rect(mat: List[List[Number]]):
    if not mat:
        return
    n = len(mat[0])
    for row in mat:
        if len(row) != n:
            raise ValueError("рваная матрица")


def transpose(mat: List[List[Number]]) -> List[List[Number]]:
    if not mat:
        return []
    _check_rect(mat)
    # zip(*mat) даёт колонки; превращаем в списки
    return [list(col) for col in zip(*mat)]


def row_sums(mat: List[List[Number]]) -> List[Number]:
    _check_rect(mat)
    return [sum(row) for row in mat]


def col_sums(mat: List[List[Number]]) -> List[Number]:
    _check_rect(mat)
    if not mat:
        return []
    return [sum(col) for col in zip(*mat)]


if __name__ == "__main__":
    cases = [
        ("transpose", [[1, 2, 3]]),
        ("transpose", [[1], [2], [3]]),
        ("transpose", [[1, 2], [3, 4]]),
        ("transpose", []),
        ("transpose", [[1, 2], [3]]),
        ("row_sums", [[1, 2, 3], [4, 5, 6]]),
        ("row_sums", [[-1, 1], [10, -10]]),
        ("row_sums", [[0, 0], [0, 0]]),
        ("row_sums", [[1, 2], [3]]),
        ("col_sums", [[1, 2, 3], [4, 5, 6]]),
        ("col_sums", [[-1, 1], [10, -10]]),
        ("col_sums", [[0, 0], [0, 0]]),
        ("col_sums", [[1, 2], [3]]),
    ]

    funcs = {"transpose": transpose, "row_sums": row_sums, "col_sums": col_sums}

    for fname in ("transpose", "row_sums", "col_sums"):
        print(fname)
        for name, inp in cases:
            if name != fname:
                continue
            try:
                res = funcs[name](inp)
                print(f"{inp!r} -> {res!r}")
            except Exception as e:
                print(f"{inp!r} -> {type(e).__name__}: {e}")
        print()
