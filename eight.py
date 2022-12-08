file = open("temp.txt", "r")

def isVisible(y, x, tab, value):

    i = x
    j = y
    found = True

    while i > 0:
        i -= 1
        if tab[y][i] >= value:
            found = False
            break

    if found == True:
        return True

    i = x
    found = True

    while i < len(tab[0]) - 1:
        i += 1
        if tab[y][i] >= value:
            found = False
            break

    if found == True:
        return True

    found = True

    while j > 0:
        j -= 1
        if tab[j][x] >= value:
            found = False
            break

    if found == True:
        return True

    found = True
    j = y

    while j < len(tab) - 1:
        j += 1
        if tab[j][x] >= value:
            found = False
            break

    return found

def getScore(y, x, tab, value):

    i = x
    j = y
    totalscore = 0
    score = 0

    while i > 0:
        i -= 1
        score += 1
        if tab[y][i] >= value:
            break

    totalscore = score
    score = 0
    i = x

    while i < len(tab[0]) - 1:
        i += 1
        score += 1
        if tab[y][i] >= value:
            break

    totalscore *= score
    score = 0

    while j > 0:
        j -= 1
        score += 1
        if tab[j][x] >= value:
            break

    totalscore *= score
    score = 0
    j = y

    while j < len(tab) - 1:
        j += 1
        score += 1
        if tab[j][x] >= value:
            break

    totalscore *= score
    return totalscore

tab = []

for line in file:
    temp = []
    for c in line:
        if c == '\n':
            continue
        temp.append(int(c))
    tab.append(temp)

total = 0
score = 0

y = 0
x = 0

for ytab in tab:
    for xtab in ytab:
        if isVisible(y, x, tab, xtab) == True:
            total += 1
        s = getScore(y, x, tab, xtab)
        if s > score:
            score = s
        x += 1
    x = 0
    y += 1

print(total)
print(score)