count = 0
with open("day4/input.txt", "r") as file:
    for line in file.readlines():
        line_split = line.split(",")
        first = [int(x) for x in line_split[0].split("-")]
        second = [int(x) for x in line_split[1].split("-")]
        if first[0] >= second[0] and first[1] <= second[1] or second[0] >= first[0] and second[1] <= first[1]:
            count += 1
    print(count)