#!/usr/bin/env python3

# Check for square board?
def checkmate(board):

    board = board.upper() 
    row = board.splitlines() #แยกstringหลายบรรทัดเป็นลิสต์
    n = len(row)
    
    if n == 0: #ไม่มีแถว กระดานว่าง
        print("Blank board")
        return
    
    #check for invalid board
    for r in range(n):
        if len(row[r]) != n: 
            print("Invalid board") 
            return
        
#find king

    #set เมื่อยังไม่เจอ king
    kr = -1
    kc = -1
    c = 0

    #วนแถวกับคอลัมน์ 0-(n-1)
    for r in range(n):
        for c in range(n):
            if row[r][c] == 'K':
                kr = r
                kc = c

    #check for invalid king ไม่เกิน 1 หรือไม่มี
    if c != 1:
        print("Invalid king")
        return
    
    #Limit board 
    def Limit_board(r,c):
        return 0<=r<n and 0<=c<n

            
    #pawn checkเฉียงซ้ายขวาขึ้นบน (-1,-1),(-1,+1)
    pr = kr + 1
    pc1 = kc -1
    pc2 = kc +1
    if Limit_board(pr, pc1)and row[pr][pc1] == 'P' :
        print("Success")
        return
    if Limit_board(pr, pc2) and row[pr][pc2] == 'P' :
        print("Success")
        return

    #rook and queen check+
    #checkบนking
    r = kr -1
    while Limit_board(r, kc):
        if row[r][kc] != '.' :
            if row[r][kc] == 'R' or row[r][kc] == 'Q' :
                print("Success")
                return
            break
        r-=1
    #checkล่างking
    r = kr + 1
    while Limit_board(r, kc):
        if row[r][kc] != '.' :
            if row[r][kc] == 'R' or row[r][kc] == 'Q' :
                print("Success")
                return
            break
        r+=1
    #checkซ้าย
    c = kc - 1
    while Limit_board(kr, c):
        if row[kr][c] != '.' :
            if row[kr][c] == 'R' or row[kr][c] == 'Q' :
                print("Success")
                return
            break
        c-=1
    #check-;k
    c = kc + 1
    while Limit_board(kr, c):
        if row[kr][c] != '.' :
            if row[kr][c] == 'R' or row[kr][c] == 'Q' :
                print("Success")
                return
            break
        c+=1
    
    #Bichop & Queen checkx
    #ซ้ายบน
    r = kr - 1
    c = kc - 1
    while Limit_board(r, c):
        if row[r][c] != '.' :
            if row[r][c] == 'B' or row[r][c] == 'Q' :
                print("Success")
                return
            break
        r-=1
        c-=1
    #ขวาบน
    r = kr - 1
    c = kc + 1
    while Limit_board(r, c):
        if row[r][c] != '.' :
            if row[r][c] == 'B' or row[r][c] == 'Q' :
                print("Success")
                return
            break
        r-=1
        c+=1
    #ซ้ายล่าง
    r = kr + 1
    c = kc - 1
    while Limit_board(r, c):
        if row[r][c] != '.' :
            if row[r][c] == 'B' or row[r][c] == 'Q' :
                print("Success")
                return
            break
        r+=1
        c-=1
    #ขวาล่าง
    r = kr + 1
    c = kc + 1
    while Limit_board(r, c):
        if row[r][c] != '.' :
            if row[r][c] == 'B' or row[r][c] == 'Q' :
                print("Success")
                return
            break
        r+=1
        c+=1
    
    print("Fail")