from khet_move import *
from khet_board import *
from khet_path import *



import pygame, sys
from pygame.locals import *
pygame.init()
maSurface = pygame.display.set_mode((960, 646))
pygame.display.set_caption('KHET ')
FPS = 300
fpsClock = pygame.time.Clock()


m_p0=pygame.image.load("BOARD SETUP.jpg")
m_p1=pygame.image.load("CLASSIC.png")
m_p2=pygame.image.load("DYNASTY.png")
m_p3=pygame.image.load("IMHOTEP.png")
m_p4=pygame.image.load("Background.jpg")

m_p5=pygame.image.load("PHA-RED-SOU.png")
m_p6=pygame.image.load("PHA-SILVER-NOR.png")

m_p30=pygame.image.load("PHA-RED-NOR.png")
m_p31=pygame.image.load("PHA-RED-E.png")
m_p32=pygame.image.load("PHA-RED-W.png")
m_p33=pygame.image.load("PHA-SILVER-SOU.png")
m_p34=pygame.image.load("PHA-SILVER-W.png")
m_p35=pygame.image.load("PHA-SILVER-E.png")

m_p7=pygame.image.load("SPH-RED-SOU.png")
m_p8=pygame.image.load("SPH-SILVER-NOR.png")

m_p36=pygame.image.load("SPH-RED-E.png")
m_p37=pygame.image.load("SPH-SILVER-W.png")


m_p9=pygame.image.load("ANU-RED-SOU.png")
m_p10=pygame.image.load("ANU-SILVER-NOR.png")

m_p38=pygame.image.load("ANU-RED-NOR.png")
m_p39=pygame.image.load("ANU-RED-W.png")
m_p40=pygame.image.load("ANU-RED-E.png")
m_p41=pygame.image.load("ANU-SILVER-SOU.png")
m_p42=pygame.image.load("ANU-SILVER-W.png")
m_p43=pygame.image.load("ANU-SILVER-E.png")

m_p11=pygame.image.load("SCA-RED-WN.png")
m_p12=pygame.image.load("SCA-RED-EN.png")
m_p13=pygame.image.load("SCA-RED-WS.png")
m_p14=pygame.image.load("SCA-RED-ES.png")
m_p15=pygame.image.load("SCA-SILVER-WN.png")
m_p16=pygame.image.load("SCA-SILVER-EN.png")
m_p17=pygame.image.load("SCA-SILVER-WS.png")
m_p18=pygame.image.load("SCA-SILVER-ES.png")

m_p19=pygame.image.load("PYR-RED-WN.png")
m_p20=pygame.image.load("PYR-RED-EN.png")
m_p21=pygame.image.load("PYR-RED-WS.png")
m_p22=pygame.image.load("PYR-RED-ES.png")
m_p23=pygame.image.load("PYR-SILVER-WN.png")
m_p24=pygame.image.load("PYR-SILVER-EN.png")
m_p25=pygame.image.load("PYR-SILVER-WS.png")
m_p26=pygame.image.load("PYR-SILVER-ES.png")

m_p27=pygame.image.load("HOME.png")
m_p28=pygame.image.load("FIRE.png")
m_p29=pygame.image.load("TURN.png")
m_p30=pygame.image.load("light.png")

m_p31=pygame.image.load("HONGWIN.png")
m_p32=pygame.image.load("HUIWIN.png")

def show_home_interface():
    maSurface.blit(m_p0,(0,0))
    maSurface.blit(m_p1,(256,130))#左上角坐标，像素是448*109
    maSurface.blit(m_p2,(256,250))#左上角坐标，像素是448*109
    maSurface.blit(m_p3,(256,375))#左上角坐标，像素是448*109
    pygame.display.flip()

black=(0,0,0)

