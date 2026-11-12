import pygame
import json

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Session 10 - State Machine Animation")
clock = pygame.time.Clock()

sprite_sheet = pygame.image.load("spritesheet.png").convert_alpha()

with open("sprites.json", "r") as file:
    data = json.load(file)

frames = data["frames"]

sprites = {}

for name, info in frames.items():
    rect = pygame.Rect(info["x"], info["y"], info["w"], info["h"])
    sprites[name] = sprite_sheet.subsurface(rect).copy()


animations = {
    "Idle": [sprites["idle_1"], sprites["idle_2"]],
    "Run": [sprites["run_1"], sprites["run_2"]],
    "Jump": [sprites["jump_1"]],
    "Attack": [sprites["attack_1"]]
}


ANIMATION_FPS = 5
frame_duration = 1 / ANIMATION_FPS

current_frame = 0
last_frame_time = 0
previous_state = "Idle"


player_x = 250
player_y = 250
player_speed = 5

current_state = "Idle"
is_moving = False
is_jumping = False
is_attacking = False

jump_start_time = 0
attack_start_time = 0

JUMP_DURATION = 700
ATTACK_DURATION = 500


running = True

while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                jump_start_time = current_time

            if event.key == pygame.K_f and not is_attacking:
                is_attacking = True
                attack_start_time = current_time

    keys = pygame.key.get_pressed()
    is_moving = False

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        is_moving = True

    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        is_moving = True

    player_x = max(0, min(player_x, 600 - 64))

    if is_jumping and current_time - jump_start_time >= JUMP_DURATION:
        is_jumping = False

    if is_attacking and current_time - attack_start_time >= ATTACK_DURATION:
        is_attacking = False

    if is_attacking:
        current_state = "Attack"
    elif is_jumping:
        current_state = "Jump"
    elif is_moving:
        current_state = "Run"
    else:
        current_state = "Idle"

    current_animation = animations[current_state]

    if current_state != previous_state:
        current_frame = 0
        last_frame_time = current_time
        previous_state = current_state

    if current_time - last_frame_time >= frame_duration * 1000:
        current_frame = (current_frame + 1) % len(current_animation)
        last_frame_time = current_time

    screen.fill((40, 40, 40))
    screen.blit(current_animation[current_frame], (player_x, player_y))

    font = pygame.font.Font(None, 30)
    text = font.render("State: " + current_state, True, (255, 255, 255))
    screen.blit(text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
