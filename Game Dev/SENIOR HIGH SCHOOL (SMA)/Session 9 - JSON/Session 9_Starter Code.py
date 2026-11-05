import pygame
import json

# 1. Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((400, 150))
pygame.display.set_caption("Sprite Sheet & JSON")

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

    # TODO 1: Create a rectangle using x, y, w, and h
    rect = pygame.Rect(
        # isi koordinat dan ukuran dari info JSON
    )

    # TODO 2: Extract the selected frame
    sprites[name] = sprite_sheet.subsurface(rect).copy()

# 6. Display extracted sprites
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((40, 40, 40))

    # TODO 3: Display all extracted sprites
    # Gunakan loop dan screen.blit()

    pygame.display.flip()

pygame.quit()