
def inclusive_range(start, stop):
    return range(start, stop + 1, 1)


def make_inclusive_range(input):
    start = int(input.split('-')[0])
    stop = int(input.split('-')[1])

    return inclusive_range(start, stop)


def day4(overlap_predicate):
    with open("input.txt") as f:
        sum = 0

        for line in f:
            first = line.split(',')[0]
            second = line.split(',')[1]

            first_set = set(make_inclusive_range(first))
            second_set = set(make_inclusive_range(second))

            if overlap_predicate(first_set, second_set):
                sum += 1

        print(sum)


def part_one_overlap_predicate(first_set, second_set):
    return first_set.issubset(second_set) or second_set.issubset(first_set)


def part_two_overlap_predicate(first_set, second_set):
    return len(first_set.intersection(second_set)) != 0


day4(part_one_overlap_predicate)
day4(part_two_overlap_predicate)