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
    
def getHand(other, outcome):
    if other == "A":
        if outcome == "X":
            return "Z"
        elif outcome == "Y":
            return "X"
        else:
            return "Y"
    elif other == "B":
        if outcome == "X":
            return "X"
        elif outcome == "Y":
            return "Y"
        else:
            return "Z"
    else:
        if outcome == "X":
            return "Y"
        elif outcome == "Y":
            return "Z"
        else:
            return "X" 

score = 0
with open("day2/input.txt", "r") as file:
    for line in file.readlines():
        line = line.rstrip()
        hands = line.split(" ")
        myHand = getHand(hands[0], hands[1])
        score += shapeScore(myHand) + outcomeScore(myHand, hands[0])
print(score)