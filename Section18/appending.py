file_path: str = "Section18/info.txt"

with open(file_path, "a") as file:
    file.write("This is spam\n")
    file.writelines(["This is eggs\n", "This is ham\n"])
