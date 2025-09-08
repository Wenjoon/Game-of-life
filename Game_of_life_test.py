import random
rows = []
changestatus = []
valid = []
alive = []
gamestate = 1
dead = []
boardsize = int(input("Boardsize? "))
tiles = int(input("What percent of tiles would you like to be alive? "))
t = 0
while t != ((pow(boardsize,2)) * tiles) // 100:
    tile = [random.randint(0,boardsize-1),random.randint(0,boardsize-1)]
    if tile not in alive:
        alive.append(tile)
        t += 1
for i in range (boardsize):
    rows.append(["."]*boardsize)
    for j in range (boardsize):
        valid.append([i,j])
        if [i,j] in alive:
            rows[i][j] = "0"
for r in range (pow(boardsize,2)):
    if valid[r] not in alive:
        dead.append(valid[r])
def checkneighbors(x,y):
    aliveneighbors = 0
    for i in range (-1,2):
        for j in range (-1,2):
            if [x+i,y+j] in valid and [x+i,y+j] in alive and [x+i,y+j] != [x,y]:
                aliveneighbors += 1
    if [x,y] in dead and aliveneighbors == 3:
        changestatus.append([x,y])
    if [x,y] in alive and (aliveneighbors < 2 or aliveneighbors > 3):
        changestatus.append([x,y])
def genboard():
    for r in range (len(changestatus)):
        if changestatus[r] in alive:
            rows[changestatus[r][0]][changestatus[r][1]] = "."
            alive.remove([changestatus[r][0],changestatus[r][1]])
            dead.append([changestatus[r][0],changestatus[r][1]])
        elif changestatus[r] in dead:
            rows[changestatus[r][0]][changestatus[r][1]] = "0"
            dead.remove([changestatus[r][0],changestatus[r][1]])
            alive.append([changestatus[r][0],changestatus[r][1]])
    for r in range (boardsize):
        print (*rows[r])
    changestatus.clear()
    for i in range (boardsize):
        for j in range (boardsize):
            checkneighbors(i,j)
while gamestate == 1:
    genboard()