__author__ = 'black_000'
import copy
import sys
import os
import pygame
from pygame.locals import *

#Ask for file input
#Background, TitleBarBG, ButtonList, Graph

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
DARKRED = [175, 0, 0]
RED = [127, 0, 0]
MEDRED = [150, 0, 0]

DEFAULTBG = BLACK
DEFAULT = WHITE


#does everything for now
def main():
    fileName = input('Input save file name')
    if len(fileName) == 0:
        fileName = 'Default.txt'
    else:
        fileName += '.txt'

    fileSave = open(fileName, 'r+')

    theGraph = Graph()
    for line in fileSave:
        theGraph.Add(Block(line))


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
        self.Setup(aLine)

    def Setup(self, aLine):
        temp = ''
        value = None
        pos = False
        size = False
        # TODO: Make sure this works correctly, and a print to the file upon exits
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


class Graph():
    def __init__(self):
        self.blockList = []
        self.colorBG = DEFAULTBG        # Default Black
        self.colorArrows = DEFAULT      # Default White
        self.colorDefault = DEFAULT     # Default White
        self.windowPos = [0, 0]
        self.zoom = 1.0

    def Add(self, aBlock):
        self.blockList.append(aBlock)


if __file__ == 'main':
    main()
