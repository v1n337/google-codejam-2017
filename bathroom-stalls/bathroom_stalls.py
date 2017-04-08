import sys


def get_min_max_dist(stall_count, person_count):
    stall_spaces = [stall_count]

    for person in range(person_count - 1):
        max_dist = max(stall_spaces)
        max_index = stall_spaces.index(max_dist)
        stall_spaces.pop(max_index)
        stall_spaces.append((max_dist // 2))
        stall_spaces.append(max_dist - (max_dist // 2) - 1)

    for i in range(len(stall_spaces)):
        space = stall_spaces.pop(i)
        stall_spaces.append(space // 2)
        stall_spaces.append(space - (space // 2) - 1)

    return min(stall_spaces), max(stall_spaces)


with open(sys.argv[1]) as input_file:
    test_case_count = int(input_file.readline())

    for i in range(test_case_count):
        test_input = input_file.readline().split()
        print(test_input)
        stall_count = int(test_input[0])
        person_count = int(test_input[1])

        (min_dist, max_dist) = get_min_max_dist(stall_count, person_count)
        print(max_dist, min_dist)
