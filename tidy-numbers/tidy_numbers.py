import sys

input_file_path = sys.argv[1]


def find_last_tidy(number):
    while (number >= 0):
        # print("working on " + str(number))
        number_list = [int(d) for d in str(number)]
        if sorted(number_list) == number_list:
            return number
        elif sorted(number_list) == list(reversed(number_list)):
            new_num_str = ""
            for i in range(len(number_list) - 1):
                new_num_str += "9"
            return int(new_num_str)
        number -= 1


with open(input_file_path) as input_file:
    test_case_count = int(input_file.readline())

    for test_case in range(test_case_count):
        number = int(input_file.readline())

        tidy_number = find_last_tidy(number)
        print("Case #" + str(test_case + 1) + ": " + str(tidy_number))
