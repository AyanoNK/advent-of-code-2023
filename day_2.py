from data_import import get_question_data


question_data = get_question_data(2023, 2)

# # separate enter from a string into a list
question_data = question_data.splitlines()


max_cubes = {"red": 12, "green": 13, "blue": 14}


def collect_max_info(game_line):
    division = game_line.split(":")
    game_records = division[1].split(";")
    results = {}
    for record in game_records:
        record = record.split(",")
        record = [x.split(" ") for x in record]
        record = [[x[1], x[2]] for x in record]

        for color_count in record:
            if (
                color_count[1] not in results
                or int(color_count[0]) > results[color_count[1]]
            ):
                results[color_count[1]] = int(color_count[0])
    return {
        "game_number": division[0].split(" ")[1],
        "color_max": results,
    }


SUMMER = 0

for line in question_data:
    game_max_info = collect_max_info(line)
    CAN_CONTINUE = True
    for game_max_record in game_max_info["color_max"].items():
        if (game_max_record[1]) > max_cubes[game_max_record[0]]:
            CAN_CONTINUE = False
            break
    if CAN_CONTINUE:
        SUMMER += int(game_max_info["game_number"])

print(SUMMER)

SUMMER = 0

for line in question_data:
    MULTIP = 1
    game_max_info = collect_max_info(line)
    for game_max_record in game_max_info["color_max"].items():
        MULTIP *= game_max_record[1]
    SUMMER += MULTIP

print(SUMMER)
