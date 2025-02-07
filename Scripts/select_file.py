# UI Function to select a file from a directory
import os

def select_file(directory_str) -> str:
    files = os.listdir(directory_str)
    filenumber = 1
    for file in files:
        print(f"{filenumber}. {file}")
        filenumber += 1

    while True:
        user_input = input("Select a file number: ")
        try:
            files[int(user_input) - 1]
        except:
            print("Invalid input")
            continue

        break

    return files[int(user_input) - 1]