#数组变为图片
def image_board():
    pygame.draw.rect(maSurface,black,(0,0,960,646))
    #展示棋盘背景图
    maSurface.blit(m_p4,(80,50))
    pygame.display.flip()
    #home键  像素75*84
    maSurface.blit(m_p27,(870,50))
    pygame.display.flip()
    #发射激光键  像素81*53
    maSurface.blit(m_p28,(865,580))
    pygame.display.flip()
    for i in range(8):
        for j in range(10):
            if plateau[i][j]==113:#红法老朝南
                maSurface.blit(m_p5,(80+77*j,27+73*i))
            elif plateau[i][j]==211:#灰法老朝北
                maSurface.blit(m_p6,(80+77*j,27+73*i))
            elif plateau[i][j]==123:#红SPH朝南
                maSurface.blit(m_p7,(80+77*j,27+73*i))
            elif plateau[i][j]==221:#灰SPH朝北
                maSurface.blit(m_p8,(80+77*j,27+73*i))
            elif plateau[i][j]==153:#红AUN南
                maSurface.blit(m_p9,(80+77*j,27+73*i))
            elif plateau[i][j]==251:#灰AUN北
                maSurface.blit(m_p10,(80+77*j,27+73*i))
            elif plateau[i][j]==132:#红SCA西北
                maSurface.blit(m_p11,(80+77*j,27+73*i))
            elif plateau[i][j]==131:#红SCA东北
                maSurface.blit(m_p12,(80+77*j,27+73*i))
            elif plateau[i][j]==133:#红SCA西南
                maSurface.blit(m_p13,(80+77*j,27+73*i))
            elif plateau[i][j]==134:#红SCA东南
                maSurface.blit(m_p14,(80+77*j,27+73*i))
            elif plateau[i][j]==232:#灰SCA西北
                maSurface.blit(m_p15,(80+77*j,27+73*i))
            elif plateau[i][j]==231:#灰SCA东北
                maSurface.blit(m_p16,(80+77*j,27+73*i))
            elif plateau[i][j]==233:#灰SCA西南
                maSurface.blit(m_p17,(80+77*j,27+73*i))
            elif plateau[i][j]==234:#灰SCA东南
                maSurface.blit(m_p18,(80+77*j,27+73*i))
            elif plateau[i][j]==142:#红PYR西北
                maSurface.blit(m_p19,(80+77*j,27+73*i))
            elif plateau[i][j]==141:#红PYR东北
                maSurface.blit(m_p20,(80+77*j,27+73*i))
            elif plateau[i][j]==143:#红PYR西南
                maSurface.blit(m_p21,(80+77*j,27+73*i))
            elif plateau[i][j]==144:#红PYR东南
                maSurface.blit(m_p22,(80+77*j,27+73*i))
            elif plateau[i][j]==242:#灰PYR西北
                maSurface.blit(m_p23,(80+77*j,27+73*i))
            elif plateau[i][j]==241:#灰PYR东北
                maSurface.blit(m_p24,(80+77*j,27+73*i))
            elif plateau[i][j]==243:#灰PYR西南
                maSurface.blit(m_p25,(80+77*j,27+73*i))
            elif plateau[i][j]==244:#灰PYR东南
                maSurface.blit(m_p26,(80+77*j,27+73*i))
            elif plateau[i][j]==111:#红法老北
                maSurface.blit(m_p30,(80+77*j,27+73*i))
            elif plateau[i][j]==114:#红法老东
                maSurface.blit(m_p31,(80+77*j,27+73*i))
            elif plateau[i][j]==112:#红法老西
                maSurface.blit(m_p32,(80+77*j,27+73*i))
            elif plateau[i][j]==213:#灰法老南
                maSurface.blit(m_p33,(80+77*j,27+73*i))
            elif plateau[i][j]==212:#灰法老西
                maSurface.blit(m_p34,(80+77*j,27+73*i))
            elif plateau[i][j]==214:#灰法老东
                maSurface.blit(m_p35,(80+77*j,27+73*i))
            elif plateau[i][j]==124:#红SPH东
                maSurface.blit(m_p36,(80+77*j,27+73*i))
            elif plateau[i][j]==222:#灰SPH西
                maSurface.blit(m_p37,(80+77*j,27+73*i))
            elif plateau[i][j]==151:#红ANU北
                maSurface.blit(m_p38,(80+77*j,27+73*i))
            elif plateau[i][j]==152:#红ANU西
                maSurface.blit(m_p39,(80+77*j,27+73*i))
            elif plateau[i][j]==154:#红ANU东
                maSurface.blit(m_p40,(80+77*j,27+73*i))
            elif plateau[i][j]==253:#灰ANU南
                maSurface.blit(m_p41,(80+77*j,27+73*i))
            elif plateau[i][j]==252:#灰ANU西
                maSurface.blit(m_p42,(80+77*j,27+73*i))
            elif plateau[i][j]==254:#灰ANU东
                maSurface.blit(m_p43,(80+77*j,27+73*i))
            pygame.display.flip()

