names = ["Alice", "Bob", "Charlie", "David", "Eve", "Alphonse"]
matches = []
for name in names:
    if name.startswith("A"):
        matches.append(name)
print(matches)