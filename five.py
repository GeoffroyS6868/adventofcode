file = open("temp.txt", "r")

stock: list[list[str]] = []

stock.append(["D", "L", "V", "T", "M", "H", "F"])
stock.append(["H", "Q", "G", "J", "C", "T", "N", "P"])
stock.append(["R", "S", "D", "M", "P", "H"])
stock.append(["L", "B", "V", "F"])
stock.append(["N", "H", "G", "L", "Q"])
stock.append(["W", "B", "D", "G", "R", "M", "P"])
stock.append(["G", "M", "N", "R", "C", "H", "L", "Q"])
stock.append(["C", "L", "W"])
stock.append(["R", "D", "L", "Q", "J", "Z", "M", "T"])

for line in file:
    splittedline = line.split(" ")
    nbToMove = int(splittedline[1])
    fromStack = int(splittedline[3]) - 1
    toStack = int(splittedline[5]) - 1
    tempArray = stock[fromStack][len(stock[fromStack])-nbToMove:]
    stock[fromStack] = stock[fromStack][:len(stock[fromStack])-nbToMove]
    # Ligne du dessous sert pour le premier exercice du jour 5
    # tempArray.reverse()
    for c in tempArray:
        stock[toStack].append(c)

for t in stock:
    print(t[len(t)-1])