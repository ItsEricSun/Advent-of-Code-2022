with open("day6/input.txt", "r") as file:
    line = file.readline()
    for i in range(len(line) - 14):
        dup = False
        letters = line[i : i + 14]
        for letter in letters:
            if letters.count(letter) >= 2:
                dup = True
                continue
        if dup:
            continue
        else:
            print(i + 14)
            break