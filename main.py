__author__ = 'black_000'
import copy
import sys
import os
import pygame
from pygame.locals import *

#Ask for file input
#Background, TitleBarBG, ButtonList, Graph
#TODO: IMPLEMENT ARROWS
#TODO: Basic Typing
#TODO: Drag and Drop
#TODO: Box Select
#TODO: Basic Selection
#TODO:

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
DARKRED = [175, 0, 0]
RED = [127, 0, 0]
MEDRED = [150, 0, 0]

DEFAULTBG = BLACK
DEFAULT = WHITE


#does everything for now
def main():
    global fileBackup
    #This looks to see if
    cntr = 0
    while True:
        if os.path.exists('temp'+str(cntr)+'.txt'):
            cntr += 1
            #TODO: ask to save things here
        else:
            break
    fileBackup = open('temp'+str(cntr)+'.txt', 'r+')

    fileName = input('Input save file name')
    if len(fileName) == 0:
        fileName = 'Default.txt'
    else:
        fileName += '.txt'

    fileSave = open(fileName, 'r+')
    theGraph = Graph(fileName)
    for line in fileSave:
        theGraph.Add(Block(line))

    fileSave.close()

    while True:
        #Interact
        #Update
        theGraph.Draw()


class Block():
    #Draw, DragandDrop, Update, Interact
    def __init__(self, aLine):
        self.title = ''
        self.text = ''
        self.pos = []                   # [x, y]
        self.size = []                  # [width, height]
        self.colorBG = DEFAULTBG        # Default Black
        self.colorText = DEFAULT        # Default Black
        self.colorBorder = self.colorText
        self.arrows = []
        #TODO: Arrows: Figure out Implementation
        self.Setup(aLine)

    def Setup(self, aLine):
        temp = ''
        value = None
        pos = False
        size = False
        # TODO: Make sure this works correctly
        #TITLE  |  BODY TEXT  |Posx,Posy|Sizex,Sizey
        for i in range(len(aLine)):
            if aLine[i] == ',':
                if pos:
                    self.pos.append(copy.deepcopy(value))
                elif size:
                    self.size.append(copy.deepcopy(value))
            elif aLine[i] == '|':
                if self.title != '':
                    self.title = temp
                elif self.text != '':
                    self.text = temp
                    pos = True
                else:
                    size = True
                    pos = False
                    value = None
            else:
                if pos or size:
                    if value is None:
                        value = int(aLine[i])
                    else:
                        value = value*10 + int(aLine[i])
                else:
                    temp += aLine[i]
            #TODO: Arrows: Setup Implementation for reading arrows

    def Draw(self):
        #TODO: OutlineRect, BGRect, Title, Text
        pass

    def PrintToFile(self, aFile):
        print(self.title, end='|', file=aFile)
        print(self.text, end='|', file=aFile)
        print(str(self.pos[0]+','+str(self.pos[1]), end='|', file=aFile))
        print(str(self.size[0]+','+str(self.size[1]), file=aFile))
        #TODO: Arrows: PRINT TO FILE?


class Graph():
    def __init__(self, fileName):
        self.blockList = []
        self.colorBG = DEFAULTBG        # Default Black
        self.colorArrows = DEFAULT      # Default White
        self.colorDefault = DEFAULT     # Default White
        self.windowPos = [0, 0]
        self.zoom = 1.0
        self.fileSaveName = fileName

    def Add(self, aBlock):
        self.blockList.append(aBlock)

    def Draw(self):
        for i in range(len(self.blockList)):
            self.blockList.Draw()

    def PrintToFile(self, aFile):
        for i in range(len(self.blockList)):
            self.blockList[i].PrintToFile(aFile)
            #TODO: Arrows: Print to SaveFile


def Terminate():
    pygame.quit()
    fileBackup.close()
    sys.exit()

if __file__ == 'main':
    main()
