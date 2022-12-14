file = open("temp.txt", "r")
score = 0

def letterToInt(l):
    if l == "A" or l == "X":
        return 1
    if l == "B" or l == "Y":
        return 2
    if l == "C" or l == "Z":
        return 3

def iwin(he, you):
    if you > he:
        if you == 3 and he == 1:
            return False
        return True
    if you == 1 and he == 3:
        return True
    return False

temp = []

for line in file:
    spl = line.split(" ")
    he = spl[0]
    you = spl[1][0:1]
    temp.append([letterToInt(he), letterToInt(you)])

"""for line in temp:
    he = line[0]
    you = line[1]
    if he == you:
        score += (you + 3)
    else:
        if iwin(he, you):
            score += 6 + you
        else:
            score += you"""

for line in temp:
    he = line[0]
    you = line[1]
    if you == 1:
        you = he - 1
        if you == 0:
            you = 3
        score += you
    elif you == 2:
        score += he + 3
    else:
        you = he + 1
        if you == 4:
            you = 1
        score += you + 6
print(score)
