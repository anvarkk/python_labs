# Лабораторная Работа 1

## Задание 1 - Приветствие и возраст
![Задание 1](images/lab01_task1.png)

## Задание 2 - Сумма и среднее
![Задание 2](images/lab01_task2.png)

## Задание 3 - Чек: скидка и НДС
![Задание 3](images/lab01_task3.png)

## Задание 4 - Минуты → ЧЧ:ММ
![Задание 4](images/lab01_task4.png)

## Задание 5 - Инициалы и длина строки
![Задание 5](images/lab01_task5.png)

## Задание 6* - Подсчет участников
![Задание 6](images/lab01_task6.png)

## Задание 7* - Расшифровка строки
![Задание 7](images/lab01_task7.png)

## Лабораторная работа 2 

### Задание 1 - Реализовать функции

### Код
```python
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
```

![Задание 1](images/lab02_task1.png)

### Задание 2

### Код
```python
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
```

![Задание 2](images/lab02_task2.png)

### Задание 3

### Код
```python
# tuples.py

from typing import Tuple

def format_record(rec: Tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise TypeError("record must be tuple (fio, group, gpa)")
    fio, group, gpa = rec
    if not isinstance(fio, str) or not fio.strip():
        raise ValueError("пустое ФИО")
    if not isinstance(group, str) or not group.strip():
        raise ValueError("пустая группа")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")

    parts = fio.split()  # split() уже убирает лишние пробелы
    if len(parts) < 2:
        raise ValueError("ФИО должно содержать как минимум фамилию и имя")

    surname = parts[0].lower().capitalize()
    names = parts[1:3]  # 1–2 имени для инициалов
    initials = "".join((n[0].upper() + ".") for n in names if n)

    return f"{surname} {initials}, гр. {group.strip()}, GPA {gpa:.2f}"


if __name__ == "__main__":
    cases = [
        ("Иванов Иван Иванович", "BIVT-25", 4.6),
        ("Петров Пётр", "IKBO-12", 5.0),
        ("Петров Пётр Петрович", "IKBO-12", 5.0),
        ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
        # несколько негативных для демонстрации
        ("", "G-1", 4.0),
        ("Иванов", "G-1", 4.0),
        ("Иванов Иван", "", 4.0),
        ("Иванов Иван", "G-1", "badgpa"),
    ]

    print("format_record")
    for rec in cases:
        try:
            out = format_record(rec)
            print(f"{rec!r} -> {out!r}")
        except Exception as e:
            print(f"{rec!r} -> {type(e).__name__}: {e}")
```


![Задание 3](images/lab02_task3.png)
