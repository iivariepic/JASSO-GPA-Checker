# Function to return a list of file names from a directory
import os

def get_files(directory:str) -> list[str]:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(os.path.dirname(script_dir), directory)
    return os.listdir(path)

if __name__ == "__main__":
    print(get_files("Place txt here"))