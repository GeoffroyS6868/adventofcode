file = open("temp.txt", "r")
temp = []
i = 0
temp.append(0)
for line in file:
    if line == "" or line == "\n":
        i += 1
        temp.append(0)
    else:
        temp[i] += int(line)

temp.sort(reverse=True)

print(temp[0])
print(temp[0] + temp[1] + temp[2])