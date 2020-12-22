#My version of Pong Game

import pygame, sys
from pygame.locals import *

class Game():
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Calibri', 72, bold=True)
    clock = pygame.time.Clock()

    WINDOWSIZE = (800,640)
    screen = pygame.display.set_mode(WINDOWSIZE)

    #PLAYER
    player = pygame.Surface((14, 80))
    player.fill((255,255,255))
    player_position = [760, 310]
    player_rect = pygame.Rect(player_position[0], player_position[1], player.get_width(), player.get_height())


    #ENEMY
    enemy = pygame.Surface((14, 80))
    enemy.fill((255,255,255))
    enemy_position = [26, 310]
 

    #BALL
    ball = pygame.Surface((14, 14))
    ball.fill((255,255,255))
    ball_position = [400, 320]


    #Moviment 
    moving_up = False
    moving_down = False
    velocity = 7
    ball_direction_lr = None
    ball_direction_ud = None

    #Counter
    player_points = 0
    enemy_points = 0
    


    while True:
        screen.fill((0,0,0))
        screen.blit(player, player_position)
        screen.blit(enemy, enemy_position)
        screen.blit(ball, ball_position)
        score_player = font.render(str(player_points), False, (255,255,255)) 
        score_enemy = font.render(str(enemy_points), False, (255,255,255)) 
        screen.blit(score_player, (446,90))
        screen.blit(score_enemy, (308,90))


        player_rect = pygame.Rect(player_position[0], player_position[1], player.get_width(), player.get_height())
        enemy_rect = pygame.Rect(enemy_position[0], enemy_position[1], enemy.get_width(), enemy.get_height())
        ball_rect = pygame.Rect(ball_position[0], ball_position[1], ball.get_width(), ball.get_height())

        for i in range(16):
            pygame.draw.rect(screen, (255,255,255), (386, i+5+40*i, 10,10))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    moving_up = True
                if event.key == K_DOWN:
                    moving_down = True
            if event.type == KEYUP:
                if event.key == K_UP:
                    moving_up = False
                if event.key == K_DOWN:
                    moving_down = False
        
        if moving_up:
            if player_position[1] > 0:
                player_position[1] -= velocity
        if moving_down:
            if player_position[1] < 560:
                player_position[1] += velocity

        if ball_direction_lr == 'left':
            ball_position[0] -= velocity-2
        else:
            ball_position[0] += velocity-2
        
        if ball_direction_ud == 'up':
            ball_position[1] -= velocity-2
        if ball_direction_ud == 'down':
            ball_position[1] += velocity-2

        middle_enemy = enemy_position[1] + 25         
        if (enemy_position[1] != ball_position[1]) and ball_position[0] < 400:
            if middle_enemy > ball_position[1]:
                if enemy_position[1] > 0:
                    enemy_position[1] -= velocity-2
            if middle_enemy < ball_position[1]:
                if enemy_position[1] < 561:
                    enemy_position[1] += velocity-2
        if ball_rect.colliderect(player_rect):
            ball_direction_lr = 'left'
            if moving_up:
                ball_direction_ud = 'up'
            if moving_down:
                ball_direction_ud = 'down'
                
        if ball_rect.colliderect(enemy_rect):
            ball_direction_lr = 'right'
            if moving_up:
                ball_direction_ud = 'up'
            if moving_down:
                ball_direction_ud = 'down'

        if ball_position[1] < 0:
            ball_direction_ud = 'down'
        if ball_position[1] > 640:
            ball_direction_ud = 'up'
        if ball_position[0] > 800:
            ball_position = [400, 320]
            player_position[1] = 300
            enemy_position[1] = player_position[1]
            enemy_points += 1
            ball_direction_ud = None
            pygame.time.wait(1000)

        if ball_position[0] < 0:
            ball_position = [400, 320]
            player_position[1] = 300
            enemy_position[1] = player_position[1]
            player_points += 1
            ball_direction_ud = None
            pygame.time.wait(1000)
       
        pygame.display.update()
        clock.tick(60)

Game()