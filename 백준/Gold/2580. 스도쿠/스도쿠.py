import copy

class Problem:
    def __init__(self, b):
        self.board = copy.deepcopy(b)
        self.found_ans = False
        self.ans_board = []
        self.empty_rooms = []
        self.check_row = [[False for _ in range(9)] for _ in range(9)]
        self.check_col = [[False for _ in range(9)] for _ in range(9)]
        self.check_square = [[False for _ in range(9)] for _ in range(9)]
        self.findEmptyRooms()
        
    def promising(self, room, i):
        row = room[0]; col = room[1]

        if self.check_row[row][i-1] == True:
            return False
        if self.check_col[col][i-1] == True:
            return False
        if self.check_square[(row//3)*3 + (col//3)][i-1] == True:
            return False

        self.check_row[row][i-1] = True
        self.check_col[col][i-1] = True
        self.check_square[(row//3)*3 + (col//3)][i-1] = True
        
        return True

    def emptyChecks(self, room, i):
        row = room[0]; col = room[1]
        self.check_row[row][i-1] = False
        self.check_col[col][i-1] = False
        self.check_square[(row//3)*3 + (col//3)][i-1] = False

    def dfs(self):
        if len(self.empty_rooms) == 0:
            self.found_ans = True
            self.ans_board = copy.deepcopy(self.board)
            return

        room = self.empty_rooms.pop(-1)
        for i in range(1,10):
            if self.promising(room,i) == True:
                self.board[room[0]][room[1]] = i
                self.dfs()
                if self.found_ans == True:
                    return
                self.emptyChecks(room,i)
        self.board[room[0]][room[1]] = 0
        self.empty_rooms.append(room)

    def findEmptyRooms(self):
        for r in range(9):
            for c in range(9):
                i = self.board[r][c]
                if i == 0:
                    self.empty_rooms.append([r,c])
                else:
                    self.check_row[r][i-1] = True
                    self.check_col[c][i-1] = True
                    self.check_square[(r//3)*3 + (c//3)][i-1] = True

    def getBoard(self):
        s = ""
        for i in range(9):
            s += " ".join(map(str,self.ans_board[i])) + "\n"
        return s

        
board = []
for i in range(9):
    board.append(list(map(int, input().split())))

p = Problem(board)
p.dfs()
print(p.getBoard())