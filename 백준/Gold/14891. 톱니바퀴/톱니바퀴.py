class Wheel:
    def __init__(self, tooths):
        self.tooths = tooths
        self.turn_num = 0
        self.left_idx = 6; self.right_idx = 2

    def turn(self, di):
        self.turn_num += di
        self.left_idx -= di
        self.right_idx -= di
        self.left_idx %= 8
        self.right_idx %= 8

    def actualTurn(self):
        self.turn_num %= 8
        tmp = [0 for _ in range(8)]
        st = self.turn_num
        for i in range(8):
            tmp[(st+i)%8] = self.tooths[i]
        self.tooths = tmp

class WheelSet:
    def __init__(self, tooths):
        self.wheels = []
        for i in range(len(tooths)):
            w = Wheel(tooths[i])
            self.wheels.append(w)

    def turnWheels(self, num, di):
        turn_list = []
        for i in range(num-1,-1,-1):
            if self.wheels[i].tooths[self.wheels[i].right_idx] != self.wheels[i+1].tooths[self.wheels[i+1].left_idx]:
                this_di = di * (1 if abs(num-i) % 2 == 0 else -1)
                turn_list.append([i,this_di])
            else:
                break
        for i in range(num+1, len(self.wheels)):
            if self.wheels[i].tooths[self.wheels[i].left_idx] != self.wheels[i-1].tooths[self.wheels[i-1].right_idx]:
                this_di = di * (1 if abs(num-i) % 2 == 0 else -1)
                turn_list.append([i,this_di])
            else:
                break
        for w in turn_list:
            self.wheels[w[0]].turn(w[1])
        self.wheels[num].turn(di)

    def actualTurnWheels(self):
        for i in range(len(self.wheels)):
            self.wheels[i].actualTurn()

    def getScore(self):
        score = 0
        for i in range(len(self.wheels)):
            if self.wheels[i].tooths[0] == 1:
                score += 2**i
        return score

tooths=[]
for i in range(4):
    str = input()
    t = []
    for j in range(8):
        t.append(int(str[j]))
    tooths.append(t)

wheel_set = WheelSet(tooths)
K = int(input())
for i in range(K):
    num, di = list(map(int, input().split()))
    wheel_set.turnWheels(num-1, di)
wheel_set.actualTurnWheels()
ans = wheel_set.getScore()
print(ans)
