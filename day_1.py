import re
from data_import import get_question_data


question_data = get_question_data(2023, 1)

# separate enter from a string into a list
question_data = question_data.splitlines()


SUMMER = 0

for i in question_data:
    found = re.findall(r"\d+", i)
    two_added = f"{found[0][0]}{found[-1][-1]}"
    SUMMER += int(two_added)

print(SUMMER)

# PT 2

# question_data = [
#     "two1nine",
#     "eightwothree",
#     "abcone2threexyz",
#     "xtwone3four",
#     "4nineeightseven2",
#     "zoneight234",
#     "7pqrstsixteen",
# ]

letter_to_number = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

SUMMER = 0

trans_string = []
for i in question_data:
    for word, number in letter_to_number.items():
        i = i.replace(str(number), word)

    for word in letter_to_number:
        INDEX = i.find(word)
        while INDEX != -1:
            trans_string.append((word, INDEX))
            INDEX = i.find(word, INDEX + 1)

    trans_string.sort(key=lambda x: x[1])
    first_value = letter_to_number[trans_string[0][0]]
    last_value = letter_to_number[trans_string[-1][0]]
    toadd = first_value + last_value
    SUMMER += int(toadd)

    trans_string = []

print(SUMMER)
