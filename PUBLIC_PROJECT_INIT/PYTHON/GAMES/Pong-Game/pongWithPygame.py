# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:21:41 2021

@author: josce
"""

import pygame
import winsound

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen_size = (800, 600)



def main():
    pygame.init()
    
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("BASIC PONG GAME WITH PYGAME")
    clock = pygame.time.Clock()
    
    #PLAYER A
    coord_x_a = 50
    coord_y_a = 255
    width_a = 15
    height_a = 90
    speed_a = 0
    
    #PLAYER B
    coord_x_b = 740
    coord_y_b = 255
    width_b = 15
    height_b = 90
    speed_b = 0
    
    #BALL
    coord_x_ball = 400
    coord_y_ball = 300
    radius_ball = 10
    speed_x_ball = 3
    speed_y_ball = 3
    
    score_a = 0
    score_b = 0
    game_font = pygame.font.SysFont("Consola", 28)
    
    game_over = False
    while not game_over:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    speed_a = -3
                if event.key == pygame.K_s:
                    speed_a = 3
                if event.key == pygame.K_o:
                    speed_b = -3
                if event.key == pygame.K_l:
                    speed_b = 3
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    speed_a = 0
                if event.key == pygame.K_s:
                    speed_a = 0
                if event.key == pygame.K_o:
                    speed_b = 0
                if event.key == pygame.K_l:
                    speed_b = 0
            
        coord_y_a += speed_a
        coord_y_b += speed_b
        
        # Para que la pelota se mueva
        coord_x_ball += speed_x_ball
        coord_y_ball += speed_y_ball
        
        # Scores en la pantalla
        if coord_x_ball > 790:
            coord_x_ball = 400
            coord_y_ball = 300
            speed_x_ball *= -1
            score_a += 1
            
        if  coord_x_ball < 0:
            coord_x_ball = 400
            coord_y_ball = 300
            speed_x_ball *= -1
            score_b += 1
            
        if coord_y_ball > 590 or coord_y_ball < 0:
            speed_y_ball *= -1
            winsound.PlaySound("plateBreak", winsound.SND_ASYNC)
        
        
        
        screen.fill(BLACK)        
        #-----ZONA DE DIBUJO-----------#
        player1 = pygame.draw.rect(screen, WHITE, [coord_x_a, coord_y_a , width_a, height_a])
        player2 = pygame.draw.rect(screen, WHITE, [coord_x_b, coord_y_b , width_b, height_b])
        ball_game = pygame.draw.circle(screen, WHITE, [coord_x_ball, coord_y_ball], radius_ball)
        
        if ball_game.colliderect(player1) or ball_game.colliderect(player2):
            speed_x_ball *= -1  # Porque las paredes estan en el eje 'x'
            winsound.PlaySound("plateBreak", winsound.SND_ASYNC)
        
        score_text = game_font.render(f"PLAYER 1:  {score_a}", True, WHITE)
        screen.blit(score_text, (5, 3))
        score_text = game_font.render(f"PLAYER 2:  {score_b}", True, WHITE)
        screen.blit(score_text, (665, 3))
        
        clock.tick(60)
        pygame.display.flip()
    
    
if __name__ == "__main__":
    main()

