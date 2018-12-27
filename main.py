import sys
import pygame

pygame.init()
pygame.font.init()

size = width, height = 250, 300
speed = [1, 0]
black = 255, 255, 255

screen = pygame.display.set_mode(size)

ball = pygame.image.load("d:/code_repository/game/butten.png")
bound = pygame.image.load("d:/code_repository/game/bound.png")
ballrect = ball.get_rect()
f = pygame.font.SysFont('arial', 20, True)
f1 = f.render('1', True, (0, 0, 0))
f2 = f.render('2', True, (0, 0, 0))
f3 = f.render('3', True, (0, 0, 0))
f4 = f.render('4', True, (0, 0, 0))
f5 = f.render('5', True, (0, 0, 0))
f6 = f.render('6', True, (0, 0, 0))
f7 = f.render('7', True, (0, 0, 0))
f8 = f.render('8', True, (0, 0, 0))
num = {1: f1, 2: f2, 3: f3, 4: f4, 5: f5, 6: f6, 7: f7, 8: f8}


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            (b1, b2, b3) = pygame.mouse.get_pressed()
            if b1:
                x = mouse_x // 25
                y = mouse_y // 25 - 2
                if y < 0:
                    continue
                else:
                    

    screen.fill(black)
    for j in range(10):
        for i in range(10):
            screen.blit(ball, (25 * i, 25 * j + 50))
    #        screen.blit(bound, (25 * i, 25 * j))
    # screen.blit(f1, (25 * i + 8, 125))
    pygame.display.flip()
