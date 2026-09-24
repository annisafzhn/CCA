# Session 05 — Vector Mathematics

## Space Shooter: Vector2 Movement

This version continues the Space Shooter OOP project from Session 04.

### What changed?

The game now uses `pygame.Vector2` for object positions and movement.

- `position` uses `Vector2`
- `direction` uses `Vector2`
- Movement uses `direction * speed * dt`
- `normalize()` prevents diagonal movement from becoming faster
- `rect` is still used for drawing and collision
- Image assets are loaded from the `assets/` folder

## Folder structure

```text
Session_05_Vector_Mathematics/
├── space_shooter.py
├── README.md
└── assets/
    ├── space_background.png
    ├── player_ship.png
    ├── laser.png
    ├── asteroid_1.png
    ├── asteroid_2.png
    └── asteroid_3.png
```

## Run

Install Pygame if needed:

```powershell
pip install pygame
```

Then:

```powershell
python space_shooter.py
```

## Controls

- WASD / Arrow Keys = Move
- Space = Shoot

## Main lesson

```python
direction = pygame.Vector2(0, 0)

self.position += direction * self.speed * dt
```

The `assets` folder must stay next to `space_shooter.py`.
