from khet_board import *


def fire_laser(pla,flag,_line,_colum,laserposition,l):   #flag是发射激光得那个棋子或着转折点转发激光的那个棋子,后面分别是棋子的行和列,激光方向  l是一个装经过格子的list
    if laserposition == 3:#看激光方向
        a=0
        for i in range(_line,8):
            l[i][_colum] = 1
            a+=1
            if a == 8 - _line and pla[7][_colum]%100 == 0:
                return   pla[i][_colum],i, _colum, laserposition,l
            elif pla[i][_colum]%100 != 0 and i != _line:
                return   pla[i][_colum],i, _colum, laserposition,l
            else:
                continue
    if laserposition == 1:
        a = 0
        for i in range(_line,-1,-1):
            l[i][_colum] = 1
            a += 1
            if a == _line+1 and pla[0][_colum]%100 == 0:
                return   pla[i][_colum], i, _colum, laserposition,l
            elif pla[i][_colum]%100 != 0 and i!=_line:
                return   pla[i][_colum],i, _colum, laserposition,l
            else:
                continue
    if laserposition == 4:
        a = 0
        for i in range(_colum,10):
            a += 1
            l[_line][i] = 1
            if a == 10-_colum and pla[_line][9]%100 == 0:
                return  pla[_line][i],_line, i, laserposition,l
            elif pla[_line][i]%100 != 0 and i != _colum:
                return  pla[_line][i], _line, i, laserposition,l
            else:
                continue
    if laserposition == 2:
        a = 0
        for i in range(_colum,-1,-1):

            l[_line][i] = 1
            a += 1
            if a == _colum+1 and pla[_line][0]%100 == 0:
                return pla[_line][i], _line, i, laserposition,l
            elif pla[_line][i]%100 != 0 and i != _colum:
                return pla[_line][i] , _line, i, laserposition,l #返回被激光射到的棋子的值，棋子的位置，还有激光的方向
            else:
                continue



def judgelaser(pla, flag,_line,_colum,laserposition):#调用这个函数的是上个函数的返回值，判断激光遇上了什么棋子

    laser_col, laser_self, laser_position = information(flag)

    if flag%100 == 0:
        dead_laser = 1
        laserposition = 0
        return _line, _colum, dead_laser ,laserposition
    if laser_self == 1:
        dead_laser=flag
        laserposition = 0
        return _line, _colum, dead_laser ,laserposition
    if laser_self == 2:
        dead_laser = 1
        laserposition = 0
        return _line, _colum, dead_laser,laserposition
    if laser_self == 3:#nnnnnnnnnnnnnnnnnnnnnnnnnnnn
        if laser_position==1 or laser_position==3:
            if laserposition==3:
                laserposition=2
            elif laserposition==2:
                laserposition=3
            elif laserposition==1:
                laserposition=4
            else:#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
                laserposition=1
        if laser_position==2 or laser_position==4:
            if laserposition==3:
                laserposition=4
            elif laserposition==4:
                laserposition=3
            elif laserposition==1:
                laserposition=2
            else:#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
                laserposition=1
        dead_laser = 0
        return _line, _colum, dead_laser,laserposition

    if laser_self == 4:
        if laser_position == 2:
            if laserposition == 4:
                laserposition = 1
                dead_laser = 0
            elif laserposition == 3:
                laserposition = 2
                dead_laser = 0
            else:
                dead_laser=flag
                laserposition = 0

            return _line, _colum, dead_laser,laserposition
        if laser_position == 1:
            if laserposition == 3:
                laserposition = 4
                dead_laser = 0
            elif laserposition == 2:
                laserposition = 1
                dead_laser = 0
            else:
                dead_laser=flag
                laserposition = 0
            return _line, _colum, dead_laser,laserposition
        if laser_position == 4:
            if laserposition == 1:
                laserposition = 4
                dead_laser = 0
            elif laserposition == 2:
                laserposition = 3
                dead_laser = 0
            else:
                dead_laser=flag
                laserposition = 0
            return _line, _colum, dead_laser,laserposition
        if laser_position == 3:
            if laserposition == 1:
                laserposition = 2
                dead_laser = 0
            elif laserposition == 4:
                laserposition = 3
                dead_laser = 0
            else:
                dead_laser=flag
                laserposition = 0
            return _line, _colum, dead_laser,laserposition
    if laser_self == 5:
        if laser_position == 1 and laserposition != 3:
            dead_laser = flag
            laserposition = 0
        elif laser_position == 3 and laserposition != 1:
            dead_laser = flag
            laserposition = 0
        elif laser_position == 4 and laserposition != 2:
            dead_laser = flag
            laserposition = 0
        elif laser_position == 2 and laserposition != 4:
            dead_laser = flag
            laserposition = 0
        else:
            dead_laser = 1
            laserposition =0
        return _line, _colum, dead_laser,laserposition
def px(line,colum):
    x=colum*77+38+80
    y=line*74+37+50
    return x,y

def win_or_lose(dead_laser):
    if (dead_laser - (dead_laser//100)*100)//10 == 1:
        print("Pharl is dead. Game over!")
        return 1
    else:
        print("Game goes on!")
        return 0
