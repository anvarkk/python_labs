def min_max(a):
    if not a:
        return 'ValueError'

    max_ = -10 ** 10
    min_ = 10 ** 10
    for i in a:
        if i > max_:
            max_ = i
        if i < min_:
            min_ = i

    return (min_, max_)


def unique_sorted(b):
    return sorted(set(b))


def flatten(c):
    if not c:
        return []

    result = []

    for i in c:
        if not isinstance(i, (list, tuple)):
            return 'TypeError'
        result.extend(i)

    return result
