import sys, pygame

class player:
    def __init__(self, image, size, speed):
        self.pos = image.get_rect().move(0, size['height'])
        self.size_mod = 1
        self.size = size
        self.speed = speed
        self.image = image
        self.health = 100
    
    def move(self, res):
        self.pos = self.pos.move(self.speed['x'], (self.speed['y'] + 10))
        
        if self.pos.bottom > res[1]:
            self.pos.bottom = res[1]
            # print("top over")
        
        if self.pos.bottom < 0:
            self.pos.top = 0
            # print("bottom under")
        
        if self.pos.left < 0:
            self.pos.left = 0
            # print("left under")
        
        if self.pos.right > res[0]:
            self.pos.right = res[0]
            # print("right over")

    def change_speed(self, delta):
        #apply gravity
        self.speed['x'] += delta[0]
        self.speed['y'] = delta[1] - self.speed['y']