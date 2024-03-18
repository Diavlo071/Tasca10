import pygame
import sys
from pygame.locals import *

white = (255,255,255)
black = (0,0,0)

objs = []

MAIN_BUTTON = 1

class Pane():

    def __init__(self):
        self.Screen = pygame.display.set_mode((1000,600), 0, 32)
        self.font = pygame.font.SysFont('Arial', 25)

    def drawPane(self, textToDisplay):
        self.Screen.blit(self.font.render(textToDisplay, True, (black)), (250, 115))
        pygame.draw.rect(self.Screen, (black), (175, 75, 200, 100), 2)

    def drawPane1(self, textToDisplay):
        self.Screen.blit(self.font.render(textToDisplay, True, (black)), (250, 115))
        pygame.draw.rect(self.Screen, (black), (175, 75, 200, 100), 2)

    def drawPane2(self, textToDisplay):
        self.Screen.blit(self.font.render(textToDisplay, True, (black)), (250, 115))
        pygame.draw.rect(self.Screen, (black), (175, 75, 200, 100), 2)

    def drawPane3(self, textToDisplay):
        self.Screen.blit(self.font.render(textToDisplay, True, (black)), (250, 115))
        pygame.draw.rect(self.Screen, (black), (175, 75, 200, 100), 2)

    def drawPane4(self, textToDisplay):
        self.Screen.blit(self.font.render(textToDisplay, True, (black)), (250, 115))
        pygame.draw.rect(self.Screen, (black), (175, 75, 200, 100), 2)

    def drawPane5(self, textToDisplay):
        self.Screen.blit(self.font.render(textToDisplay, True, (black)), (250, 115))
        pygame.draw.rect(self.Screen, (black), (175, 75, 200, 100), 2)

    def drawPane6(self, textToDisplay):
        self.Screen.blit(self.font.render(textToDisplay, True, (black)), (250, 115))
        pygame.draw.rect(self.Screen, (black), (175, 75, 200, 100), 2)

    def drawPane7(self, textToDisplay):
        self.Screen.blit(self.font.render(textToDisplay, True, (black)), (250, 115))
        pygame.draw.rect(self.Screen, (black), (175, 75, 200, 100), 2)

    def drawPane8(self, textToDisplay):
        self.Screen.blit(self.font.render(textToDisplay, True, (black)), (250, 115))
        pygame.draw.rect(self.Screen, (black), (175, 75, 200, 100), 2)

    def drawPane9(self, textToDisplay):
        self.Screen.blit(self.font.render(textToDisplay, True, (black)), (250, 115))
        pygame.draw.rect(self.Screen, (black), (175, 75, 200, 100), 2)

class Screen():

    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((1000,600), 0, 32)
        self.screen.fill((white))
        pygame.display.update()
        numberOfPanes = 0
        self.NoOfPanes = numberOfPanes

    def addPane(self, textToDisplay):
        myPane = Pane()
        myPane.drawPane(textToDisplay)

    def clearScreen(self):
        self.screen = pygame.display.set_mode((600,400), 0, 32)
        self.screen.fill((white))
        pygame.display.update()

    def mousePosition(self):
        global clickPos
        global releasePos
        for event in pygame.event.get():
            if event.type == MAIN_BUTTON:
                self.Pos = pygame.mouse.get_pos()
                return MAIN_BUTTON
            else:
                return False


if __name__ == '__main__':
    Pan3 = Screen()
    Pan3.addPane("hello")
    Pan3.mousePosition()
    pygame.display.update()
    while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                posx,posy = pygame.mouse.get_pos()
                print(posx)
                print(posy)


        for event in pygame.event.get():        
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();

def addPane(self, textToDisplay):
    myPane = Pane(self.screen) # send screen to Pane
    myPane.drawPane(textToDisplay)

# ...

class Pane():

    def __init__(self, screen):
        self.Screen = screen # get screen 
