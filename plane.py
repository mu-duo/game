import random
import bullet


class BasePlane():
    def __init__(self):
        self.path = ''
        self.site = [0, 0]
        self.hp = 100
        self.speed = 20
        self.bullet = bullet.BaseBullet

    def move_left(self):
        self.site[0] = self.site[0] - self.speed

    def move_right(self):
        self.site[0] = self.site[0] + self.speed

    def move_forward(self):
        self.site[1] = self.site[1] - self.speed

    def move_backward(self):
        self.site[1] = self.site[1] + self.speed

    def get_hurt(self, bullet):
        self.hp = self.hp - bullet.attack

    def shoot(self):
        flag = random.randint(0, 200)
        if flag == 0:
            return True
        else:
            return False

    def remove(self):
        pass


class Enemy1(BasePlane):
    def __init__(self):
        BasePlane.__init__(self)
        self.path = 'image/plane/p1.png'
        self.site = [random.randint(1, 340), 0]
        self.bullet = bullet.FastBullet


class Enemy2(BasePlane):
    def __init__(self):
        BasePlane.__init__(self)
        self.path = 'image/plane/p2.png'
        self.site = [random.randint(1, 340), 0]
        self.bullet = bullet.HurtBullet


class Enemy3(BasePlane):
    def __init__(self):
        BasePlane.__init__(self)
        self.path = 'image/plane/p3.png'
        self.site = [random.randint(1, 340), 0]
        self.bullet = bullet.HurtBullet


class Enemy4(BasePlane):
    def __init__(self):
        BasePlane.__init__(self)
        self.path = 'image/plane/p4.png'
        self.site = [random.randint(1, 340), 0]
        self.bullet = bullet.HurtBullet


class Enemy5(BasePlane):
    def __init__(self):
        BasePlane.__init__(self)
        self.path = 'image/plane/p5.png'
        self.site = [random.randint(1, 340), 0]
        self.bullet = bullet.HurtBullet


class Enemy6(BasePlane):
    def __init__(self):
        BasePlane.__init__(self)
        self.path = 'image/plane/p6.png'
        self.site = [random.randint(1, 340), 0]
        self.bullet = bullet.HurtBullet


class Heroplane(BasePlane):
    def __init__(self):
        BasePlane.__init__(self)
        self.path = 'image/plane/heroplane.png'
        self.site = [130,720]
        self.bullet = bullet.HeroBullet
