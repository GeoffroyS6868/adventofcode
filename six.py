file = open("temp.txt", "r")

def check(i, line):
    test = line[i:i+3]
    print(test, line[i+3])

    if test[0] == test[1] or test[0] == test[2] or test[1] == test[2]:
        return False
    if line[i+3] not in test:
        return True
    return False

def gigacheck(i, line):
    test = line[i:i+14]
    print(test, line[i+14])

    for l in test:
        temp = 0
        for j in test:
            if j == l:
                temp += 1
        if temp > 1:
            return False
    if line[i+14] not in test:
        return True
    return False

i = 0

for line in file:
    for _ in line:
        if gigacheck(i, line):
            i += 14
            break
        i += 1

print(i)