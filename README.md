# Pixel Fighters

A 2D pixel-art fighting game built with Python and Pygame featuring two characters in real-time combat.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [How to Play](#how-to-play)
- [Game Architecture](#game-architecture)
- [Class Diagram](#class-diagram)
- [Game State Flow](#game-state-flow)
- [Game Mechanics](#game-mechanics)
- [Technologies Used](#technologies-used)
- [File Structure](#file-structure)
- [Future Enhancements](#future-enhancements)

## Overview

**Pixel Fighters** is a competitive 2D fighting game where two players control unique characters (Baki and Samurai) in an arena-based combat system. The game features real-time combat mechanics including attacks, blocking, dodging via jumping, and a health system. Players battle to reduce their opponent's health to zero.

## Features

- **Two Playable Characters**: Baki and Samurai with unique animations
- **Real-Time Combat**: Attack, block, and movement mechanics
- **Animation System**: Frame-based sprite animations for all character actions
- **Health System**: Visual HP bars and damage calculation
- **Game States**: Menu, Fight, and Game Over screens
- **Keyboard Controls**: Customizable input for each player
- **Collision Detection**: Attack hitbox detection for damage application
- **Visual Effects**: Knockback and hurt animations

## Project Structure

```
Final_Project/
├── main.py              # Main game loop and state management
├── Character.py         # Character class and animation handling
├── images/              # Sprite assets
│   ├── Fighter/        # Baki character sprites
│   ├── Samurai/        # Samurai character sprites
│   └── fightericon.png # Game icon
├── fonts/              # Custom fonts
├── icons/              # UI icons and backgrounds
│   └── main_bg.jpg    # Game background
└── sounds/             # Audio assets (optional)
```

## Installation & Setup

### Requirements
- Python 3.7+
- Pygame library

### Install Dependencies
```bash
pip install pygame
```

### Run the Game
```bash
python main.py
```

## How to Play

### Main Menu
- Click the **"CLICK START"** button to begin the game

### Player 1 (Baki) Controls
| Action | Key |
|--------|-----|
| Move Left | A |
| Move Right | D |
| Jump | W |
| Attack | E |
| Block | F |

### Player 2 (Samurai) Controls
| Action | Key |
|--------|-----|
| Move Left | ← (Left Arrow) |
| Move Right | → (Right Arrow) |
| Jump | ↑ (Up Arrow) |
| Attack | Numpad 0 |
| Block | ↓ (Down Arrow) |

### Gameplay
1. Move closer to opponent to attack
2. Time your attacks to hit the opponent
3. Hold block to reduce incoming damage by 67%
4. Jump to dodge or create distance
5. Reduce opponent's HP to 0 to win
6. Click **"RESTART"** on game over screen to play again

## Game Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     PYGAME WINDOW                       │
│                   (1200 x 500 pixels)                   │
└─────────────────────────────────────────────────────────┘
                            ▼
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
    ┌────────┐         ┌────────┐         ┌──────────┐
    │ MENU   │────────▶│ FIGHT  │◀────────│ GAME OVER│
    │ STATE  │         │ STATE  │         │ STATE    │
    └────────┘         └────────┘         └──────────┘
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
        ┌─────────┐   ┌──────────┐   ┌─────────┐
        │Player 1 │   │Player 2  │   │Background
        │Updates  │   │Updates   │   │& UI
        │         │   │          │   │Rendering
        └─────────┘   └──────────┘   └─────────┘
```

## Class Diagram

```
┌────────────────────────────────────────────────────────────┐
│                      Character Class                       │
├────────────────────────────────────────────────────────────┤
│ Attributes:                                                │
│  ├─ name: str                    (Character name)          │
│  ├─ hp: int                      (Current health)          │
│  ├─ max_hp: int                  (Maximum health)          │
│  ├─ damage: int                  (Attack damage value)     │
│  ├─ x, y: float                  (Position on screen)      │
│  ├─ vx: float                    (Horizontal velocity)     │
│  ├─ state: str                   (Current animation state) │
│  ├─ animations: dict             (Loaded sprite frames)    │
│  ├─ is_attacking: bool           (Attack active status)    │
│  ├─ is_blocking: bool            (Block active status)     │
│  ├─ is_jumping: bool             (Jump active status)      │
│  ├─ is_hurt: bool                (Hurt state status)       │
│  ├─ is_dead: bool                (Death status)            │
│  ├─ frame_index: float           (Current animation frame) │
│  ├─ attack_cooldown: int         (Attack delay counter)    │
│  ├─ knockback_speed: float       (Knockback velocity)      │
│  └─ controls: dict               (Keyboard input mapping)  │
├────────────────────────────────────────────────────────────┤
│ Methods:                                                   │
│  ├─ __init__()                   Constructor              │
│  ├─ update(keys)                 Update character state    │
│  ├─ move(keys)                   Handle movement input     │
│  ├─ jump(keys)                   Handle jump logic         │
│  ├─ update_animation()           Manage sprite animation   │
│  ├─ draw(screen)                 Render character         │
│  ├─ start_attack()               Initiate attack          │
│  ├─ update_attack()              Process attack frames    │
│  ├─ damage_deal(other)           Deal damage to opponent  │
│  ├─ take_damage(dmg, attacker)  Receive damage           │
│  ├─ get_hitbox()                 Return collision box     │
│  ├─ attack_hitbox()              Return attack range      │
│  ├─ knockback()                  Apply knockback effect   │
│  ├─ update_hurt()                Handle hurt animation    │
│  └─ draw_hp(screen, x, y)       Render health bar        │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────┐
│       load_frames(folder) Function      │
├────────────────────────────────────────┤
│ Purpose: Load sprite images from path  │
│ Input:   folder path string            │
│ Output:  List of pygame image objects  │
└────────────────────────────────────────┘
```

## Game State Flow

```
                         START
                           │
                           ▼
                    ┌─────────────┐
                    │  MENU STATE │
                    └──────┬──────┘
                           │
                    Click Start Button
                           │
                           ▼
                    ┌─────────────────┐
                    │   FIGHT STATE   │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    │                 │
              Player 1         Player 2
              Takes Input      Takes Input
                    │                 │
                    └────────┬────────┘
                             │
                    Update Character States
                    ├─ Position Updates
                    ├─ Animation Frame Updates
                    ├─ Attack Resolution
                    ├─ Damage Calculation
                    └─ Status Effects
                             │
                    Check Defeat Condition
                    ├─ Player 1 HP ≤ 0?
                    └─ Player 2 HP ≤ 0?
                             │
                      YES ◄──┴──► NO
                      │         │
                      ▼         ▼
                ┌──────────┐  Loop Back to
                │GAME OVER │  Fight State
                │  STATE   │
                └────┬─────┘
                     │
              Click Restart Button
                     │
                     ▼
              Reset Game State
              ├─ HP Reset
              ├─ Position Reset
              ├─ Animation Reset
              └─ Cooldown Reset
                     │
                     ▼
              Return to FIGHT STATE
```

## Game Mechanics

### Attack System
- **Attack Cooldown**: 6 frames between attacks
- **Hit Window**: Attacks deal damage only during frames 3-3 of the animation
- **Attack Hitbox**: 40x80 pixels, extends forward from character
- **Damage Value**: 15 HP per hit

### Defense System
- **Blocking**: Reduces incoming damage by 67% (divides by 3)
- **Cannot Block**: During attacks, hurt state, or while dead
- **Knockback**: Applied on hit, decays at 80% per frame

### Movement System
- **Speed**: 10 pixels per frame
- **Map Boundaries**: X range 10-1100 pixels
- **Cannot Move**: During attacks, blocking, or hurt state

### Jump System
- **Jump Physics**: Quadratic trajectory using jump_count (0-18 frames)
- **Height**: Maximum ~40 pixels above base position
- **Air Control**: Cannot move horizontally while jumping

### Health System
- **Starting HP**: 100 points
- **Death**: Triggers death animation and game over state
- **Visual Feedback**: HP bar displayed at top of screen

## Technologies Used

- **Python 3**: Core programming language
- **Pygame**: Game engine and graphics rendering
- **Sprite Animation**: Frame-based animation system
- **Collision Detection**: Rectangle-based hitbox collision

## File Structure

### main.py
Main game loop and state management
- Initializes Pygame window (1200x500)
- Manages game states (menu, fight, game_over)
- Handles event processing (keyboard, mouse, quit)
- Renders UI elements (buttons, text, HP bars)
- Coordinates character updates and collision

### Character.py
Character class implementation
- Character attributes and state management
- Animation system with frame-based rendering
- Movement and jump physics
- Attack mechanics and hitbox detection
- Damage calculation and knockback physics
- Animation state transitions

### Asset Directories
- **images/Fighter/**: Baki character sprite sheets
  - idle_frames, run_frames, attack_frames, dead_frames, block_frames, hurt_frames
- **images/Samurai/**: Samurai character sprite sheets
  - idle_frames, run_frames, attack_frames, dead_frames, block_frames, hurt_frames
- **icons/**: Background image and visual assets
- **fonts/**: Custom TTF font files
- **sounds/**: Audio files (currently disabled)

## Future Enhancements

- [ ] Sound effects and background music
- [ ] Additional characters with unique movesets
- [ ] Special attacks and combos
- [ ] Multiplayer networking support
- [ ] AI opponent for single-player mode
- [ ] Difficulty levels
- [ ] Character customization
- [ ] Replay system
- [ ] Leaderboard
- [ ] More game modes (team battles, tournaments)
- [ ] Particle effects and visual polish
- [ ] Mobile/touch controls support

---

**Created**: May 2026  
**Language**: Python  
**License**: Open Source  
**Game Engine**: Pygame
