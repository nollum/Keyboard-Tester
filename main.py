#!/bin/usr/python3

import pygame
import sys

def main():
    pygame.init()

    screen = pygame.display.set_mode((935, 400))
    icon = pygame.image.load('./images/kticon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Keyboard Tester')

    import application

    app = application.Application()

    while True:
        app.listen()
        app.draw(screen)
        app.update(screen)

if __name__ == '__main__':
    main()
