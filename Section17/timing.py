from timeit import repeat, timeit

a: str = "list(range(1000))"
b: str = "list(range(1000))"
c: str = "set(range(1000))"

# Allows the CPU to warm up to get more consistent results
warmup: float = timeit(stmt=a, number=100_000)

a_time: float = timeit(stmt=a, number=100_000)
b_time: float = timeit(stmt=b, number=100_000)

print(f"a: {a_time:.3f}s")
print(f"b: {b_time:.3f}s")

print()

# No warmup needed for repeat
a_time_list: list[float] = repeat(stmt=a, repeat=5, number=100_000)
b_time_list: list[float] = repeat(stmt=b, repeat=5, number=100_000)
c_time_list: list[float] = repeat(stmt=c, repeat=5, number=100_000)

print(f"a: {min(a_time_list):.3f}s")
print(f"b: {min(b_time_list):.3f}s")
print(f"c: {min(c_time_list):.3f}s")

print()

power_time: float = timeit("a**b", setup="a, b = 10, 3")
print(f"a**b: {power_time:.3f}s")

math_power_time: float = timeit("math.pow(a, b)", setup="import math; a, b = 10, 3")
print(f"math.pow(a, b): {math_power_time:.3f}s")

math_power_time2: float = timeit(
    "pow(a, b)", setup="from math import pow; a, b = 10, 3"
)
print(f"pow(a, b): {math_power_time2:.3f}s")
