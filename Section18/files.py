from typing import TextIO

file_path: str = "Section18/info.txt"

try:
    file: TextIO = open(file_path, mode="r")
    text: str = file.read()
    print(text)
    raise Exception("unkown error")
except FileNotFoundError:
    print(f"File {file_path} not found")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Closing the file")
    file.close()

print()

try:
    with open(file_path, mode="r") as file:
        text: str = file.read()
        print(text)
except FileNotFoundError:
    print(f"File {file_path} not found")
