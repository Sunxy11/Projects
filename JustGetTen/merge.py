from bases import *
from possibles import *

def propagation(n, i, j, board) :
    a=n*n
    list=[(i,j)]
    b=board[i][j]
    board[i][j]=0
    while a>0 :
        for m in range(n) :
            for k in range(n):
                if m==0 and k==0 and board[m][k]==b:
                    if board[m+1][k]==0 or board[m][k+1]==0:
                        board[m][k]=0
                        list.append((m,k))
                elif m==0 and k==n-1 and board[m][k]==b:
                    if board[m+1][k]==0 or board[m][k-1] ==0 :
                        board[m][k]=0
                        list.append((m,k))
                elif m==n-1 and k==0 and board[m][k]==b:
                    if board[m-1][k]==0 or board[m][k+1]==0:
                        board[m][k]=0
                        list.append((m,k))
                elif m==n-1 and k==n-1 and board[m][k]==b:
                    if board[m][k-1]==0 or board[m-1][k]==0:
                        board[m][k]=0
                        list.append((m,k))
                elif m>0 and m<n-1 and k==0 and board[m][k]==b:
                    if board[m-1][k]==0 or board[m+1][k]==0 or board[m][k+1]==0 :
                        board[m][k]=0
                        list.append((m,k))
                elif  m>0 and m<n-1 and k==n-1 and board[m][k]==b:
                    if board[m][k-1]==0 or board[m-1][k]==0 or board[m+1][k]==0:
                        board[m][k]=0
                        list.append((m,k))
                elif m==0 and k>0 and k<n-1 and board[m][k]==b:
                    if board[m][k-1]==0 or board[m][k+1]==0 or board[m+1][k]==0:
                        board[m][k]=0
                        list.append((m,k))
                elif m==n-1 and k>0 and k<n-1 and board[m][k]==b:
                    if board[m][k-1]==0 or board[m][k+1]==0 or board[m-1][k]==0:
                        board[m][k]=0
                        list.append((m,k))
                elif m>0 and m<n-1 and k>0 and k<n-1 and board[m][k]==b:
                    if board[m][k+1]==0 or board[m][k-1]==0 or board[m-1][k]==0 or board[m+1][k]==0:
                        board[m][k]=0
                        list.append((m,k))
        a-=1
    new_list = []
    for things in list:
        if things not in new_list:
            new_list.append(things)
    board[i][j]=b+1
    print(new_list)

def gravity(gameboard,n,proba):
    import random
    a=n-1
    while a>0:
        for m in range(n-1):
            for k in range(n):
                if gameboard[m][k]!=0 and gameboard[m+1][k]==0:
                    gameboard[m+1][k]=gameboard[m][k]
                    gameboard[m][k]=0
        a-=1
    for i in range(n):
        for j in range(n):
            if gameboard[i][j] == 0:
                random_number = random.random()
                if random_number < proba[0]:
                    gameboard[i][j] = 4
                elif proba[0] <= random_number < proba[1]:
                    gameboard[i][j] = 3
                elif proba[1] <= random_number < proba[2]:
                    gameboard[i][j] = 2
                else:
                    gameboard[i][j] = 1
    display(gameboard,n)



#while check_board(gameboard,n) == True:
    #i=int(input("which row do you want to choose?"))-1
    #j=int(input("which column do you want to choose?"))-1
    #while i < 0 or j < 0 or i > n-1 or j > n-1 or check_cell(i,j,gameboard,n) == False:
        #i=int(input("which row do you want to choose?"))-1
        #j=int(input("which column do you want to choose?"))-1
    #propagation(n, i, j, gameboard)
    #display(gameboard,n)
    #print("\n",end="")
    #gravity(gameboard,n,proba)

