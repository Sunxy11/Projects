from bases import *
from possibles import *
from merge import *
import pygame, sys
from pygame.locals import *
pygame.init()
maSurface = pygame.display.set_mode((800, 500))
pygame.display.set_caption('JUST Get Ten ')
def colorboard(gameboard,n):
    for i in range(n):
        for j in range(n):
            b=gameboard[i][j]
            if b==1:
                color=(137,207,240)
            if b==2:
                color=(0,255,0)
            if b==3:
                color=(242,156,177)
            if b==4:
                color=(255,255,0)
            if b==5:
                color=(238,87,0)
            if b==6:
                color=(200,100,100)
            if b==7:
                color=(200,100,50)
            if b==8:
                color=(100,200,200)
            if b==9:
                color=(100,150,150)
            if b==10:
                color=(100,100,100)
            pygame.draw.rect(maSurface,color,(j*100,i*100,100,100))
            black=(0,0,0)
            fontObj = pygame.font.Font ('freesansbold.ttf',50)
            texteSurface = fontObj.render(str(b),True,black,color)
            texteRect = texteSurface.get_rect()
            texteRect.topleft = (30+j*100,30+i*100)
            maSurface.blit(texteSurface,texteRect)
    green1=(51,153,102)
    black=(0,0,0)
    red=(255,0,0)
    lhg=(190,190,190)
    #重玩页面
    fontObj = pygame.font.Font ('freesansbold.ttf',70)
    pygame.draw.rect(maSurface,black,(600,400,200,100))
    #playagain = fontObj.render('playagain',True,green1)
    playagain = fontObj.render('playagain',True,lhg)
    page1= playagain.get_rect()
    page1.topleft = (600,420)
    maSurface.blit(playagain,page1)
    #停止页面
    fontObj = pygame.font.Font ('freesansbold.ttf',40)
    pygame.draw.rect(maSurface,black,(600,320,100,50))
    quit = fontObj.render('Quit',True,green1)
    page4= quit.get_rect()
    page4.topleft = (600,320)
    maSurface.blit(quit,page4)
    #记分页面
    fontObj = pygame.font.Font ('freesansbold.ttf',60)
    getscore = fontObj.render('score',True,red)
    page2= getscore.get_rect()
    page2.topleft = (570,50)
    maSurface.blit(getscore,page2)

def playgame(gameboard):
    colorboard(gameboard,n)
    while True:

        if check_board(gameboard,n) == True and max_value(gameboard,n) != 10:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    poseX, poseY = event.pos
                    j = poseX//100
                    i = poseY//100
                    if 600 <= poseX <= 700 and 320 <= poseY <= 370:
                        pygame.quit()
                        sys.exit()
                    if j == 6 and i==4 or j == 7 and i == 4:
                        gameboard = newboard(n,proba)
                        playgame(gameboard)
                    if check_cell(i,j,gameboard,n) == True:
                        list=[(i,j)]
                        propagation(n, i, j, gameboard)
                        print("\n",end="")
                        gravity(gameboard,n,proba)
                        print("\n",end="")
                        colorboard(gameboard,n)
                        red=(255,0,0)
                        black=(0,0,0)
                        yourscore = max_value(gameboard,n)
                        fontObj = pygame.font.Font ('freesansbold.ttf',60)
                        nowscore = fontObj.render(str(yourscore),True,red,black)
                        page3= nowscore.get_rect()
                        page3.topleft = (630,150)
                        maSurface.blit(nowscore,page3)
            pygame.display.update()
        if max_value(gameboard,n) == 10:
            get = pygame.image.load('get.jpg')
            maSurface.blit(get,(110,100))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    poseX, poseY = event.pos
                    j = poseX//100
                    i = poseY//100
                    if 600 <= poseX <= 700 and 320 <= poseY <= 370:
                        pygame.quit()
                        sys.exit()
                    if j == 6 and i==4 or j == 7 and i == 4:
                        gameboard = newboard(n,proba)
                        playgame(gameboard)
        if check_board(gameboard,n) == False and max_value(gameboard,n) != 10:
            lose= pygame.image.load('lose.jpg')
            maSurface.blit(lose,(120,100))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    poseX, poseY = event.pos
                    j = poseX//100
                    i = poseY//100
                    if 600 <= poseX <= 700 and 320 <= poseY <= 370:
                        pygame.quit()
                        sys.exit()
                    if j == 6 and i==4 or j == 7 and i == 4:
                        gameboard = newboard(n,proba)
                        playgame(gameboard)
pygame.mixer.music.load("Another_Day_Of_Sun.ogg")
pygame.mixer.music.play(-1,0.0)
musicPlaying = True
playgame(gameboard)


