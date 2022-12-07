N = int(input())

N_len = len(str(N))
if N_len == 1:
    below_9 = 0
else:
    below_9 = int("9"*(N_len-1))
cnt = (N - below_9) * N_len

for i in range(1, N_len):
    cnt += 9 * (10 ** (i-1)) * i

print(cnt)
