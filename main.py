import time
import pygame
from pygame.locals import *
import plane
import random


from config import *

def key_in(plane,bullet_set):
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                bullet_set.append(plane.bullet(site=[plane.site[0]+40,plane.site[1]-50]))
            elif event.key == K_a:
                plane.move_left()
            elif event.key == K_d:
                plane.move_right()
            elif event.key == K_w:
                plane.move_forward()
            elif event.key == K_s:
                plane.move_backward()

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    bg1 = pygame.image.load('image/backgrund/backgrund.png')
    bg2 = pygame.image.load('image/backgrund/backgrund.png')

    p = plane.Heroplane()
    screen.blit(pygame.image.load(p.path),p.site)

    plane_set = []
    bullet_set = []

    # fps = 1/time_sleep
    time.sleep(0.05)

    x = 0
    while True:

        screen.blit(bg1, (0, x))
        screen.blit(bg2, (0, x - 800))
        screen.blit(pygame.image.load(p.path), p.site)

        # 20 fps
        #time.sleep(0.01)
        x = x + 1
        if x >= 800:
            x = 0

        key_in(p,bullet_set)

        '''
        产生敌机
        '''
        if random.randint(1,10)==5 and len(plane_set)<5:
            plane_set.append(plane.Enemy5())


        '''
        敌机是否射击
        '''
        if len(plane_set) > 0:
            for i in range(len(plane_set) - 1):
                screen.blit(pygame.image.load(plane_set[i].path), plane_set[i].site)
                # shoot
                if plane_set[i].shoot():
                    bullet_set.append(plane_set[i].bullet(site=[plane_set[i].site[0] + 20, plane_set[i].site[1]]))

        '''
        子弹移动
        '''
        if len(bullet_set) > 0:
            for i in range(len(bullet_set) - 1):
                bullet_set[i].move()
                screen.blit(pygame.image.load(bullet_set[i].path), bullet_set[i].site)

        '''
        子弹删除
        '''
        if len(bullet_set) > 0:
            flag = []
            for i in range(len(bullet_set) - 1):
                if bullet_set[i].remove():
                    flag.append(bullet_set[i])
            for i in flag:
                bullet_set.remove(i)

        '''
        是否击中飞机
        '''



        pygame.display.update()

if __name__ == '__main__':
    main()
