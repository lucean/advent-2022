import re
from collections import defaultdict


class Instruction():

    def __init__(self, source, target, quantity):
        self.source = int(source)
        self.target = int(target)
        self.quantity = int(quantity)

    def __repr__(self):
        return "move {} from {} to {}".format(self.quantity, self.source, self.target)


def parse_stack_line(dict, line: str):
    stacks = len(line) // 4

    for i in range(0, stacks):
        ch = line[(i * 4) + 1]
        if not ch.isspace() and ch.isalpha():
            dict[i + 1].insert(0, ch)

    return dict


def parse_instruction(line: str):
    matches = re.search("move\s(\d*)\sfrom\s(\d*)\sto\s(\d*)", line)
    return Instruction(matches.group(2), matches.group(3), matches.group(1))


def process_instruction(dict, instruction):
    source = instruction.source
    target = instruction.target
    quantity = instruction.quantity

    for i in range(0, quantity):
        dict[target].append(dict[source].pop())

    return dict

def process_instruction_9001(dict, instruction):
    source = instruction.source
    target = instruction.target
    quantity = instruction.quantity

    dict[target].extend(dict[source][-quantity:])

    for i in range(0, quantity):
        dict[source].pop()

    return dict


def day5(crate_mover_func):
    instructions = []
    dict = defaultdict(list)

    with open("input.txt") as f:
        for line in f:
            if "[" in line:
                dict = parse_stack_line(dict, line)
            elif line.startswith("move"):
                instructions.append(parse_instruction(line))

    for ins in instructions:
        dict = crate_mover_func(dict, ins)

    sorted_list = [(item[0], item[1].pop()) for item in dict.items() if len(item[1]) != 0]
    sorted_list.sort(key=lambda elem: elem[0])

    print("".join([item[1] for item in sorted_list]))

def part_one():
    day5(process_instruction)

def part_two():
    day5(process_instruction_9001)

part_one()
part_two()