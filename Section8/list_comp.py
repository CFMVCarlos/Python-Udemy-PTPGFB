from math import e

numbers: list[int] = [1, 2, 3]

doubled: list[int] = []
for number in numbers:
    doubled.append(number * 2)
print(doubled)

doubled_lc: list[int] = [number * 2 for number in numbers]
print(doubled)

##############################################

names: list[str] = ["Mario", "James", "Luigi", "John"]
j_names: list[str] = []
for name in names:
    if name.startswith("J"):
        j_names.append(name)
print(j_names)

j_names_lc: list[str] = [name for name in names if name.startswith("J")]
print(j_names_lc)

##############################################

numbers: list[int] = [1, 2, 4, 6, 7, 10]
even_numbers: list[int] = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

even_numbers_lc: list[int] = [number for number in numbers if number % 2 == 0]
print(even_numbers_lc)
