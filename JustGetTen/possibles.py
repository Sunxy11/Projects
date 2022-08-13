from bases import *
def check_cell(i,j,gameboard,n):
    range_num=[i for i in range(1,n)]
    if i == j == 0:
        return gameboard[i][j] == gameboard[i+1][j] or gameboard[i][j] == gameboard[i][j+1]
    elif i == 0 and j == n-1:
        return gameboard[i][j] == gameboard[i+1][j] or gameboard[i][j] == gameboard[i][j-1]
    elif i == n-1 and j == 0:
        return gameboard[i][j] == gameboard[i-1][j] or gameboard[i][j] == gameboard[i][j+1]
    elif i == j == n-1:
        return gameboard[i][j] == gameboard[i-1][j] or gameboard[i][j] == gameboard[i][j-1]
    elif i == 0 and j in range_num:
        return gameboard[i][j] == gameboard[i-1][j] or gameboard[i][j] == gameboard[i][j-1] or gameboard[i][j] == gameboard[i][j+1]
    elif i == n-1 and j in range_num:
        return gameboard[i][j] == gameboard[i-1][j] or gameboard[i][j] == gameboard[i][j-1] or gameboard[i][j] == gameboard[i][j+1]
    elif i in range_num and j == 0:
        return gameboard[i][j] == gameboard[i-1][j] or gameboard[i][j] == gameboard[i+1][j] or gameboard[i][j] == gameboard[i][j+1]
    elif i in range_num and j == n-1:
        return gameboard[i][j] == gameboard[i-1][j] or gameboard[i][j] == gameboard[i+1][j] or gameboard[i][j] == gameboard[i][j-1]
    else:
        return gameboard[i][j] == gameboard[i-1][j] or gameboard[i][j] == gameboard[i+1][j] or gameboard[i][j] == gameboard[i][j-1] or gameboard[i][j] == gameboard[i][j+1]
def check_board(gameboard,n):
    count1 = 0
    count2 = 0
    for i in range(n):
        for j in range(n):
            if check_cell(i,j,gameboard,n) == True:
                count1 += 1
            else:
                count2 += 1
    if count1 > 0:
        return True
    else:
        return False

def max_value(gameboard,n):
    a=gameboard[0][0]
    for i in gameboard:
        for j in i:
            if j >= a:
                a=j
            else:
                a=a
    return a




