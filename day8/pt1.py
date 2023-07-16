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

def isVisibleUp(org, row, col):
    if row < 0:
        return True
    elif (org > trees[row][col]):
        return isVisibleUp(org, row - 1, col)
    else:
        return False
    
def isVisibleDown(org, row, col):
    if row >= len(trees):
        return True
    elif (org > trees[row][col]):
        return isVisibleDown(org, row + 1, col)
    else:
        return False
    
def isVisibleLeft(org, row, col):
    if col < 0:
        return True
    elif (org > trees[row][col]):
        return isVisibleLeft(org, row, col - 1)
    else:
        return False
    
def isVisibleRight(org, row, col):
    if col >= len(trees[0]):
        return True
    elif (org > trees[row][col]):
        return isVisibleRight(org, row, col + 1)
    else:
        return False

def isVisible(org, row, col):
    return isVisibleUp(org, row - 1, col) or isVisibleDown(org, row + 1, col) or isVisibleLeft(org, row, col - 1) or isVisibleRight(org, row, col + 1)
    
count = 0
for row in range(rows):
    for col in range(cols):
        if (isVisible(trees[row][col], row, col)):
            count += 1
print(count)