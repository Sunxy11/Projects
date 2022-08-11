from khet_board import *


def ori_judge_move(ori_r, ori_c, pla):#判断最初选择的位置是否有棋子,所选棋子是不是狮身人面像（斯芬克斯）  三种模式通用
    while pla[ori_r - 1][ori_c - 1] == 400 or pla[ori_r - 1][ori_c - 1] == 200 or pla[ori_r - 1][ori_c - 1] == 100 or pla[ori_r - 1][ori_c - 1] == 123 or pla[ori_r - 1][ori_c - 1] == 221:
        print("Select again!")
        ori_r = int(input("Which row?"))
        ori_c = int(input("Which column?"))
    return ori_r, ori_c


def ori_judge_rotate(ori_r, ori_c, pla, ori_p, res):#旋转 三种模式通用
    while pla[ori_r - 1][ori_c - 1] == 400 or pla[ori_r - 1][ori_c - 1] == 200 or pla[ori_r - 1][ori_c - 1] == 100:
        print("Select again!")
        ori_r = int(input("Which row?"))
        ori_c = int(input("Which column?"))
    if pla[ori_r - 1][ori_c - 1] == 123:
        while (ori_p == 3 and res == "clockwise") or (ori_p == 4 and res == "anticlockwise"):
            print("Select again!")
            res = input("Clockwise or Anticlockwise?")
    if pla[ori_r - 1][ori_c - 1] == 221:
        while (ori_p == 1 and res == "clockwise") or (ori_p == 2 and res == "anticlockwise"):
            print("Select again!")
            res = input("Clockwise or Anticlockwise?")
    return ori_r, ori_c, res


def move(fin_r, fin_c, ori_r, ori_c, pla, ori_pla, ori_co, s):#判断棋子要移动的位置是否符合规则  和原来棋盘一样的数组，但没变过；棋子的颜色；棋子的类型
    (fin_col, fin_self, fin_position) = information(pla[fin_r - 1][fin_c - 1])
    if s != 3:
        while abs(fin_r - ori_r) > 1 or abs(fin_c - ori_c) > 1 or fin_self != 0:
            if ori_co == 1 and pla[fin_r - 1][fin_c - 1] == 100:
                break
            if ori_co == 2 and pla[fin_r - 1][fin_c - 1] == 200:
                break
            print("Select again!")
            fin_r = int(input("Which row to go?"))
            fin_c = int(input("Which column to go?"))
            (fin_col, fin_self, fin_position) = information(pla[fin_r - 1][fin_c - 1])
    if s == 3:
        while abs(fin_r - ori_r) > 1 or abs(fin_c - ori_c) > 1 or fin_self != 4 or fin_self !=5:
            print("Select again!")
            fin_r = int(input("Which row to go?"))
            fin_c = int(input("Which column to go?"))
            (fin_col, fin_self, fin_position) = information(pla[fin_r - 1][fin_c - 1])
    a = pla[fin_r - 1][fin_c - 1]
    pla[fin_r - 1][fin_c - 1] = pla[ori_r - 1][ori_c - 1]
    pla[ori_r - 1][ori_c - 1] = a
    if (ori_pla[ori_r - 1][ori_c - 1] == 100 and a == 400) or (ori_pla[ori_r - 1][ori_c - 1] == 100 and a == 200):
        pla[ori_r - 1][ori_c - 1] = 100
    if (ori_pla[ori_r - 1][ori_c - 1] == 200 and a == 400) or (ori_pla[ori_r - 1][ori_c - 1] == 200 and a == 100):
        pla[ori_r - 1][ori_c - 1] = 200
    if a == 100 or a == 200:
        pla[ori_r - 1][ori_c - 1] = 400
    return fin_r, fin_c


def rotate(ori_p, pla, ori_r, ori_c, res):   #顺、逆时针方向转动
    fin_p = ori_p
    if res == "clockwise":
        if ori_p == 1:
            pla[ori_r - 1][ori_c - 1] += 3
            fin_p += 3
        else:
            pla[ori_r - 1][ori_c - 1] -= 1
            fin_p -= 1
    if res == "anticlockwise":
        if ori_p == 4:
            pla[ori_r - 1][ori_c - 1] -= 3
            fin_p -= 3
        else:
             pla[ori_r - 1][ori_c - 1] += 1
             fin_p += 1
    return fin_p
