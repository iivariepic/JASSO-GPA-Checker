# Main function to run the UI
from Scripts.calculate_average import calculate_average
from Scripts.filereader import read_file
from Scripts.select_file import select_file
import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    selected_file = select_file(f"{script_dir}/Place txt here")
    selected_file_path = script_dir + "/Place txt here/" + selected_file

    grades = read_file(selected_file_path)
    average = calculate_average(grades)

    total_credits:int = 0
    for grade in grades:
        print(grade.TUAS_grade)
        total_credits += grade.credit_amount

    print(f"Total amount of calculated credits: {total_credits}")
    print(f"JASSO GPA: {average}")


if __name__ == '__main__':
    main()