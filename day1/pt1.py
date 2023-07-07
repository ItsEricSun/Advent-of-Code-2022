max = 0
count = 0
with open("day1/input.txt", "r") as file:
    for line in file.readlines():
        line = line.rstrip()
        if line == "":
            if count > max:
                max = count
            count = 0
        else: count += int(line)
print(max)