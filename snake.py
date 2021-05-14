from tkinter import messagebox
import tkinter as tk
import math
import random
import pygame

class cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

class snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass

def drawGrid(w, rows, surface):
    pass

def redrawWindow(surface):
    pass

def randomSnack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    # It should be the same so that we have the same no. of boxes
    window = pygame.display.set_mode((500, 500))
    rows = 20 # divisible by 500, thus makes 25x25 grid
    s = snake((255, 0, 0), (10, 10))

    clock = pygame.time.Clock()
    while True:
        pygame.time.delay(50) # milliseconds
        clock.tick(10) # This makes it so that the snake doesnt zoom around the board
        redrawWindow(surface=window)


rows = None
w = None
h = None
cube.rows = rows
cube.w = w

main()

