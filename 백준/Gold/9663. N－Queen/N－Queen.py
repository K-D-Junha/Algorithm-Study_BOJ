def promising(i, depth, visited, queens):
    if visited[i] == True:
        return False
    idx = 0
    for q in queens:
        idx += 1
        if abs(idx-depth) == abs(q-i):
            return False
    return True

def dfs(N, depth, visited, queens, ways):
    if depth == N:
        ways[0] += 1; return
    for i in range(1,N+1):
        if promising(i,depth+1,visited,queens) == True:
            visited[i] = True; queens.append(i)
            dfs(N,depth+1,visited,queens,ways)
            visited[i] = False; queens.pop(-1)


N = int(input())
ways = [0,]
visited = [False for _ in range(N+1)]
queens = []
dfs(N,0,visited,queens,ways)
print(ways[0])