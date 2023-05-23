import classes
import random
def create_obstacles(count, file_path, speed, x, dino_bottom):
    obstacles = []
    for i in range(1, count):
        obstacle = classes.Obstacle(speed, f'{file_path}{i}.png', x, dino_bottom, i == count - 1)
        obstacles.append(obstacle)
    return obstacles
def check_new_obstacles(current_obstacles, obstacles, WIDTH):
    if current_obstacles:
        current_obstacles = add_obstacles_to_not_empty_list(current_obstacles, obstacles, WIDTH)
    else:
        current_obstacles = add_obstacles_to_empty_list(obstacles, WIDTH)
    return current_obstacles
def add_obstacles_to_empty_list(obstacles, WIDTH):
    new_obstacle = random.choice(obstacles)
    new_obstacle.rect.left = random.randint(WIDTH, WIDTH + 10)
    return [new_obstacle]
def add_obstacles_to_not_empty_list(current_obstacles, obstacles, WIDTH):
    last_obstacle = current_obstacles[-1]
    if WIDTH - last_obstacle.rect.right > 300:
        new_obstacle = random.choice(obstacles)
        while new_obstacle in current_obstacles:
            new_obstacle = random.choice(obstacles)
        new_obstacle.rect.left = random.randint(WIDTH, WIDTH + 100)
        current_obstacles.append(new_obstacle)
    return current_obstacles
def delete_first_obstacle(obstacles):
    if obstacles:
        first_obstacle = obstacles[0]
        if first_obstacle.rect.right < 0:
            obstacles.pop(0)
    return obstacles