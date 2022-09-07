def sum(a,b,c):
    return a+b+c

def printBoard(xState,zState):
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    nine = 'X' if xState[9] else ('O' if zState[9] else 9)
    print(f"                        {one} | {two} | {three} ")
    print(f"                       ---|---|---")
    print(f"                        {four} | {five} | {six} ")
    print(f"                       ---|---|---")
    print(f"                        {seven} | {eight} | {nine} ") 
    print()
    print()

def checkWin(xState, zState):
    wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("         X Won the match")
            printBoard(xState,zState)
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("         O Won the match")
            printBoard(xState,zState)
            return 0
    return -1
    
if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    s=[1,2,3,4,5,6,7,8,9]
    turn = 1 # 1 for X and 0 for O
    count=0
    print()
    print()
    print("                   ----Welcome to Tic Tac Toe---                       ")
    print()
    print()
    while(True):
        printBoard(xState, zState)
        if count>=9:
            print("         Match draw")
            print()
            break    
        else:
            if(turn == 1):
                print("         X's Chance")
                print()
                value = int(input("         Please enter a value from 1 to 9: "))
                print()
                while value<=0 or value>9:
                    print("         Value Not in Range")
                    print()
                    print("         Pls enter a valid value")
                    print()
                    value = int(input("         Please enter a value from 1 to 9: "))
                    print()
                else:
                    while value not in s:
                        print("         Space already Occupied")
                        print()
                        value = int(input("         Please enter a value of unoccupied cell: "))
                        print()
                    else:
                        xState[value]=1
                        s.remove(value)
                    count+=1
            else:
                print("         O's Chance")
                print()
                value = int(input("         Please enter a value from 1 to 9: "))
                print()
                while value<=0 or value>9:
                    print("         Pls enter a valid value")
                    print()
                    value = int(input("         Please enter a value from 1 to 9: "))
                    print()
                else:
                    while value not in s:
                        print("         Space already Occupied")
                        print()
                        value = int(input("         Please enter a value of unoccupied cell: "))
                        print()
                    else:
                        zState[value]=1
                        s.remove(value)
                    count+=1
            cwin = checkWin(xState, zState)
            if(cwin != -1):
                print("         Match over")
                print()
                print()
                break
            
            turn = 1 - turn