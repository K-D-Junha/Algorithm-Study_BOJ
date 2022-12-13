def promising(seq, i):
    if i in seq:
        return False
    if i <= seq[-1]:
        return False
    return True
    
def dfs(seq, N, toPick):
    if toPick == 0:
        print(' '.join(map(str,seq)))
        return
    for i in range(1, N+1):
        if promising(seq, i) == True:
            seq.append(i)
            dfs(seq, N, toPick-1)
            seq.pop(-1)
    

N, M = list(map(int, input().split()))

seq = []
for i in range(1,N+1):
    seq.append(i)
    dfs(seq, N, M-1)
    seq.pop(-1)