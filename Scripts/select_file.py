# UI Function to select a file from a directory
import os

def select_file(directory_str) -> str:
    files = os.listdir(directory_str)
    filenumber = 1
    for file in files:
        print(f"{filenumber}. file")
        filenumber += 1

    while True:
        user_input = input("Select a file number: ")
        try:
            int(user_input)
        except ValueError:
            continue

    return files[int(user_input) + 1]