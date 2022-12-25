import math

def calDiff(visited, N):
    start_score=0; link_score=0
    start_team = []
    link_team = []
    for i in range(1,N+1):
        if visited[i] == True:
            start_team.append(i)
        else:
            link_team.append(i)

    for i in start_team:
        for j in start_team:
            start_score += scores[i-1][j-1]
    for i in link_team:
        for j in link_team:
            link_score += scores[i-1][j-1]
    return abs(start_score-link_score)


def dfs(team_cnt, visited, try_cnt,N, max_diff, lastpick):
    if try_cnt[0]>try_cnt[1]: return
    if team_cnt == N//2:
        try_cnt[0] += 1
        sc_diff = calDiff(visited, N)
        if sc_diff < max_diff[0]:
            max_diff[0] = sc_diff
        return
    for i in range(lastpick+1,N+1):
        if visited[i] == False:
            visited[i] = True
            dfs(team_cnt+1, visited, try_cnt, N, max_diff, i)
            if try_cnt[0]>try_cnt[1]: return
            visited[i] = False


N = int(input())
scores = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    scores[i] = list(map(int, input().split()))

visited = [False for _ in range(N+1)]
try_cnt = [0,int(math.comb(N,N//2)//2)]
max_diff = [98765432,]
dfs(0,visited,try_cnt,N,max_diff,0)
print(max_diff[0])