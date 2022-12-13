def checkAandB(A, B):
    if A % 2 == 1:
        if B == (A+1):
            return True
    return False

N, a, b = list(map(int, input().split()))
A = min(a,b); B = max(a,b)

round = 0
res = -1
while N >= 2:
    round += 1
    if checkAandB(A,B) == True:
        res = round
        break
    else:
        A = (A+1) //2
        B = (B+1) //2
        if N%2 == 0:
            N = N//2
        else:
            N = (N+1)//2

print(res)