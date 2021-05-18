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
    sizeBtwn = w // rows
    x, y = 0, 0
    for i in range(rows):
        x += sizeBtwn
        y += sizeBtwn
    
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))
        

def redrawWindow(surface):
    global width, rows
    width = 200
    rows = 50
    fill((0, 0, 0))
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    # It should be the same so that we have the same no. of boxes
    window = pygame.display.set_mode((500, 500))
    rows = 20  # divisible by 500, thus makes 25x25 grid
    s = snake((255, 0, 0), (10, 10))

    clock = pygame.time.Clock()
    while True:
        pygame.time.delay(50)  # milliseconds
        # This makes it so that the snake doesnt zoom around the board
        clock.tick(10)
        redrawWindow(surface=window)


rows = None
w = None
h = None
cube.rows = rows
cube.w = w

main()
