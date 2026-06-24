from typing import List, Optional

class ConnectFour:
    def __init__(self, ):
        self.rows = 6
        self.cols = 7
        self.board = [[" " for col in range(self.cols)] for row in range(self.rows)]

    def move(self, col: int, player: str) -> str:
        
        row = -1
        for i in range(self.rows - 1, -1, -1):
            if self.board[i][col] == " ":
                row = i
                break
        self.board[row][col] = player
        # self.printBoard()
        if self.checkWin(row, col, player):
            # print(player)
            return player
        
        if row  == 0 and self.checkDraw(): 
            # print("DRAW")
            return "DRAW"
        # print("PENDING")
        return "PENDING"
    
    def checkWin(self, row, col, player):

        def checkDirection( row, col, player, dir):
            count = 1
            x, y = row + dir[0], col + dir[1]
            while x >= 0 and x < self.rows and y >= 0 and y < self.cols and self.board[x][y] == player:
                count += 1
                x += dir[0]
                y += dir[1]

            x, y = row - dir[0], col - dir[1]
            while x >= 0 and x < self.rows and y >= 0 and y < self.cols and self.board[x][y] == player:
                count += 1
                x -= dir[0]
                y -= dir[1]
            
            return count >= 4
        
        return (checkDirection(row, col, player, (0, 1)) or
            checkDirection(row, col, player, (1, 0)) or
            checkDirection(row, col, player, (1, 1)) or
            checkDirection(row, col, player, (1, -1))
        )         

    def checkDraw(self):
        for j in range(self.cols):
            if self.board[0][j] == " ":
                return False
        return True

    def printBoard(self, ) -> str:
        bs = []
        for i in range(self.rows):
            bs.append("|")
            for j in range(self.cols):
                bs.append(self.board[i][j])
                bs.append("|")
            if i < self.rows - 1:
                bs.append("\n")
        return print("".join(bs))
    

connectFour = ConnectFour()
connectFour.move(0, "A")
connectFour.move(0, "B")
connectFour.move(1, "A")
connectFour.move(1, "B")
connectFour.move(2, "A")
connectFour.move(2, "B")
connectFour.move(3, "A")
connectFour.printBoard()
