# Function to read the given file which returns a list of the grades
import extract_grade
from Scripts.grade import Grade


def read_file(file_path:str) -> list:
    result:list = []

    text_file = open(file_path, 'r')
    for line in text_file:
        new_grade = extract_grade(line)
        if type(new_grade) == Grade:
            result.append(new_grade)

    return result