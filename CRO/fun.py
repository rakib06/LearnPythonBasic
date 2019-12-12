import random
sequence = []
dept = 6
time = 5


def repair(molecule):
    unique = []
    for n in molecule:
        if n not in unique:
            unique.append(n)
    if len(unique) != len(molecule):
        for x in range(1, len(molecule) + 1):
            if x not in unique:
                if x <= len(molecule):
                    unique.append(x)

    return unique


def sequence_gen(dept):
    short_sequence = []
    for j in range(dept):
        short_sequence.append(random.randint(1, dept))
    repair(short_sequence)
    return short_sequence


for i in range(time):
    item = sequence_gen(dept)
    sequence.append(item)


print(sequence)