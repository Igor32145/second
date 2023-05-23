import pygame
import random

class Dino:
    def __init__(self, image_path1,  image_path2, image_path3, image_path4, height, jump_sound_path, lading_sound_path, crash_sound_path):
        self.image1 = pygame.image.load(image_path1)
        self.image1.set_colorkey(pygame.Color('white'))
        x = self.image1.get_size()[0]
        self.y = height // 2 - self.image1.get_size()[1]
        self.rect = self.image1.get_rect(topleft=(x, self.y))
        self.image2 = pygame.image.load(image_path2)
        self.image2.set_colorkey(pygame.Color('white'))
        x = self.image2.get_size()[0]
        self.y = height // 2 - self.image2.get_size()[1]
        self.rect = self.image2.get_rect(topleft=(x, self.y))
        self.image3 = pygame.image.load(image_path3)
        self.image3.set_colorkey(pygame.Color('white'))
        x = self.image3.get_size()[0]
        self.y = height // 2 - self.image3.get_size()[1]
        self.rect = self.image3.get_rect(topleft=(x, self.y))
        self.image4 = pygame.image.load(image_path4)
        self.image4.set_colorkey(pygame.Color('white'))
        x = self.image4.get_size()[0]
        self.y = height // 2 - self.image4.get_size()[1]
        self.rect = self.image4.get_rect(topleft=(x, self.y))
        self.speed = 0
        self.max_speed = -10
        self.dy = 0
        self.down = False
        self.timer = 0
        self.crash = False
        self.jump_sound = pygame.mixer.Sound(jump_sound_path)
        self.lading_sound = pygame.mixer.Sound(lading_sound_path)
        self.crash_sound = pygame.mixer.Sound(crash_sound_path)
    def sat_down(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN] and not self.dy:
            self.down = True
            self.rect = self.image3.get_rect(bottomleft = self.rect.bottomleft)
        else:
            self.down = False
            self.rect = self.image1.get_rect(bottomleft=self.rect.bottomleft)
    def draw(self, sc):
        if self.timer < 5 or self.dy != 0:
            if self.down:
                sc.blit(self.image3, self.rect)
            else:
                sc.blit(self.image1, self.rect)
        elif self.timer < 10:
            if self.down:
                sc.blit(self.image4, self.rect)
            else:
                sc.blit(self.image2, self.rect)
        else:
            if self.down:
                sc.blit(self.image4, self.rect)
            else:
                sc.blit(self.image2, self.rect)
            self.timer = 0
        self.timer += 1
    def check_jump_possibility(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not self.dy:
            self.jump_sound.play()
            return True
        return False
    def jump(self):
        touch = False
        if self.check_jump_possibility():
            touch = True
            self.dy = 0.35
            self.speed = self.max_speed
        self.rect.y += self.speed
        self.speed += self.dy
        if self.rect.top >= self.y:
            if touch:
                self.lading_sound.play()
                self.touch = False
            self.dy = 0
            self.speed = 0
class Ground:
    def __init__(self, image_path, y, speed):
        self.image = pygame.image.load(image_path)
        self.image.set_colorkey(pygame.Color('white'))
        self.rect = self.image.get_rect(topleft=(0, y))
        self.speed = speed
    def draw(self, sc):
        sc.blit(self.image, self.rect)
    def move(self, width):
        self.rect.x -= self.speed
        if self.rect.right <= width:
            self.rect.x = 0
class Cloud:
    def __init__(self, image_path, x, y, speed):
        self.image = pygame.image.load(image_path)
        self.image.set_colorkey(pygame.Color('white'))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
    def move(self, width, max_height):
        if self.rect.right <= 0:
            self.rect.left = random.randint(width, width + 100)
            self.rect.top = random.randint(30, max_height)
        else:
            self.rect.x -= self.speed
    def draw(self, sc):
        sc.blit(self.image, self.rect)
class Obstacle:
    def __init__(self, speed, image_path, x, dino_bottom, flying):
        self.image = pygame.image.load(image_path)
        self.image.set_colorkey(pygame.Color('white'))
        y = dino_bottom - self.image.get_size()[1] + 40
        if flying:
            y -= 75
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
    def draw(self, sc):
        sc.blit(self.image, self.rect)
    def move(self):
        self.rect.x -= self.speed