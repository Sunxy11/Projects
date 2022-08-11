from khet_move import *
from khet_path import *
f = 0

while True:
    ori_plateau = plateau
    ori_row = int(input("Which row?"))#选择要移动的棋子
    ori_column = int(input("Which column?"))
    (ori_col, ori_self, ori_position) = information(plateau[ori_row - 1][ori_column - 1])
    f += 1
    while (ori_col == 1 and f % 2 == 0 and ori_self > 0 and ori_position > 0) or (ori_col == 2 and f % 2 != 0 and ori_self > 0 and ori_position > 0):
        print("Select again!")
        ori_row = int(input("Which row?"))
        ori_column = int(input("Which column?"))
        (ori_col, ori_self, ori_position) = information(plateau[ori_row - 1][ori_column - 1])
    if plateau[ori_row - 1][ori_column - 1] == 123 or plateau[ori_row - 1][ori_column - 1] == 221:
        select = input("Rotating or shooting?")
        if select == "shoot":
            l = [[0]*10 for a in range(8)]
            dead_laser, l = deadlaser(plateau, plateau[ori_row - 1][ori_column - 1], ori_row - 1, ori_column - 1, ori_position,l)
            print(dead_laser)#1是被墙壁或棋子吸收了没有死旗，0是光纤被反射了没有死旗，
            if win_or_lose(dead_laser) == 1:
                break
            display(l)
        if select == "rotate":
            reselect = input("Clockwise or Anticlockwise?")
            (ori_row, ori_column, reselect) = ori_judge_rotate(ori_row, ori_column, plateau, ori_position, reselect)
            rotate(ori_position, plateau, ori_row, ori_column, reselect)
            display(plateau)
    else:
        select = input("Rotating or Moving?")
        if select == "move":
            (ori_row, ori_column) = ori_judge_move(ori_row, ori_column, plateau)
            fin_row = int(input("Which row to go?"))#选择棋子要移动的位置
            fin_column = int(input("Which column to go?"))
            move(fin_row, fin_column, ori_row, ori_column, plateau, ori_plateau, ori_col, ori_self)
            display(plateau)
        if select == "rotating":
            reselect = input("Clockwise or Anticlockwise?")
            (ori_row, ori_column) = ori_judge_rotate(ori_row, ori_column, plateau, ori_position, reselect)
            rotate(ori_position, plateau, ori_row, ori_column, reselect)
            display(plateau)
