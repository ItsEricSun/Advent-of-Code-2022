maxes = [0,0,0]
count = 0
with open("day1/input.txt", "r") as file:
    for line in file.readlines():
        line = line.rstrip()
        if line == "":
            for i in range(3):
                if count > maxes[i]:
                    maxes[i] = count
                    maxes.sort()
                    break
            count = 0
        else: count += int(line)
print(sum(maxes))