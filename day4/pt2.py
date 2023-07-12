count = 0
with open("day4/input.txt", "r") as file:
    for line in file.readlines():
        line_split = line.split(",")
        first = [int(x) for x in line_split[0].split("-")]
        second = [int(x) for x in line_split[1].split("-")]
        all = first + second
        all.sort()
        if all[0] in first and all[1] in second or all[0] in second and all[1] in first:
            count += 1
    print(count)