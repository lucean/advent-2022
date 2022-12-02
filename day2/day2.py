
response_score = {"X": 1, "Y": 2, "Z": 3}
states = ["X", "Y", "Z"]


def calculate_score(challenge, response):

    outcome_score = 0

    if challenge == response:
        outcome_score = 3
    elif (states.index(response) - states.index(challenge)) % 3 == 1:
        outcome_score = 6

    return response_score[response] + outcome_score


def force_result(challenge, result):

    response = challenge

    if result == "X":
        response = states[(states.index(challenge) + 2) % len(states)]
    elif result == "Z":
        response = states[(states.index(challenge) + 1) % len(states)]

    return calculate_score(challenge, response)


with open("input.txt") as f:

    part_one = 0
    part_two = 0
    transform = {"A": "X", "B": "Y", "C": "Z"}

    for line in f:
        part_one += calculate_score(transform[line[0]], line[2])
        part_two += force_result(transform[line[0]], line[2])
    print(part_one)
    print(part_two)
