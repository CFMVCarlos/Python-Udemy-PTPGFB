from math import isclose

a: float = 0.999
b: float = 1.000

# Absolute tolerance
print(f"ABS | {a} == {b}? {isclose(a,b,abs_tol=0.002)}")

# Relative tolerance
print(f"REL | {a} == {b}? {isclose(a,b,rel_tol=0.01)}")  # 1 percent

a = 999
b = 1000
print(f"REL | {a} == {b}? {isclose(a,b,rel_tol=0.01)}")  # 1 percent
