class Robot:
    def __init__(self, rooms, r, c, di, N, M):
        self.cleanedRoom = 0
        self.rooms = rooms
        self.N = N; self.M = M
        self.row = r
        self.col = c
        self.di = di
        self.check4ways = 0
        self.movedir = [[-1,0], [0,+1], [+1,0], [0,-1]]
        
        
    def operate(self):
        flag_go1 = True
        while True:
            if flag_go1 == True:
                self.cleanRoom()
            flag_go1 = False
            self.check4ways = 0
            while self.check4ways < 4:
                if self.checkLeft() == True:
                    self.rotate()
                    self.forward()
                    flag_go1 = True
                    break
                else:
                    self.rotate()
                    self.check4ways += 1
                    continue
            if flag_go1 == True:
                continue
            else:
                if self.checkBack() == False:
                    break
                else:
                    self.backward()
                    continue
            
    def checkLeft(self):
        if self.di == 0:
            left = 3
        else:
            left = self.di-1
        if (self.row+self.movedir[left][0] >=0 and self.row+self.movedir[left][0] < self.N 
        and self.col+self.movedir[left][1] >= 0 and self.col+self.movedir[left][1]<self.M
        and self.rooms[self.row+self.movedir[left][0]][self.col+self.movedir[left][1]]) == 0:
            return True
        else:
            return False

    def checkBack(self):
        if (self.row-self.movedir[self.di][0] >=0 and self.row-self.movedir[self.di][0] < self.N 
        and self.col-self.movedir[self.di][1] >= 0 and self.col-self.movedir[self.di][1]<self.M
        and self.rooms[self.row-self.movedir[self.di][0]][self.col-self.movedir[self.di][1]]) != 1:
            return True
        else:
            return False
                
    def cleanRoom(self):
        self.rooms[self.row][self.col] = 2
        self.cleanedRoom += 1

    def rotate(self):
        if self.di == 0:
            self.di = 3
        else:
            self.di -= 1
            
    def backward(self):
        self.row -= self.movedir[self.di][0]
        self.col -= self.movedir[self.di][1]

    def forward(self):
        self.row += self.movedir[self.di][0]
        self.col += self.movedir[self.di][1]
    
        
N, M = list(map(int, input().split()))
r, c, di = list(map(int, input().split()))
rooms = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    rooms[i] = list(map(int, input().split()))

robot = Robot(rooms, r, c, di, N, M)
robot.operate()
ans = robot.cleanedRoom
print(ans)