from config import *


class BaseBullet():
    def __init__(self, attack=5, speed=2, site=[0, 0]):
        self.attack = attack
        self.speed = speed
        self.site = site
        self.path = 'image/bullet/basebullet.png'

    def __del__(self):
        print('bullet has been deleted')

    def move_left(self):
        self.site[1] = self.site[1] - self.speed / 2

    def move_right(self):
        self.site[1] = self.site[1] + self.speed / 2

    def move_forward(self):
        self.site[0] = self.site[0] + self.speed

    def move_backward(self):
        self.site[0] = self.site[0] - self.speed

    def move(self):
        self.site[1] = self.site[1] + self.speed

    def remove(self):
        if self.site[1] > SCREEN_SIZE[1] + 100 or self.site[1] < 0:
            return True
        else:
            return False

class HeroBullet(BaseBullet):
    def __init__(self, attack=50, speed=10, site=[0, 0]):
        BaseBullet.__init__(self, attack=attack, speed=speed, site=site)
        self.path = 'image/bullet/herobullet.png'

    def __del__(self):
        print('Herobullet has been deleted')

    def move(self):
        self.site[1] = self.site[1] - self.speed


class FastBullet(BaseBullet):
    def __init__(self, attack=5, speed=20, site=[0, 0]):
        BaseBullet.__init__(self, attack=attack, speed=speed, site=site)
        self.path = 'image/bullet/fastbullet.png'


class HurtBullet(BaseBullet):
    def __init__(self, attack=10, speed=2, site=[0, 0]):
        BaseBullet.__init__(self, attack=attack, speed=speed, site=site)
        self.path = 'image/bullet/hurtbullet.png'


class ShotBullet(BaseBullet):
    def __init__(self):
        BaseBullet.__init__()
        self.path = []
        self.flag = True

    def shot(self):
        pass
