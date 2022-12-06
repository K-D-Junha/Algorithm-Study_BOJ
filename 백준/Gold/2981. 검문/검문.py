def gcd(a,b):
    while b>0:
        r = a%b
        a = b
        b = r
    return a

N = int(input())
ns = []
for i in range(N):
    ns.append(int(input()))

ns = sorted(ns)
ks = []
for i in range(N-1):
    ks.append(ns[i+1]-ns[i])

M = ks[0]
for i in range(N-2):
    M = gcd(max(M,ks[i+1]),min(M,ks[i+1]))

left = []; right = []
i = 2
while i**2 <= M:
    if M % i == 0:
        left.append(i)
        if M // i != i:
            right.append(M//i)
    i += 1
right.reverse()
ans = left+right
ans.append(M)
print(" ".join(map(str,ans)))