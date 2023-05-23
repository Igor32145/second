import pygame
import random
import display
import classes
import adit_obstacles
import game_settings

pygame.init()
#Параметры игрового поля и fps
WIDTH, HEIGHT = 1500, 600
start_fps = 60
score2 = 0
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
OBSTACLES_SPEED = 8
COUNT_OBSTACLES = 11
fps = start_fps
current_obstacles = []
score = 0
display.background_music('music/фон.mp3')
dino = classes.Dino('images/dino/dino_1.png', 'images/dino/dino_2.png', 'images/dino/dino_3.png', 'images/dino/dino_4.png', HEIGHT, 'music/прыжок.ogg', 'music/подение.ogg', 'music/проигрыш.ogg')
ground = classes.Ground('images/world/ground.png', dino.rect.y + dino.rect.size[0] - 20, 0)
clouds = display.create_cloud(7, WIDTH, 200, 'images/world/cloud.png',  0)
obstacles = adit_obstacles.create_obstacles(COUNT_OBSTACLES, 'images/enemies/cactus_', 0, WIDTH + 20, dino.rect.bottom)
while True:
    # Выход по нажатию крестика
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if game_settings.check_start(ground.speed):
        dino.crash = True
        score = 0
        fps = start_fps
        current_obstacles = []
        ground.speed = OBSTACLES_SPEED
        for obstacle in obstacles:
            obstacle.speed = OBSTACLES_SPEED
        for cloud in clouds:
            cloud.speed = OBSTACLES_SPEED
    display.draw_world(sc, ground, clouds, score, WIDTH)
    dino.draw(sc)
    dino.jump()
    dino.sat_down()
    ground.move(WIDTH)
    for obstacle in current_obstacles:
        obstacle.draw(sc)
        obstacle.move()
    for cloud in clouds:
        cloud.move(WIDTH, 200)
    if game_settings.check_game_over(dino, current_obstacles):
        ground.speed = 0
        for obstacle in obstacles:
            obstacle.speed = 0
        for cloud in clouds:
            cloud.speed = 0
        font = pygame.font.SysFont(None, 100)
        text = font.render('Game Over', True, pygame.Color('grey'))
        sc.blit(text, (WIDTH / 2 - 230, HEIGHT / 4))
    score = game_settings.increase_score(score, fps, ground.speed
                                             )
    current_obstacles = adit_obstacles.check_new_obstacles(current_obstacles, obstacles, WIDTH)
    current_obstacles = adit_obstacles.delete_first_obstacle(current_obstacles)
    pygame.display.flip()
    clock.tick(fps + score // 10)