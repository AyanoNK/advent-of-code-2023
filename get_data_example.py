from data_import import get_question_data


question_data = get_question_data(2022, 1)

# separate enter from a string into a list
question_data = question_data.splitlines()
