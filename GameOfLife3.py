import os
import random
boardsize = int(input("Size of board? "))
percentoftiles = boardsize * boardsize * int(input("Percent of tiles? ")) // 100
board = []
change = []
for r in range(boardsize):
    board.append(' '*boardsize)
while len(change) != percentoftiles:
    newtile = [random.randint(0,boardsize-1),random.randint(0,boardsize-1)]
    if newtile not in change:
        change.append(newtile)
def printboard():
    for r in range(boardsize):
        print(*board[r])
def check(x,y):
    neighbors = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0: continue
            if board[(x + i) % boardsize][(y + j) % boardsize] == '0':
                neighbors += 1
    if board[x][y] == '0' and (neighbors > 3 or neighbors < 2):
        change.append([x,y])
    if board[x][y] == ' ' and neighbors == 3:
        change.append([x,y])
def run():
    os.system("clear")
    printboard()
    for r in range(len(change)):
        if board[change[r][0]][change[r][1]] == ' ':
            board[change[r][0]] = board[change[r][0]][:change[r][1]] + '0' + board[change[r][0]][change[r][1]+1:]
        else:
            board[change[r][0]] = board[change[r][0]][:change[r][1]] + ' ' + board[change[r][0]][change[r][1]+1:]
    change.clear()
    for i in range(boardsize):
        for j in range(boardsize):
            check(i,j)
while 1:
    run()