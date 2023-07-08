def shapeScore(me):
    if me == "X":
        return 1
    elif me == "Y":
        return 2
    else:
        return 3

def outcomeScore(me, other):
    if me == "X" and other == "C" or me == "Y" and other == "A" or me == "Z" and other == "B":
        return 6
    elif me == "X" and other == "A" or me == "Y" and other == "B" or me == "Z" and other == "C":
        return 3
    else:
        return 0
    
score = 0
with open("day2/input.txt", "r") as file:
    for line in file.readlines():
        line = line.rstrip()
        hands = line.split(" ")
        score += shapeScore(hands[1]) + outcomeScore(hands[1], hands[0])
print(score)
