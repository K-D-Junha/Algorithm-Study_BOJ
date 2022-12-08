def checkBingo(board):
    bingo_lines = 0
    for r in range(5):
        cnt_0 = 0
        for c in range(5):
            if board[r][c] == 0:
                cnt_0 += 1
        if cnt_0 == 5:
            bingo_lines += 1

    for c in range(5):
        cnt_0 = 0
        for r in range(5):
            if board[r][c] == 0:
                cnt_0 += 1
        if cnt_0 == 5:
            bingo_lines += 1

    cnt_0 = 0
    for i in range(5):
        if board[i][i] == 0:
            cnt_0 += 1
    if cnt_0 == 5:
        bingo_lines += 1

    cnt_0 = 0
    for i in range(5):
        if board[4-i][i] == 0:
            cnt_0 += 1
    if cnt_0 == 5:
        bingo_lines += 1
            
    return bingo_lines

board = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    board[i] = list(map(int, input().split()))

call_nums = []
for i in range(5):
    call_nums.extend(list(map(int, input().split())))

call_cnt = 0
for c in call_nums:
    call_cnt += 1
    idx = [(i,j) for i in range(5) for j in range(5) if board[i][j]==c]
    idx = idx[0]
    board[idx[0]][idx[1]] = 0
    if checkBingo(board) >= 3:
        print(call_cnt)
        break