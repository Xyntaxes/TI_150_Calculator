import pygame,sys
from pygame.locals import *
running = True
width = 360
height = 600
FPS = 60
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 12)
font1 = pygame.font.Font('freesansbold.ttf', 50)
buttonFont = pygame.font.Font('freesansbold.ttf', 30)
dispText = 0
beforeDot = 0
m = False
currentDisp = []
add = False
mult = False
subtract = False
dividing = False
mod = False
lastDisp = 0
dot = False
i = 0
j = 0
#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
BLUE = (135, 206, 250)
GREY = (150, 150,150)
beforeDecimal = 0

#initialize pygame and create window

pygame.mixer.init()
SCREEN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Calculator")
clock = pygame.time.Clock()
logo = font.render('ManavInstruments', True, RED)


num1 = buttonFont.render('1', True, BLACK) 
num11 = num1.get_rect()
num11.center = (60,440)

num2 = buttonFont.render('2', True, BLACK) 
num22 = num1.get_rect()
num22.center = (140,440)

num3 = buttonFont.render('3', True, BLACK) 
num33 = num1.get_rect()
num33.center = (220,440)

num4 = buttonFont.render('4', True, BLACK) 
num44 = num1.get_rect()
num44.center = (60,360)

num5 = buttonFont.render('5', True, BLACK) 
num55 = num1.get_rect()
num55.center = (140,360)

num6 = buttonFont.render('6', True, BLACK) 
num66 = num1.get_rect()
num66.center = (220,360)

num7 = buttonFont.render('7', True, BLACK) 
num77 = num1.get_rect()
num77.center = (60,280)

num8 = buttonFont.render('8', True, BLACK) 
num88 = num1.get_rect()
num88.center = (140,280)

num9 = buttonFont.render('9', True, BLACK) 
num99 = num1.get_rect()
num99.center = (220,280)

num0 = buttonFont.render('0', True, BLACK) 
num00 = num1.get_rect()
num00.center = (75,520)

num = buttonFont.render('.', True, BLACK) 
numnum = num1.get_rect()
numnum.center = (175,510)

ENTER = buttonFont.render('=', True, BLACK) 
ENTER1 = num1.get_rect()
ENTER1.center = (270,515)

plus = buttonFont.render('+', True, WHITE) 
plusBut = num1.get_rect()
plusBut.center = (300,440)

minus = buttonFont.render('_', True, WHITE) 
minusBut = num1.get_rect()
minusBut.center = (300,345)

divide = buttonFont.render('÷', True, WHITE) 
divideBut = num1.get_rect()
divideBut.center = (300,200)

multiply = buttonFont.render('×', True, WHITE) 
multiplyBut = num1.get_rect()
multiplyBut.center = (300,280)

modulo = buttonFont.render('%', True, WHITE) 
modBut = num1.get_rect()
modBut.center = (220,200)

CE = buttonFont.render('CE', True, WHITE) 
CEBut = num1.get_rect()
CEBut.center = (130,200)

C = buttonFont.render('C', True, WHITE) 
CBut = num1.get_rect()
CBut.center = (60,200)




