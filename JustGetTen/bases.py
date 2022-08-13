def newboard(n,proba):
    board = [["." for i in range(n)] for j in range(n)]
    import random
    for i in range(n):
        for j in range(n):
            random_number = random.random()
            if random_number < proba[0]:
                board[i][j] = 4
            elif proba[0] <= random_number < proba[1]:
                board[i][j] = 3
            elif proba[1] <= random_number < proba[2]:
                board[i][j] = 2
            else:
                board[i][j] = 1
    return board
def display(gameboard,n):
    for i in range(n):
        for j in range(n):
            print(gameboard[i][j],end=" ")
        print()
#n=int(input("how many rows and columns do you want to play?"))
#while n <= 1:
    #n=int(input("how many rows and columns do you want to play?"))
n=5
proba=(0.05,0.30,0.6)
gameboard=newboard(n,proba)
display(gameboard,n)
