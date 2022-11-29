import math

def sub_pattern(first_row, first_col, k, data, coord, part):
    if part == 5:
        for i in range(first_row, first_row + 3**k):
            for j in range(first_col, first_col + 3**k):
                data[i][j] = ' '
        return
    if k == 1:
        data[first_row+1][first_col+1] = ' '
        return
    for i in range(9):
        sub_pattern(first_row+(3**(k-1))*coord[i][0], first_col+(3**(k-1))*coord[i][1],
                    k-1,data,coord,i+1)


def build_s(N,data):
    s = ""
    for i in range(N):
        s += ''.join(data[i])
        s += "\n"
    print(s)

N = int(input())

square = [['*' for j in range(N)] for i in range(N)]
coord_list = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
k = round(math.log(N,3))
sub_pattern(0,0,k,square,coord_list,1)

build_s(N,square)
