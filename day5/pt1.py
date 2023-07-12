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
            for i in range(quantity):
                stacks[toSpot].append(stacks[fromSpot].pop())
    result = ""
    for stack in stacks:
        result += stack.pop()
    print(result)