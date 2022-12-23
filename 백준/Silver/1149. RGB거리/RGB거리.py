import sys

class Problem:
    def __init__(self):
        self.solve()

    def solve(self):
        R = 0
        G = 1
        B = 2
        N = int(input())
        colors_cost = [[] for _ in range(N)]
        for i in range(N):
            costs = list(map(int, input().split()))
            colors_cost[i] = costs
        cache_R = [0 for _ in range(N)]    #min cost when colored R(G,B) at i-th house
        cache_G = [0 for _ in range(N)]
        cache_B = [0 for _ in range(N)]

        cache_R[0] = colors_cost[0][R]
        cache_G[0] = colors_cost[0][G]
        cache_B[0] = colors_cost[0][B]
        for i in range(1,N):
            cache_R[i] = colors_cost[i][R] + min(cache_G[i-1],cache_B[i-1])
            cache_G[i] = colors_cost[i][G] + min(cache_R[i-1],cache_B[i-1])
            cache_B[i] = colors_cost[i][B] + min(cache_R[i-1],cache_G[i-1])

        ans = min(cache_R[N-1], cache_G[N-1], cache_B[N-1])
        print(ans)
    
p = Problem()