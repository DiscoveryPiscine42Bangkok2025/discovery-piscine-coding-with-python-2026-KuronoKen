notKing = ["P","Q","B","R"]

def pawn(pawnPos:tuple,boardList:list):
    inCheck = False
    pawnLeftPos = (pawnPos[0]-1,pawnPos[1]-1)
    pawnRightPos = (pawnPos[0]+1,pawnPos[1]-1)
    if pawnLeftPos[0] >= 0 and pawnLeftPos[1] >= 0:
        if boardList[pawnLeftPos[1]][pawnLeftPos[0]] == "K":
            inCheck = True
    if pawnRightPos[0] < len(boardList) and pawnRightPos[1] >= 0:
        if boardList[pawnRightPos[1]][pawnRightPos[0]] == "K":
            inCheck = True

    return inCheck

def rook(rookPos:tuple,boardList:list):
    inCheck = False
    widthAndHeight = len(boardList)

    #Left
    finding = (rookPos[0]-1,rookPos[1])
    while finding[0] >= 0:
        found = boardList[finding[1]][finding[0]]
        if found in notKing:
            break
        if found == "K":
            inCheck = True
            break
        finding = (finding[0]-1,finding[1])
    
    if inCheck:
        return inCheck

    #Right
    finding = (rookPos[0]+1,rookPos[1])
    while finding[0] < widthAndHeight:
        found = boardList[finding[1]][finding[0]]
        if found in notKing:
            break
        if found == "K":
            inCheck = True
            break
        finding = (finding[0]+1,finding[1])

    if inCheck:
        return inCheck

    #Down
    finding = (rookPos[0],rookPos[1]+1)
    while finding[1] < widthAndHeight:
        found = boardList[finding[1]][finding[0]]
        if found in notKing:
            break
        if found == "K":
            inCheck = True
            break
        finding = (finding[0],finding[1]+1)

    if inCheck:
        return inCheck
    
    #Up
    finding = (rookPos[0],rookPos[1]-1)
    while finding[1] >= 0:
        found = boardList[finding[1]][finding[0]]
        if found in notKing:
            break
        if found == "K":
            inCheck = True
            break
        finding = (finding[0],finding[1]-1)

    return inCheck

def bishop(bishopPos:tuple, boardList:list):
    #left-up
    finding = (bishopPos[0]-1,bishopPos[1]-1)
    while finding[0] >= 0 and finding[1] >= 0:
        found = boardList[finding[1]][finding[0]]
        if found == "K":
            return True
        elif found in notKing:
            break
        finding = (finding[0]-1,finding[1]-1)

    #right-up
    finding = (bishopPos[0]+1,bishopPos[1]-1)
    while finding[0] <= len(boardList[0])-1 and finding[1] >= 0:
        found = boardList[finding[1]][finding[0]]
        if found == "K":
            return True
        elif found in notKing:
            break
        finding = (finding[0]+1,finding[1]-1)

    #left-down
    finding = (bishopPos[0]-1,bishopPos[1]+1)
    while finding[0] >= 0 and finding[1] <= len(boardList)-1 :
        found = boardList[finding[1]][finding[0]]
        if found == "K":
            return True
        elif found in notKing:
            break
        finding = (finding[0]-1,finding[1]+1)

    #right-down
    finding = (bishopPos[0]+1,bishopPos[1]+1)
    while finding[0] <= len(boardList[0])-1 and finding[1] <= len(boardList)-1 :
        found = boardList[finding[1]][finding[0]]
        if found == "K":
            return True
        elif found in notKing:
            break
        finding = (finding[0]+1,finding[1]+1)
    return False

def checkmate(board:str):

    if not board:
        print("There is no board.")
    
    board = board.upper().replace(" ","")
    boardList = board.split()
    height = len(boardList)
    kingCount = 0
    width = -1
    inCheck = False
    
    for i in boardList:
        localLength = len(i)
        if width == -1:
            width = localLength
        elif width != localLength:
            print("The board is invalid.")
            return
        kingCount += i.count("K")
    
    if height != width:
        print("The board is not a square.")
        return
    elif kingCount != 1:
        if not kingCount:
            print("No king is found on the board.")
        else:
            print("There is multiple king on the board.")
        return

    for lnIndex, line in enumerate(boardList):
        for colIndex, col in enumerate(line):
            if inCheck:
                break
            if col == "P":
                if pawn((colIndex,lnIndex),boardList):
                    inCheck = True
            elif col == "R":
                if rook((colIndex,lnIndex),boardList):
                    inCheck = True
            elif col == "B":
                if bishop((colIndex,lnIndex),boardList):
                    inCheck = True
            elif col == "Q":
                if bishop((colIndex,lnIndex),boardList) or rook((colIndex,lnIndex),boardList):
                    inCheck = True

    if inCheck:
        print("Success")
    else:
        print("Fail")