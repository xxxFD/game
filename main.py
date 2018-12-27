import sys
import pygame
import mine


def game_init():
    screen.fill(black)
    for j in range(10):
        for i in range(10):
            screen.blit(ball, (25 * i, 25 * j + 50))
        pygame.display.flip()


pygame.init()
pygame.font.init()
(state, num_list, expose) = mine.mine_init()
mine_num = 10
accumulate = 0
over = 0

size = width, height = 250, 300
black = 255, 255, 255

screen = pygame.display.set_mode(size)

ball = pygame.image.load("butten.png")
bound = pygame.image.load("bound.png")
flag = pygame.image.load("flag.png")
boom = pygame.image.load("mine.png")
again = pygame.image.load("again.png")
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

game_init()

while 1:
    if over == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (mouse_x, mouse_y) = pygame.mouse.get_pos()
                (b1, b2, b3) = pygame.mouse.get_pressed()
                x = mouse_x // 25
                y = mouse_y // 25 - 2
            elif event.type == pygame.MOUSEBUTTONUP:
                if b1 and b3:
                    continue
                elif b1:
                    if y < 0:
                        continue
                    else:
                        if state[x][y] == 1:
                            over = 1
                            for i in range(10):
                                for j in range(10):
                                    if state[i][j] == 1:
                                        screen.blit(boom, (25 * i, 25 * j + 50))
                            screen.blit(again, (75, 0))
                            pygame.display.flip()
                            break
                        else:
                            if expose[x][y] == 0:
                                if num_list[x][y] != 0:
                                    screen.blit(bound, (25 * x, 25 * y + 50))
                                    screen.blit(num[num_list[x][y]], (25 * x + 8, 25 * y + 50))
                                if num_list[x][y] == 0:
                                    screen.blit(bound, (25 * x, 25 * y + 50))
                                expose[x][y] = 1
                                accumulate += 1
                                if accumulate == 90:
                                    over = 1
                                    screen.blit(again, (75, 0))
                                pygame.display.flip()
                elif b3:
                    if y < 0:
                        continue
                    elif expose[x][y] == 1:
                        continue
                    else:
                        screen.blit(flag, (25 * x, 25 * y + 50))
                        pygame.display.flip()
    elif over == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (mouse_x, mouse_y) = pygame.mouse.get_pos()
                (b1, b2, b3) = pygame.mouse.get_pressed()
                x = mouse_x // 25
                y = mouse_y // 25 - 2
            elif event.type == pygame.MOUSEBUTTONUP:
                if y < 0:
                    over = 0
                    (state, num_list, expose) = mine.mine_init()
                    game_init()
                    accumulate = 0
                else:
                    continue




    # screen.blit(f1, (25 * i + 8, 125))