logoRect = logo.get_rect() 
logoRect.center = (74, 143)
while running:
    clock.tick(FPS)
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, GREY,[10,150,width - 20,height - 160])
    pygame.draw.rect(SCREEN, GREY,[10,10,width - 20,130], 1)
    pygame.draw.rect(SCREEN, BLUE,[25,160,70,70])
    pygame.draw.rect(SCREEN, BLUE,[105,160,70,70])
    pygame.draw.rect(SCREEN, BLUE,[185,160,70,70])
    pygame.draw.rect(SCREEN, BLUE,[265,160,70,70])
    pygame.draw.rect(SCREEN, BLUE,[265,240,70,70])
    pygame.draw.rect(SCREEN, BLUE,[265,320,70,70])
    pygame.draw.rect(SCREEN, BLUE,[265,400,70,70])
    pygame.draw.rect(SCREEN, ORANGE,[215,480,120,70])
    pygame.draw.rect(SCREEN, WHITE,[185,400,70,70])
    pygame.draw.rect(SCREEN, WHITE,[185,320,70,70])
    pygame.draw.rect(SCREEN, WHITE,[185,240,70,70])
    pygame.draw.rect(SCREEN, WHITE,[25,400,70,70])
    pygame.draw.rect(SCREEN, WHITE,[25,320,70,70])
    pygame.draw.rect(SCREEN, WHITE,[25,240,70,70])
    pygame.draw.rect(SCREEN, WHITE,[105,400,70,70])
    pygame.draw.rect(SCREEN, WHITE,[105,320,70,70])
    pygame.draw.rect(SCREEN, WHITE,[105,240,70,70])
    pygame.draw.rect(SCREEN, WHITE,[25,480,100,70])
    pygame.draw.rect(SCREEN, WHITE,[135,480,70,70]) ##Buttons
    
    display = font1.render(str(dispText), True, ORANGE)
    displayRect = display.get_rect()
    displayRect.midright = (width - 15,40)
    
    SCREEN.blit(display, displayRect)
    SCREEN.blit(logo, logoRect)
    SCREEN.blit(num1, num11)
    SCREEN.blit(num2, num22)
    SCREEN.blit(num3, num33)
    SCREEN.blit(num4, num44)
    SCREEN.blit(num5, num55)
    SCREEN.blit(num6, num66)
    SCREEN.blit(num7, num77)
    SCREEN.blit(num8, num88)
    SCREEN.blit(num9, num99)
    SCREEN.blit(num0, num00)
    SCREEN.blit(num, numnum)
    SCREEN.blit(ENTER, ENTER1)
    SCREEN.blit(plus, plusBut)
    SCREEN.blit(minus, minusBut)
    SCREEN.blit(divide, divideBut)
    SCREEN.blit(multiply, multiplyBut)
    SCREEN.blit(modulo, modBut)
    SCREEN.blit(C, CBut)
    SCREEN.blit(CE, CEBut)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.K_p:
             dispText = 111
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx > 25 and mx < 95 and my > 160 and my < 230:
                dispText = 0
                currentDisp = []
                i = 0
                beforeDecimal = 0
                lastDisp = 0
                beforeDot = 0
                dot = False
                m = False
            print(mx, my)
            if mx > 25 and mx < 95 and my > 320 and my < 390:
                currentDisp.append(4)
            if mx > 25 and mx < 95 and my > 400 and my < 470:
                currentDisp.append(1)
            if mx > 25 and mx < 95 and my > 240 and my < 310:
                currentDisp.append(7)
            if mx > 105 and mx < 175 and my > 240 and my < 310:
                currentDisp.append(8)
            if mx > 105 and mx < 175 and my > 320 and my < 390:
                currentDisp.append(5)
            if mx > 105 and mx < 175 and my > 400 and my < 470:
                currentDisp.append(2)
            if mx > 185 and mx < 255 and my > 240 and my < 310:
                currentDisp.append(9)
            if mx > 185 and mx < 255 and my > 320 and my < 390:
                currentDisp.append(6)
            if mx > 185 and mx < 255 and my > 400 and my < 470:
                currentDisp.append(3)
            if mx > 25 and mx < 125 and my > 480 and my < 550:
                currentDisp.append(0)
            if mx > 135 and mx < 205 and my > 480 and my < 550:
                dot = True
                beforeDecimal = len(currentDisp)
                beforeDot = dispText
                
            if mx > 265 and mx < 335 and my > 400 and my < 470:
                add = True
                lastDisp = dispText
                dispText = 0
                currentDisp = []
                i = 0
                beforeDecimal = 0
                beforeDot = 0
                dot = False
                m = False
            if mx > 185 and mx < 255 and my > 160 and my < 230:
                mod = True
                lastDisp = dispText
                dispText = 0
                currentDisp = []
                i = 0
                beforeDecimal = 0
                beforeDot = 0
                dot = False
                m = False
            if mx > 105 and mx < 175 and my > 160 and my < 230:
                dispText = 0
                currentDisp = []
                i = 0
                beforeDecimal = 0
                beforeDot = 0
                dot = False
                m = False
            if mx > 265 and mx < 335 and my > 240 and my < 310:
                mult = True
                lastDisp = dispText
                dispText = 0
                currentDisp = []
                i = 0
                beforeDecimal = 0
                beforeDot = 0
                dot = False
                m = False
            if mx > 265 and mx < 335 and my > 320 and my < 390:
                subtract = True
                lastDisp = dispText
                dispText = 0
                currentDisp = []
                i = 0
                beforeDecimal = 0
                beforeDot = 0
                dot = False
                m = False
            if mx > 265 and mx < 335 and my > 160 and my < 230:
                dividing = True
                lastDisp = dispText
                dispText = 0
                currentDisp = []
                i = 0
                beforeDecimal = 0
                beforeDot = 0
                dot = False
                m = False
            if mx > 215 and mx < 335 and my > 480 and my < 550:
                if add == True:  
                    currentDisp = []
                    currentDisp.append(dispText + lastDisp)
                if dividing:
                    currentDisp = []
                    if dispText != 0:
                        currentDisp.append(lastDisp/dispText)
                    else:
                        dispText = "DIV 0 ERROR"
                if mult:
                    currentDisp = []
                    currentDisp.append(lastDisp * dispText)
                if subtract:
                    currentDisp = []
                    currentDisp.append(lastDisp - dispText)
                if mod:
                    currentDisp = []
                    currentDisp.append(lastDisp % dispText)
                add = False
                dividing = False
                mult = False
                subtract = False
                mod = False
            i = 0
            dispText = 0
            if dot == False:
                j = len(currentDisp) - 1
            if dot:
                j = 1
            while i < len(currentDisp)and dot == False:
                dispText += currentDisp[i] * (10**j)
                j -= 1
                i += 1
            if len(str(dispText)) > 10:
                   currentDisp.remove(currentDisp[0])
            while i < len(currentDisp) - beforeDecimal and dot == True and len(currentDisp) >  (beforeDecimal) :
                if m == False:
                    j = 1
                m = True
                dispText += (beforeDot) + (currentDisp[i + beforeDecimal] * (10**(-j)))
                if i > 0:
                    dispText -= beforeDot
                    dispText = round(dispText,j)
                j += 1
                i += 1
                
                
    pygame.display.flip()
