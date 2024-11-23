file_path: str = "Section18/info.txt"

with open(file_path, "r") as file:
    text: str = file.read()
    print(text)

print()

with open(file_path, "r") as file:
    print(file.readline(5), end="")  # "This "
    print(file.readline(3), end="")  # "is "
    print(file.readline(), end="")  # "some info"
    print(file.readline(), end="")
