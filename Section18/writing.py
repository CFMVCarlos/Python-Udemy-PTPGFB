file_path: str = "Section18/info2.txt"

with open(file_path, "w") as file:
    file.write("This is spam\n")
    file.writelines(["This is eggs\n", "This is ham\n"])
