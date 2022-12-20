import sys

class Problem:
    def __init__(self):
        N = int(input())
        self.nums = list(map(int, sys.stdin.readline().split()))
        self.cache = [0 for _ in range(N)]   #cache: max_sum containing nums[i](restriction needed)
        self.solve(N)

    def solve(self, N):
        self.cache[0] = self.nums[0]
        for i in range(1,N):
            if self.cache[i-1] < 0:
                self.cache[i] = self.nums[i]
            else:
                self.cache[i] = self.cache[i-1] + self.nums[i]

        max = self.cache[0]
        for i in range(1,N):
            if self.cache[i]>max:
                max = self.cache[i]
        print(max)
    
p = Problem()