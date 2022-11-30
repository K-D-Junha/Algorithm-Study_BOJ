class Cnts:
    def __init__(self, cnt_2, cnt_5):
        self.cnt_2 = cnt_2
        self.cnt_5 = cnt_5
        
def count2and5(n):
    cnt_2 = 0; k = 2
    while k <= n:
        cnt_2 += (n//k)
        k *= 2
    cnt_5 = 0; k = 5
    while k <= n:
        cnt_5 += (n//k)
        k *= 5
    res = Cnts(cnt_2, cnt_5)
    return res

N, M = list(map(int, input().split()))         

cnts1 = count2and5(N)
cnts2 = count2and5(M)
cnts3 = count2and5(N-M)

ans = min((cnts1.cnt_2 - cnts2.cnt_2 - cnts3.cnt_2),
          (cnts1.cnt_5 - cnts2.cnt_5 - cnts3.cnt_5))
print(ans)