def fireLaser(_flag, _line_, _colum_, laserposition_,l,x1,y1):
    pygame.mixer.music.load("laser.ogg")
    pygame.mixer.music.play(1,2.0)
    musicPlaying = True
    x2,y2=px(_line_, _colum_)
    if x1==x2:
        if laserposition_ == 1:
            for a in range (y1,y2,-1):
                fond = pygame.image.load("light.png")
                maSurface.blit(fond,(x1,a))
                pygame.display.update()
                fpsClock.tick(FPS)

            if _line_==0 and _flag%100==0:
                for i in range(y2,y2-37,-1):
                    fond = pygame.image.load("light.png")
                    maSurface.blit(fond,(x1,i))
                    pygame.display.update()
                    fpsClock.tick(FPS)
        if laserposition_ == 3:
            for a in range (y1,y2):
                fond = pygame.image.load("light.png")
                maSurface.blit(fond,(x1,a))
                pygame.display.update()
                fpsClock.tick(FPS)
            if _line_==7 and _flag%100==0:
                for i in range(y2,y2+37):
                    fond = pygame.image.load("light.png")
                    maSurface.blit(fond,(x1,i))
                    pygame.display.update()
                    fpsClock.tick(FPS)
    if y1==y2:
        if laserposition_ == 4:
            for a in range (x1,x2):
                fond = pygame.image.load("light.png")
                maSurface.blit(fond,(a,y1))
                pygame.display.update()
                fpsClock.tick(FPS)
            if _flag%100==0 and _colum_==9:
                for i in range(x2,x2+38):
                    fond = pygame.image.load("light.png")
                    maSurface.blit(fond,(y1,i))
                    pygame.display.update()
                    fpsClock.tick(FPS)
        if laserposition_ == 2:
            for a in range (x1,x2,-1):
                fond = pygame.image.load("light.png")
                maSurface.blit(fond,(a,y1))
                pygame.display.update()
                fpsClock.tick(FPS)
            if _flag%100==0 and _colum_==0:
                for i in range(x2,x2-38,-1):
                    fond = pygame.image.load("light.png")
                    maSurface.blit(fond,(y1,i))
                    pygame.display.update()
                    fpsClock.tick(FPS)
    line, colum, dead_laser,laserposition=judgelaser(plateau, _flag,_line_,_colum_,laserposition_)
    while(dead_laser == 0 and laserposition != 0):
        _flag, _line_, _colum_, laserposition_,l=fire_laser(plateau,flag,line,colum,laserposition,l)
        x1_,y1_=px(line,colum)
        x2_,y2_=px(_line_, _colum_)
        if x1_==x2_:
            if laserposition_ == 1:
                for a in range (y1_,y2_,-1):
                    fond = pygame.image.load("light.png")
                    maSurface.blit(fond,(x1_,a))
                    pygame.display.update()
                    fpsClock.tick(FPS)
                if _line_==0 and _flag%100==0:
                    for i in range(y2_,y2_-37,-1):
                        fond = pygame.image.load("light.png")
                        maSurface.blit(fond,(x1_,i))
                        pygame.display.update()
                        fpsClock.tick(FPS)
            if laserposition_ == 3:
                for a in range (y1_,y2_):
                    fond = pygame.image.load("light.png")
                    maSurface.blit(fond,(x1_,a))
                    pygame.display.update()
                    fpsClock.tick(FPS)
                if _line_==7 and _flag%100==0:
                    for i in range(y2_,y2_+37):
                        fond = pygame.image.load("light.png")
                        maSurface.blit(fond,(x1_,i))
                        pygame.display.update()
                        fpsClock.tick(FPS)
        if y1_==y2_:
            if laserposition_ == 4:
                for a in range (x1_,x2_):
                    fond = pygame.image.load("light.png")
                    maSurface.blit(fond,(a,y1_))
                    pygame.display.update()
                    fpsClock.tick(FPS)
                if _flag%100==0 and _colum_==9:
                    for i in range(x2_,x2_+38):
                        fond = pygame.image.load("light.png")
                        maSurface.blit(fond,(y1_,i))
                        pygame.display.update()
                        fpsClock.tick(FPS)
            if laserposition_ == 2:
                for a in range (x1_,x2_,-1):
                    fond = pygame.image.load("light.png")
                    maSurface.blit(fond,(a,y1_))
                    pygame.display.update()
                    fpsClock.tick(FPS)
                if _flag%100==0 and _colum_==0:
                    for i in range(x2_,x2_-38,-1):
                        fond = pygame.image.load("light.png")
                        maSurface.blit(fond,(y1_,i))
                        pygame.display.update()
                        fpsClock.tick(FPS)
        line, colum, dead_laser,laserposition=judgelaser(plateau, _flag,_line_,_colum_,laserposition_)

    return line,colum,dead_laser

