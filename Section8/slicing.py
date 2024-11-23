numbers: list[int] = [1, 2, 3, 4, 5, 6]
# numbers: str = "123456"
# numbers: tuple[int, int, int, int, int, int] = (1, 2, 3, 4, 5, 6)

# print(numbers[0:3])
print("First numbers: ", numbers[:3])

# print(numbers[3:6])
print("Last numbers: ", numbers[3:])

print("All numbers: ", numbers[:3] + numbers[3:])

print("Last element: ", numbers[-1])

print("All until 4th with step of 2: ", numbers[:4:2])

print("All numbers with step of 2: ", numbers[::2])

print("All numbers in reverse: ", numbers[::-1])
