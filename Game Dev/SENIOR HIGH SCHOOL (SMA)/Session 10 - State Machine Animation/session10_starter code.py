import pygame
import json

# 1. Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Session 10 - State Machine Animation")
clock = pygame.time.Clock()

# 2. Load the sprite sheet
sprite_sheet = pygame.image.load("spritesheet.png").convert_alpha()

# 3. Read the JSON file
with open("sprites.json", "r") as file:
    data = json.load(file)

# 4. Get frame information
frames = data["frames"]

# 5. Extract sprites
sprites = {}

for name, info in frames.items():

    # TODO 1: Create a rectangle using the JSON frame information
    rect = pygame.Rect(
        # Hint: info["x"], info["y"], info["w"], info["h"]
    )

    # TODO 2: Extract the selected frame
    # Hint: sprite_sheet.subsurface(rect).copy()
    sprites[name] =


# 6. Create animation groups
animations = {
    "Idle": [
        # TODO 3: Add Idle frames from the sprites dictionary
    ],
    "Run": [
        # TODO 4: Add Run frames from the sprites dictionary
    ],
    "Jump": [
        # TODO 5: Add Jump frames from the sprites dictionary
    ],
    "Attack": [
        # TODO 6: Add Attack frames from the sprites dictionary
    ]
}


# 7. Animation settings
ANIMATION_FPS = 5

# TODO 7: Calculate frame duration
# Formula: Frame Duration = 1 / FPS
frame_duration =

current_frame = 0
last_frame_time = 0
previous_state = "Idle"


# 8. Player settings
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


# 9. Main game loop
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

    # 10. Get player input
    keys = pygame.key.get_pressed()
    is_moving = False

    # TODO 8: Move the player using LEFT and RIGHT arrow keys
    # Hint: update player_x and set is_moving = True when moving


    # 11. Check Jump and Attack duration
    if is_jumping and current_time - jump_start_time >= JUMP_DURATION:
        is_jumping = False

    if is_attacking and current_time - attack_start_time >= ATTACK_DURATION:
        is_attacking = False

    # 12. State Machine
    # TODO 9: Select the current state
    # Priority: Attack > Jump > Run > Idle
    # Hint: use if, elif, and else


    # 13. Select animation
    current_animation = animations[current_state]

    # Reset animation when the state changes
    if current_state != previous_state:
        current_frame = 0
        last_frame_time = current_time
        previous_state = current_state

    # 14. Update animation frame
    # TODO 10: Change to the next frame when enough time has passed
    # Hint: compare elapsed milliseconds with frame_duration * 1000
    # Formula: (current_frame + 1) % len(current_animation)


    # 15. Display
    screen.fill((40, 40, 40))

    # TODO 11: Display the current frame at (player_x, player_y)
    # Hint: screen.blit(current_animation[current_frame], (player_x, player_y))


    font = pygame.font.Font(None, 30)
    text = font.render("State: " + current_state, True, (255, 255, 255))
    screen.blit(text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
