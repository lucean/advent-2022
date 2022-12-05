import string
import itertools


def calculate_priorities(items):
    acc = 0
    for ch in items:
        if ch.isupper():
            acc += 26

        acc += string.ascii_lowercase.index(ch.lower()) + 1

    return acc


def part_one():
    sum = 0

    with open("input.txt") as f:
        for line in f:
            length = len(line)
            first = set(line[:int(length / 2)])
            second = set(line[int(length / 2):])

            match = first.intersection(second)

            sum += calculate_priorities(match)
    print(sum)

def part_two():
    sum = 0

    with open("input.txt") as f:
        for line1, line2, line3 in itertools.zip_longest(*[f] * 3):
            match = set(line1).intersection(set(line2)).intersection(set(line3))
            match.remove('\n')
            sum += calculate_priorities(match)
    print(sum)

part_one()
part_two()