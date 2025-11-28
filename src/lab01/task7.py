input_string = input()


def find_first_upper(s):
    for idx, char in enumerate(s):
        if char.isupper():
            return idx
    return -1


def find_after_digit(s):
    for idx, char in enumerate(s):
        if char.isdigit():
            return idx + 1 if idx + 1 < len(s) else -1
    return -1


def find_first_dot(s):
    for idx, char in enumerate(s):
        if char == ".":
            return idx
    return -1


start_index = find_first_upper(input_string)
step_index = find_after_digit(input_string)
end_index = find_first_dot(input_string)

if start_index == -1 or step_index == -1 or end_index == -1:
    result = ""
else:
    step_size = step_index - start_index
    if step_size == 0:
        step_size = 1
    result = "".join(
        input_string[i] for i in range(start_index, end_index + 1, step_size)
    )

print(result)
