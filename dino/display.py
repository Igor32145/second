import pygame
import random
import classes
def draw_score(sc, score, width):
    score = int(score)
    zero_count = 5 - len(str(score))
    zeros = '0' * zero_count
    score = f'{zeros}{score}'

    font = pygame.font.SysFont(None, 30)
    text = font.render(str(int(score)), True, pygame.Color('Grey'))
    sc.blit(text, (width - 70, 20))
def draw_world(sc, ground, clouds, scrole, width):
    sc.fill(pygame.Color('white'))
    ground.draw(sc)
    draw_clouds(clouds, sc)
    draw_score(sc, scrole, width)
def create_cloud(cloud_count, width, max_height, image_path, speed):
    clouds = []
    for _ in range(cloud_count):
        x = random.randint(width, width * 2)
        y = random.randint(0, max_height - 200)
        clouds.append(classes.Cloud(image_path, x, y, speed))

    return clouds
def draw_clouds(clouds, sc):
    for i in clouds:
        i.draw(sc)
def background_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)