def playGame(page,flag,tag,laser,count,first,first_col,second_col):
    while True:
        if page==1:
            flag=0
            tag=0
            laser=0
            count=0
            first=0
            first_col=0
            second_col=0
            show_home_interface()
            #显示对应类型的棋盘或退出
            for row in range(8):
                for clo in range(10):
                    plateau[row][clo]=400
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONUP:
                    poseX, poseY = event.pos
                    #classic模式
                    if 256 <= poseX <= 704 and 130 <= poseY <= 239:
                        mode_classic(plateau)
                    #dynasty模式
                    elif 256 <= poseX <= 704 and 250 <= poseY <= 359:
                        mode_dynasty(plateau)
                    #imhptep模式
                    elif 256 <= poseX <= 704 and 375 <= poseY <= 484:
                        mode_imhptep(plateau)
                    display(plateau)
                    image_board()
                    page=2
        #若没选要旋转的棋子
        elif page==2 and flag==0 and laser==0:
            for event in pygame.event.get():
                #退出
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                #旋转
                elif event.type == MOUSEBUTTONDOWN:
                    poseX, poseY = event.pos
                    j = (poseX-80)//77
                    i = (poseY-27)//73
                    down_i=i
                    down_j=j

                    #棋盘内 像素769*596
                    if 80 <= poseX <= 849 and 27 <= poseY <= 623:
                        if tag==0 and flag==0:
                            (ori_col, ori_self, ori_position) = information(plateau[i][j])
                            print(ori_col, ori_self, ori_position)
                            #若不是空且不是禁地
                            if ori_col != 4 and ori_self != 0:
                                #确定红方先还是灰方先
                                if first==0:
                                    first_col=ori_col
                                    if first_col==1:
                                        second_col=2
                                    elif first_col==2:
                                        second_col=1
                                    first=1
                                if count%2==0 and ori_col==first_col or count%2==1 and ori_col==second_col:
                                    #旋转方向图片  像素80*40
                                    image_board()
                                    maSurface.blit(m_p29,(100+77*j,10+73*i))
                                    pygame.display.flip()

                elif event.type == MOUSEBUTTONUP:
                    poseX, poseY = event.pos
                    j = (poseX-80)//77
                    i = (poseY-27)//73
                    #在棋盘内部
                    # 点击home按钮
                    if 870 <= poseX <= 945 and 50 <= poseY <= 134:
                        page = 1
                    if 80 <= poseX <= 849 and  50 <= poseY <= 646:
                        (ori_col, ori_self, ori_position) = information(plateau[down_i][down_j])
                        (col, self, position) = information(plateau[i][j])
                        #选的棋子是有效棋子
                        if ori_self != 0:
                            if down_i==i and down_j==j:
                                flag=1
                            elif count%2==0 and first_col==1 and ori_col== 1 or count%2==1 and first_col==2 and ori_col== 1 or count%2==0 and first_col==2 and ori_col== 2 or count%2==1 and first_col==1 and ori_col== 2:#选的是该出棋的一方
                                #如果不是斯芬克斯（它不能移动）
                                if self != 2:
                                    #选紧邻的地方
                                    if i==down_i and j==down_j+1 or i==down_i and j==down_j-1 or i==down_i+1 and j==down_j or i==down_i-1 and j==down_j:
                                        #如果是普通的地方、红方或灰方地盘
                                        if (col, self, position)==(4,0,0) or (col, self, position)==(1,0,0) and ori_col==2 or (col, self, position)==(2,0,0) and ori_col==1:
                                            plateau[down_i][down_j]=400
                                            plateau[i][j]=ori_col*100+ori_self*10+ori_position
                                            image_board()
                                            laser=1


        #若已选要旋转的棋子
        elif page==2 and flag==1 and laser==0:
            #选旋转方向
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONUP:
                    poseX, poseY = event.pos
                    #点击home按钮
                    if 870 <= poseX <= 945 and 50 <= poseY <= 134:
                        page=1
                    #若选逆时针旋转
                    if 100+77*j <= poseX <= 140+77*j and 10+73*i <= poseY <= 50+73*i:
                        if (ori_col, ori_self, ori_position) != (1,2,4) or (ori_col, ori_self, ori_position) != (2,2,2):
                            tag=1
                            if ori_position==1 or ori_position==2 or ori_position==3:
                                ori_position+=1
                            elif ori_position==4:
                                ori_position=1
                            plateau[i][j]=ori_col*100+ori_self*10+ori_position
                            image_board()
                            tag=0
                            flag=0
                            laser=1
                    #若选顺时针旋转：
                    elif 140+77*j <= poseX <= 180+77*j and 10+73*i <= poseY <= 50+73*i:
                        if (ori_col, ori_self, ori_position) != (1,2,3) or (ori_col, ori_self, ori_position) != (2,2,1):
                            tag=1
                            if ori_position==4 or ori_position==3 or ori_position==2:
                                ori_position-=1
                            elif ori_position==1:
                                ori_position=4
                            plateau[i][j]=ori_col*100+ori_self*10+ori_position
                            image_board()
                            tag=0
                            flag=0
                            laser=1
                    else:
                        image_board()
                        flag=0
        #发射激光
        elif page==2 and laser==1:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONUP:
                    poseX, poseY = event.pos
                    #点击home按钮
                    if 870 <= poseX <= 945 and 50 <= poseY <= 134:
                        page=1
                    #点击发射激光按钮
                    elif 865 <= poseX <= 946 and 580 <= poseY <= 633:
                        l = [[0]*10 for a in range(8)]
                        if count%2==0 and first_col==1 or count%2==1 and first_col==2:#红
                            _flag, _line_, _colum_, laserposition_,l=fire_laser(plateau,123,0,0,3,l)
                            x1,y1=px(0,0)
                        elif count%2==0 and first_col==2 or count%2==1 and first_col==1:#灰
                            _flag, _line_, _colum_, laserposition_,l=fire_laser(plateau,221,7,9,1,l)
                            x1,y1=px(7,9)
                        #发射激光
                        (line1,colum1,dead_laser1)=fireLaser(_flag, _line_, _colum_, laserposition_,l,x1,y1)
                        #没有棋子死
                        if dead_laser1 == 1:
                            image_board()
                        #有棋子死
                        else:
                            #死的是法老
                            if (dead_laser1 - (dead_laser1//100)*100)//10 == 1:
                                #输的是红方
                                if dead_laser1//100==1:
                                    maSurface.blit(m_p32,(300,150))
                                    pygame.display.flip()
                                elif dead_laser1//100==2:
                                    maSurface.blit(m_p31,(300,150))
                                    pygame.display.flip()
                                page=3
                            else:
                                #死的位置在红方领地
                                if  line1 >= 1 and line1 <= 7 and colum1 == 0 or line1 == 0 and colum1 == 8 or line1 == 7 and colum1 == 8:
                                    plateau[line1][colum1] == 100
                                    image_board()
                                #死的位置在灰方领地
                                elif line1 >= 0 and line1 <= 6 and colum1 == 9 or line1 == 0 and colum1 == 1 or line1 == 7 and colum1 == 1:
                                    plateau[line1][colum1] == 200
                                    image_board()
                                else:
                                    plateau[line1][colum1] == 400
                                    image_board()
                        laser=0
                        flag=0
                        count+=1
        elif page == 3:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONUP:
                    poseX, poseY = event.pos
                    if 870 <= poseX <= 945 and 50 <= poseY <= 134:
                        page=1

green1=(51,153,102)
silver=(190,190,190)
red=(255,0,0)

page=1
flag=0#指示是否已选要旋转的图
tag=0#指示是否已选要旋转的方向
laser=0
count=0#红灰双方交换
first=0#是否已确定第一个动的旗子
first_col=0#第一个旋转或移动的旗子是哪方
second_col=0
'''pygame.mixer.music.load("laser.ogg")
pygame.mixer.music.play(1,2.0)
musicPlaying = True'''
playGame(page,flag,tag,laser,count,first,first_col,second_col)


