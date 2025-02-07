# Function to extract a grade from a string line
# General format of a line with a grade:
# Product Development 7 cr 5 8.5.2024 Teacher Name

import re
from Scripts.grade import Grade


def extract_grade(line: str) -> Grade | None:

    match = re.search(r'(\d+)\s+cr\s+(\d+)', line)
    if match:
        credits, grade = match.groups()
        return Grade(int(grade),int(credits))

    return None