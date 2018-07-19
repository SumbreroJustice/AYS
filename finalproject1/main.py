import pygame
from button import button
import random
from time import sleep 
pygame.mixer.init()
length, width = (600,600)
screen = (length, width)
pygame.display.init()
Display = pygame.display.set_mode(screen)
pygame.display.flip()
White = (255, 255, 255)
background = pygame.Surface(screen)
button = button(200,200)


def mouseclickcheck():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            rect = pygame.Rect((event.pos), (20,20))
            col = rect.colliderect(button.click_box)
            return col

def printslow(str):
    for letter in str:
        print(letter)
        sleep(.5)

def AYSGLOBAL(mouseclick):
    if mouseclick:
        x = random.randrange(0,4)
        if x == 1:
            AYSONE()
        if x == 2:
            AYSTWO()
        if x == 3:
            AYSTHREE()
def AYSONE():
    print('Are You Sure About That')
def AYSTWO():
    printslow('Are You Sure About That')
def AYSTHREE():
    pygame.mixer.music.load('AYSJC.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    
while True:

    background.fill(White)
    button.render(background)
    AYSGLOBAL(mouseclickcheck())
    pygame.display.update()
    Display.blit(background,(0,0))
