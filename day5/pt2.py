stacks = [[] for _ in range(9)]
with open("day5/input.txt", "r") as file:
    for line in file.readlines():
        if line[0] == "[":
            for i in range(1, 34, 4):
                letter = line[i]
                if letter != " ":
                    stacks[i//4].insert(0, letter)
        elif line[0] == "m":
            instructions = line.split(" ")
            quantity = int(instructions[1])
            fromSpot = int(instructions[3]) - 1
            toSpot = int(instructions[5]) - 1
            pickedUp = []
            for i in range(quantity):
                pickedUp.append(stacks[fromSpot].pop())
            for i in range(quantity):
                stacks[toSpot].append(pickedUp.pop())
    result = ""
    for stack in stacks:
        result += stack.pop()
    print(result)