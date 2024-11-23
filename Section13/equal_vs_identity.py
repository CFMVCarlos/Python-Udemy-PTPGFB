a: int = 1000
b: int = int("1000")

print(a == b)
print(a is b)

var: int | None = None
if var is None:
    print("var is None")
else:
    print("var is not None")
