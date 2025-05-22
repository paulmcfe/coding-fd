with open("limerick.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        # Strip whitespace and print the line
        print(line.strip())