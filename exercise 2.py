# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 19:28:55 2017

@author: MSI
"""

import pygame

pygame.init()

size = width, height = 1366, 768
speed = [1,1]
black = 255, 255, 255

screen = pygame.display.set_mode(size)

ball = pygame.image.load('C:/Users/MSI/Desktop/无标题.png')#将名字用QQ截图后保存成图片 替代原程序中的球
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
#借鉴http://www.cnblogs.com/hongten/p/hongten_pygame_bouncing_ball.html
