#made by Jesse Gomer
import math


class boardClass:
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    
    def __init__(self):
        for each in range(9):
            self.board.append(0)
            
    def Clear(self):
        i=0
        for each in range(9):
            self.board[i]=0
            i+=1

    def Print(self):
        i=0
        for each in range(3):
            row=""
            for each in range(3):
                if self.board[i]==3:
                    row+="X"
                if self.board[i]==4:
                    row+="O"
                if self.board[i]==0:
                    row+="#"
                i+=1
            print(row)
    def Check(self):
        i=0
        x=0
        for each in range(8):
            total=0
            x=0
            for each in range(3):
                total+=self.board[self.win[i][x]]
                x+=1
            if total==9:
                return 1
            if total==12:
                return 2
            i+=1
        return 0
    def MakeChange(self,symbol,space):
        self.board[space]=symbol


class aiBoardClass(boardClass):  #special subclass of board that changes the check method to see if someone can win
    def Check(self):
        i=0
        x=0
        for each in range(8):
            total=0
            x=0
            for each in range(3):
                total+=self.board[self.win[i][x]]
                x+=1
            if total==6:
                return [1,i]
            i+=1
        i=0
        x=0
        for each in range(8):
            total=0
            x=0
            for each in range(3):
                total+=self.board[self.win[i][x]]
                x+=1
            if total==8:
                return [2,i]
            i+=1
        return [0,i]

    def Count(self):     #shows the number of moves made
        i=0
        x=0
        for each in self.board:
            if self.board[i] > 0:
                x+=1
            i+=1
        return x
    
    def anyFilled(self,spaces):
        i=0
        for each in spaces:
            if self.board[spaces[i]]>0:
                return spaces[i]
            i+=1
        return -1


    
class aiClass:
    aiBoard=aiBoardClass()

    def winMove(self):
        result=self.aiBoard.Check()
        if result[0]==0:
            return -1
        if result[0]==1:
            x=0
            for each in range(3):
                if self.aiBoard.board[self.aiBoard.win[result[1]][x]]==0:
                    return self.aiBoard.win[result[1]][x]
                x+=1
        if result[0]==2:
            x=0
            for each in range(3):
                if self.aiBoard.board[self.aiBoard.win[result[1]][x]]==0:
                    return self.aiBoard.win[result[1]][x]
                x+=1

    
    def DoMove(self,board):
        self.aiBoard.board=board
        count=self.aiBoard.Count()
        if self.winMove() > -1:
            return self.winMove()
        if count==0:
            return 0
        if count==2:
            if self.aiBoard.anyFilled([1,2,5])>-1:
                return 6
            return 2
        if count==4:
            print("count 4 ran")
            if self.aiBoard.anyFilled([8])==-1:
                return 8
            if self.aiBoard.anyFilled([2])==-1:
                return 2
            if self.aiBoard.anyFilled([6])==-1:
                return 6
        if count==6:
            if self.aiBoard.anyFilled([6])==-1:
                return 6
            if self.aiBoard.anyFilled([8])==-1:
                return 8
        
        
        
        return 0



def humanMove(board):

    print("here is how the board is laid out: \n123 \n456 \n789")
    while True:

        move=0
        move=(int(input("press the number corresponding to your choice: "))-1)
        if move>=9:
            print("the move must be between 1 and 9")
            continue
        if board[move]==0:
            return move
        else:
            print("You cannot make a move in that space, please make another selection.")
            continue

theBoard=boardClass()

ai=aiClass()


while True:
    theBoard.Clear()
    turns=1
    while turns <= 9:
        theBoard.Print()
        print(" ")
        if (turns%2==1):
            theBoard.MakeChange(3,ai.DoMove(theBoard.board))
        if (turns%2==0):
            theBoard.MakeChange(4,humanMove(theBoard.board))
        if theBoard.Check()==0:
            if turns==9:
                theBoard.Print()
                print("Tie game")
                break
        if theBoard.Check()==1:
            theBoard.Print()
            print("AI won")
            break
        if theBoard.Check()==2:
            theBoard.Print()
            print("Human won")
            break
        turns+=1
    x= input("Do you want to play again? (press 1 for yes 2 for no) ")
    if x=="1":
        print("restarting")
    if x=="2":
        break
print("Thanks For Playing!!!")


        
