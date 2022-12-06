
def find_consecutive_uniq_chars_pos(arr, length):
    for i in range(0, len(arr) - length):
        uniq_chars = set(arr[i:i + length])
        if len(uniq_chars) == length:
            return i + length


def day6(length):
    with open("input.txt") as f:
        for line in f:
            arr = list(line)
            print(find_consecutive_uniq_chars_pos(arr, length))


def part_one():
    day6(4)


def part_two():
    day6(14)


part_one()
part_two()
