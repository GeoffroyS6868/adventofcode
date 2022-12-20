file = open("temp.txt", "r")

directories = {"/home": 0}
path = "/home"

for line in file:
    if line[0] == "$":
        if line[2:4] == "cd":
            if line[5:6] == "/":
                path = "/home"
            elif line[5:7] == "..":
                path = path[0:path.rfind("/")]
            else:
                path = path + "/" + line[5:]
                directories.update({path: 0})
    elif line[:3] != "dir":
        size = int(line[:line.find(" ")])
        tempPath = path
        for i in range(path.count("/")):
            directories[tempPath] += size
            tempPath = tempPath[:tempPath.rfind("/")]

total = 0
limit = 30000000 - (70000000 - directories["/home"])
valid_dirs = []

for dir in directories:
    if directories[dir] < 100000:
        total += directories[dir]
    if limit <= directories[dir]:
        valid_dirs.append(directories[dir])

print(total)
print(min(valid_dirs))
