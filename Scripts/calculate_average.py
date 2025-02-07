# Function to calculate the average grade
from Scripts.grade import Grade


def calculate_average(grades:list[Grade]) -> float:
    credit_amount:int = 0
    grade_amount_weighted:int = 0

    for grade in grades:
        credit_amount += grade.credit_amount
        grade_amount_weighted += grade.JASSO_grade * grade.credit_amount

    return grade_amount_weighted/credit_amount