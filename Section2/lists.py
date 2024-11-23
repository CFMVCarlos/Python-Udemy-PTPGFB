people: list[str] = ["Bob", "James", "Tom"]
print(f"Original: {people}")

# Append
people.append("Jeremy")
print(f"Append: {people}")

# Remove
people.remove("Bob")
print(f"Remove: {people}")

# Pop
people.pop()
print(f"Pop: {people}")

# Change
people[0] = "Charlotte"
print(f"Change: {people}")

# Insert
people.insert(1, "Timothy")
print(f"Insert: {people}")

# Clear
people.clear()
print(f"Clear: {people}")
