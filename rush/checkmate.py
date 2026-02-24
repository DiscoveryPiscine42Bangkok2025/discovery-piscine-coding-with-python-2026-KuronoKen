notKing = ["P","Q","B","R"]

def pawn(pawnPos:tuple, boardList:list):

    # .x.x.
    # ..P..
    # .....

    inCheck = False

    # ชี้ตำแหน่งของ Pawn ที่สามารถโจมตีได้ (left-up, right-up)
    leftAttackPos = (pawnPos[0]-1, pawnPos[1]-1)
    rightAttackPos = (pawnPos[0]+1, pawnPos[1]-1)

    # เช็คตัวซ้ายให้ไม่อยู่เกินกระดาน
    if leftAttackPos[0] >= 0 and leftAttackPos[1] >= 0:
        if boardList[leftAttackPos[1]][leftAttackPos[0]] == "K": #boardList[row][col] == K มั้ย
            inCheck = True

    # เช็คตัวขวาให้ไม่อยู่เกินกระดาน
    if rightAttackPos[0] < len(boardList) and rightAttackPos[1] >= 0:
        if boardList[rightAttackPos[1]][rightAttackPos[0]] == "K": #boardList[row][col] == K มั้ย
            inCheck = True

    return inCheck

def rook(rookPos:tuple,boardList:list):

    # ...x...
    # ...x...
    # xxxRxxx
    # ...x...
    # ...x...
    inCheck = False

    # ขนาดกระดาน square
    boardSize = len(boardList)

    #Left
    currentPos = (rookPos[0]-1,rookPos[1]) #เริ่มจากทางซ้ายของ rook

    #loop เรื่อยๆจนกว่าจะสุดกระดาน
    while currentPos[0] >= 0:
        currentPiece = boardList[currentPos[1]][currentPos[0]]
        if currentPiece in notKing: # ถ้าเจอตัวอื่นบัง
            break
        if currentPiece == "K":
            inCheck = True
            break
        currentPos = (currentPos[0]-1,currentPos[1]) #ถ้าไม่โดนบังหรือยังไม่เจอ King ขยับซ้ายอีก
    
    if inCheck:
        return inCheck

    #Right
    currentPos = (rookPos[0]+1,rookPos[1]) #เริ่มจากทางขวาของ rook
    
    #loop เรื่อยๆจนกว่าจะสุดกระดาน
    while currentPos[0] < boardSize:
        currentPiece = boardList[currentPos[1]][currentPos[0]]
        if currentPiece in notKing: # ถ้าเจอตัวอื่นบัง
            break
        if currentPiece == "K":
            inCheck = True
            break
        currentPos = (currentPos[0]+1,currentPos[1]) #ถ้าไม่โดนบังหรือยังไม่เจอ King ขยับขวาอีก

    if inCheck:
        return inCheck

    #Down
    currentPos = (rookPos[0],rookPos[1]+1) #เริ่มจากข้างล่างของ rook

    #loop เรื่อยๆจนกว่าจะสุดกระดาน
    while currentPos[1] < boardSize:
        currentPiece = boardList[currentPos[1]][currentPos[0]]
        if currentPiece in notKing: # ถ้าเจอตัวอื่นบัง
            break
        if currentPiece == "K":
            inCheck = True
            break
        currentPos = (currentPos[0],currentPos[1]+1) #ถ้าไม่โดนบังหรือยังไม่เจอ King ขยับลงอีก

    if inCheck:
        return inCheck
    
    #Up
    currentPos = (rookPos[0],rookPos[1]-1) #เริ่มจากข้างบนของ rook

    #loop เรื่อยๆจนกว่าจะสุดกระดาน
    while currentPos[1] >= 0:
        currentPiece = boardList[currentPos[1]][currentPos[0]]
        if currentPiece in notKing: # ถ้าเจอตัวอื่นบัง
            break
        if currentPiece == "K":
            inCheck = True
            break
        currentPos = (currentPos[0],currentPos[1]-1) #ถ้าไม่โดนบังหรือยังไม่เจอ King ขยับขึ้นอีก

    return inCheck

