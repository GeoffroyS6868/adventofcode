file = open("temp.txt", "r")

def have_same_characters(str1, str2):
    for c in str1:
        for d in str2:
            if c == d:
                return c
    raise BaseException("lol")

def have_same_character(str1, str2, str3):
    for c in str1:
        for d in str2:
            for e in str3:
                if c == d and d == e:
                    return c
    raise BaseException("lol")

def point(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return ord(c) - 96
    return ord(c) - 38

total = 0

l = []

for line in file:

    """first = line[:int((len(line)/2))]
    second = line[int(len(line)/2):]"""

    l.append(line)

    if len(l) == 3:
        try:
            c = have_same_character(l[0], l[1], l[2])
            total += point(c)
        except:
            print("")
        l = []

    """try:
        c = have_same_characters(first, second)
        pts = point(c)
        total += pts
    except:
        print("")"""

print(total)