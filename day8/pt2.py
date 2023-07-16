with open("day8/input.txt", "r") as file:
    lines = file.readlines()
    rows = len(lines)
    cols = len(lines[0].strip())  
trees = [[0] * cols for _ in range(rows)] 
with open("day8/input.txt", "r") as file:
    row = 0
    for line in file.readlines():
        line = line.strip()
        for col in range(cols):
            trees[row][col] = int(line[col])
        row += 1

def countUp(orgHeight, maxHeight, row, col, count):
    if row < 0:
        return count
    height = trees[row][col]
    if height >= orgHeight:
        return count + 1
    if height >= maxHeight:
        maxHeight = height
    return countUp(orgHeight, maxHeight, row - 1, col, count + 1)

def countDown(orgHeight, maxHeight, row, col, count):
    if row >= len(trees):
        return count
    height = trees[row][col]
    if height >= orgHeight:
        return count + 1
    if height >= maxHeight:
        maxHeight = height
    return countDown(orgHeight, maxHeight, row + 1, col, count + 1)
   
    
def countLeft(orgHeight, maxHeight, row, col, count):
    if col < 0:
        return count
    height = trees[row][col]
    if height >= orgHeight:
        return count + 1
    if height >= maxHeight:
        maxHeight = height
    return countLeft(orgHeight, maxHeight, row, col - 1, count + 1)
    
def countRight(orgHeight, maxHeight, row, col, count):
    if col >= len(trees[0]):
        return count
    height = trees[row][col]
    if height >= orgHeight:
        return count + 1
    if height >= maxHeight:
        maxHeight = height
    return countRight(orgHeight, maxHeight, row, col + 1, count + 1)

def count(orgHeight, row, col):
    return countUp(orgHeight, 0, row - 1, col, 0) * countDown(orgHeight, 0, row + 1, col, 0) * countLeft(orgHeight, 0, row, col - 1, 0) * countRight(orgHeight, 0, row, col + 1, 0)

maxScore = 0
for row in range(rows):
    for col in range(cols):
        score = count(trees[row][col], row, col)
        if score > maxScore:
            maxScore = score
print(maxScore)