def bishop(bishopPos:tuple, boardList:list):

    #x...x
    #.x.x.
    #..B..
    #.x.x.
    #x...x

    #left-up
    currentPos = (bishopPos[0]-1,bishopPos[1]-1) #เริ่มเช็คจากช่องซ้ายบน (เหมือนกับ pawn)

    #เช็คว่าสุดกระดานยัง
    while currentPos[0] >= 0 and currentPos[1] >= 0:
        piece = boardList[currentPos[1]][currentPos[0]] #ดูหมากใน currentPos
        if piece == "K":
            return True
        elif piece in notKing:
            break
        currentPos = (currentPos[0]-1,currentPos[1]-1) #เขยิบขึ้นบนซ้าย

    #right-up
    currentPos = (bishopPos[0]+1,bishopPos[1]-1) #เริ่มเช็คจากช่องขวาบน (เหมือนกับ pawn)

    #เช็คว่าสุดกระดานยัง
    while currentPos[0] <= len(boardList[0])-1 and currentPos[1] >= 0:
        piece = boardList[currentPos[1]][currentPos[0]]
        if piece == "K":
            return True
        elif piece in notKing:
            break
        currentPos = (currentPos[0]+1,currentPos[1]-1) #เขยิบขึ้นบนขวา

    #left-down
    currentPos = (bishopPos[0]-1,bishopPos[1]+1) #เริ่มเช็คจากช่องซ้ายล่าง

    #เช็คว่าสุดกระดานยัง
    while currentPos[0] >= 0 and currentPos[1] <= len(boardList)-1 :
        piece = boardList[currentPos[1]][currentPos[0]]
        if piece == "K":
            return True
        elif piece in notKing:
            break
        currentPos = (currentPos[0]-1,currentPos[1]+1) #เขยิบลงซ้ายล่าง

    #right-down
    currentPos = (bishopPos[0]+1,bishopPos[1]+1) #เริ่มเช็คจากช่องขวาล่าง

    #เช็คว่าสุดกระดานยัง
    while currentPos[0] <= len(boardList[0])-1 and currentPos[1] <= len(boardList)-1 :
        piece = boardList[currentPos[1]][currentPos[0]]
        if piece == "K":
            return True
        elif piece in notKing:
            break
        currentPos = (currentPos[0]+1,currentPos[1]+1) #เขยิบลงขวาล่าง

    return False #ถ้าไม่ check เจอ king

def checkmate(board:str):

    # check ว่า มีข้อมูลเข้ามาหรือไม่ ถ้าไม่จะแสดง There is no board
    if not board:
        print("There is no board.")
        return
    
    #แปลงให้ตัวอักษรที่เข้ามาเป็นตัวพิมพ์ใหญ่ทั้งหมด และ กันไม่ให้ใส่ช่องว่าง
    board = board.upper().replace(" ","")
    boardList = board.split() #เก็บแต่ละแถวเป็น list

    boardHeight = len(boardList) #จำนวน row ของกระดาน
    kingCount = 0 # นับจำนวน King
    boardWidth = -1 #ความกว้างของกระดาน ยังไม่ check ให้เป็น -1
    inCheck = False 
    
    #loop เข้าไปใน list boardList
    for row in boardList:
        rowLength = len(row) 
        if boardWidth == -1: #เช็คถ้ายังไม่เคยเช็คความกว้างของ row
            boardWidth = rowLength
        elif boardWidth != rowLength: #return ถ้าจำนวนแต่ละ row มีความกว้างไม่เท่ากัน
            print("The board is invalid.")
            return
        
        kingCount += row.count("K")
    
    if boardHeight != boardWidth: #ต้องเป็น square only
        print("The board is not a square.")
        return
    elif kingCount != 1:
        if not kingCount: # ไม่มี king ในกระดาน
            print("No king is found on the board.")
        else: # มี king ในกระดาน > 1
            print("There is multiple king on the board.")
        return

    #loop เช็คทุกช่องของกระดานว่ามีตัวไหนโจมตี King ได้หรือไม่
    for rowIndex, row in enumerate(boardList):
        for columnIndex, piece in enumerate(row):

            if inCheck:
                break

            if piece == "P":
                if pawn((columnIndex, rowIndex), boardList):
                    inCheck = True

            elif piece == "R":
                if rook((columnIndex, rowIndex), boardList):
                    inCheck = True

            elif piece == "B":
                if bishop((columnIndex, rowIndex), boardList):
                    inCheck = True

            elif piece == "Q":
                if bishop((columnIndex, rowIndex), boardList) or rook((columnIndex, rowIndex), boardList):
                    inCheck = True

    if inCheck:
        print("Success")
    else:
        print("Fail")