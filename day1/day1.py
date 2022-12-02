

i = 0
dict = {}
sum = 0

with open("input.txt") as f:
    for line in f:
        if len(line) != 0 and line != '\n':
            sum += int(line)
        else:
            dict[i] = sum
            sum = 0
            i += 1

    print(sorted(dict.values()))
