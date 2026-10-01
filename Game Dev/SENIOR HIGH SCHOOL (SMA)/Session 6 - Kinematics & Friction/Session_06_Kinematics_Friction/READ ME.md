# Session 06 — Kinematics & Friction

## Space Shooter: Custom Physics

This version continues the Space Shooter OOP project from Session 05.

### What changed?

The Player movement now uses a simple custom physics system.

- `velocity` stores the player's current movement
- `acceleration` changes the velocity
- `friction` gradually reduces the velocity
- Movement uses `velocity * dt`
- `position` still uses `pygame.Vector2`
- `rect` is still used for drawing and collision
- Image assets are loaded from the `assets/` folder

## Movement Model

The Player now follows:

```text
Input
  ↓
Acceleration
  ↓
Velocity
  ↓
Friction
  ↓
Position
```

### Main physics formulas

```python
self.velocity += acceleration * dt
```

```python
self.velocity *= self.friction
```

```python
self.position += self.velocity * dt
```

## Folder structure

```text
Session_06_Kinematics_Friction/
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
acceleration = pygame.Vector2(0, 0)

self.velocity += acceleration * dt
self.velocity *= self.friction
self.position += self.velocity * dt
```

Acceleration changes velocity, friction reduces velocity over time, and velocity changes the player's position.

The `assets` folder must stay next to `space_shooter.py`.