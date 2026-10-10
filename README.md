# 🐍 Snake OOP — Learning Python OOP by Building a Game

A Snake game built from scratch in Python with a primary goal:

> **Learn and master Object-Oriented Programming by building a real project instead of studying OOP concepts in isolation.**

This project is being developed incrementally, with each new feature introducing an important Python/OOP concept.

---

## 🎯 Project Goal

The goal is not just to make a working Snake game.

The goal is to understand:

- Classes and objects
- Instance attributes and methods
- Encapsulation
- Composition
- Object-to-object interaction
- Separation of responsibilities
- Inheritance
- Polymorphism
- Abstract classes
- Properties
- Class methods and static methods
- Dunder methods
- Enums
- Dataclasses
- SOLID principles
- Design patterns
- Refactoring and clean architecture

The game will gradually become more complex as new OOP concepts are introduced.

---

## 🛠️ Tech Stack

- **Python 3**
- Git
- GitHub

Future technologies may be introduced as the project evolves.

---

# 📈 Current Progress

## ✅ Snake Class

The `Snake` class currently handles:

- Snake body
- Direction
- Alive state
- Movement
- Four directions
- Prevention of direct reversal
- Growth
- Apple collision detection
- Checking whether a position is occupied

Current structure:

```text
Snake
├── body
├── direction
├── alive
├── growing
├── move()
├── change_direction()
├── is_on_apple()
├── occupies()
└── grow()
```

Example body representation:

```python
[(5, 5), (4, 5), (3, 5)]
```

The first coordinate is the head and the last coordinate is the tail.

---

## ✅ Apple Class

The `Apple` class currently stores:

- Position
- Points

It also has a `respawn()` behavior.

Current structure:

```text
Apple
├── position
├── points
└── respawn(position)
```

The `respawn(position)` method updates the Apple’s position. Apple no longer needs to generate random coordinates or know the board dimensions.

---

## ✅ Board Class

The `Board` class handles the playing area's dimensions and generates random coordinates.

```text
Board
├── width
├── height
└── random_position()
```

Example:

```python
board = Board(width=50, height=30)
position = board.random_position()
```

The generated coordinates satisfy:

```text
0 <= x < width
0 <= y < height
```

This avoids hardcoding board dimensions inside other classes.

---

## ✅ Game Class

The `Game` class coordinates the objects and manages the score.

```text
Game
├── board
├── snake
├── apple
├── score
└── spawn_apple()
```

Current initialization:

```python
class Game:
    def __init__(self):
        self.board = Board()
        self.snake = Snake()
        self.apple = Apple()
        self.score = 0
```

This introduces an important OOP concept.

### Composition

A `Game` object contains other objects:

```text
Game
├── Board
├── Snake
└── Apple
```

The Game does not need to implement everything itself. Instead, it coordinates specialized objects.

---

# 🍎 Safe Apple Spawning

The game now prevents an Apple from spawning inside the Snake.

The current approach is:

```text
Game
  ↓
Ask Board for a random position
  ↓
Ask Snake if it occupies that position
  ↓
Occupied?
  ├── YES → generate another position
  └── NO  → give the position to Apple
```

Current implementation:

```python
def spawn_apple(self):
    position = self.board.random_position()

    while self.snake.occupies(position):
        position = self.board.random_position()

    self.apple.respawn(position)
```

This was tested successfully. The Apple spawned inside the board, and the following check returned `False`:

```python
game.snake.occupies(game.apple.position)
```

### Object-to-object collaboration

Game coordinates the other objects by calling their methods:

```python
self.board.random_position()
```

```python
self.snake.occupies(position)
```

```python
self.apple.respawn(position)
```

Each object performs its own responsibility instead of Game implementing all the internal logic itself.

**Known limitation:** if the Snake occupies every cell on the board, the current `while` loop will never finish. Handling this edge case is a future improvement.

---

# 🧠 OOP Concepts Practiced So Far

## 1. Classes and Objects

A class defines structure and behavior.

An object is an instance of that class.

```python
snake = Snake()
apple = Apple()
board = Board()
game = Game()
```

## 2. `__init__`

Used to initialize an object's state.

```python
def __init__(self):
    self.score = 0
```

## 3. `self`

`self` refers to the current object.

```python
self.body
self.position
self.score
```

## 4. Instance Attributes

Each object maintains its own state.

```python
self.body
self.direction
self.position
self.points
```

## 5. Instance Methods

Objects define behavior through methods.

Examples:

```python
snake.move()
snake.grow()
snake.occupies(position)
apple.respawn(position)
board.random_position()
game.spawn_apple()
```

## 6. Encapsulation

Objects manage their own state and behavior.

For example:

```python
apple.respawn(position)
```

allows Apple to update its own position, while:

```python
snake.occupies(position)
```

allows Snake to answer whether a coordinate belongs to its body.

## 7. Composition

`Game` contains other objects:

```python
self.board = Board()
self.snake = Snake()
self.apple = Apple()
```

This is one of the major OOP concepts being practiced in this project.

## 8. Separation of Responsibilities

The project assigns responsibilities to the appropriate objects.

```text
Snake
→ Owns and manages its body, direction, movement, and growth

Apple
→ Manages its position and points

Board
→ Knows the playing area's dimensions
→ Generates random coordinates

Game
→ Coordinates the objects
→ Manages overall game state
```

This helps develop the intuition:

> **Which object should be responsible for this behavior?**

---

# 🐍 Current Architecture

```text
                    ┌──────────────┐
                    │     Game     │
                    │              │
                    │    score     │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              ↓            ↓            ↓
        ┌──────────┐  ┌──────────┐  ┌──────────┐
        │  Board   │  │  Snake   │  │  Apple   │
        ├──────────┤  ├──────────┤  ├──────────┤
        │ width    │  │ body     │  │ position │
        │ height   │  │ direction│  │ points   │
        │          │  │ alive    │  │          │
        │ random_  │  │ growing  │  │ respawn()│
        │ position │  │ move()   │  │          │
        │          │  │ occupies │  │          │
        └──────────┘  └──────────┘  └──────────┘
```

---

# 🧪 Important Python Lessons

## Mutable Default Arguments

Avoid:

```python
def __init__(self, body=[]):
```

Instead:

```python
def __init__(self, body=None):
    if body is None:
        body = [(5, 5)]
```

## Tuples for Coordinates

Coordinates are represented using tuples:

```python
(5, 5)
```

The Snake body is a list of coordinate tuples:

```python
[(5, 5), (4, 5), (3, 5)]
```

This allows the body to change while individual coordinate tuples remain immutable.

## Boolean State

Game state uses actual Boolean values:

```python
True
False
```

rather than strings:

```python
'True'
'False'
```

---

# 🚧 Current Development Status

## Completed

- [x] Basic Snake class
- [x] Snake body representation
- [x] Four-direction movement
- [x] Direct-reversal prevention
- [x] Snake growth
- [x] Apple class
- [x] Apple collision detection
- [x] Board class
- [x] Random board positions
- [x] Snake position checking
- [x] Game class
- [x] Game composition
- [x] Safe Apple spawning
- [x] `Apple.respawn(position)` updates Apple's own state
- [x] Tested Apple spawning outside the Snake's body
- [x] Separation of object responsibilities

## Currently Working On

- [ ] Add `Board.is_inside(position)`
- [ ] Wall collision detection
- [ ] Self-collision detection
- [ ] Game-over logic
- [ ] Score management
- [ ] Game update loop
- [ ] User input
- [ ] Handle the full-board Apple-spawning edge case

---

# 🚀 Planned Roadmap

## Phase 1 — Basic Snake

- [x] Snake class
- [x] Movement
- [x] Direction changes
- [x] Growth

## Phase 2 — Game Objects

- [x] Apple class
- [x] Board class
- [x] Game class
- [x] Object interaction
- [x] Safe Apple spawning

## Phase 3 — Core Game

- [ ] Game loop
- [ ] User input
- [ ] Wall collision
- [ ] Self collision
- [ ] Game over
- [ ] Score

## Phase 4 — Advanced OOP

- [ ] Inheritance
- [ ] Polymorphism
- [ ] Abstract classes
- [ ] Properties
- [ ] Class methods
- [ ] Static methods
- [ ] Dunder methods
- [ ] Enums
- [ ] Dataclasses

## Phase 5 — Game Expansion

- [ ] Multiple Apples
- [ ] Special Apples
- [ ] Golden Apple
- [ ] Poison Apple
- [ ] Obstacles
- [ ] Walls
- [ ] Portals
- [ ] Speed boosts
- [ ] Slowdown effects
- [ ] Levels
- [ ] Lives
- [ ] Pause / Restart
- [ ] Different game modes

## Phase 6 — Advanced Features

- [ ] AI Snake
- [ ] Player vs AI
- [ ] Persistent high scores
- [ ] Leaderboard
- [ ] Save / Load game
- [ ] Final polished version

## Phase 7 — Software Design

- [ ] SOLID principles
- [ ] Refactoring
- [ ] Design patterns
- [ ] Testing
- [ ] Clean architecture

---

# 📚 Learning Approach

This project is intentionally being developed **incrementally**.

Instead of learning OOP theoretically and applying it later, each feature introduces a practical design problem.

For example:

```text
Need movement
    ↓
Instance methods

Need Snake state
    ↓
Instance attributes

Need Apple interaction
    ↓
Object collaboration

Need Board dimensions
    ↓
Separation of responsibilities

Need Game coordination
    ↓
Composition

Need different game entities
    ↓
Inheritance / Polymorphism
```

The objective is to develop the ability to look at a problem and ask:

> **Which object should be responsible for this?**

---

# 📖 Reference

The initial Snake implementation was inspired by:

**Programming Project #5: Snake — Robert Heaton**

https://robertheaton.com/2018/12/02/programming-project-5-snake/

The project is being extended significantly beyond the original implementation to serve as a Python OOP learning project.

---

# 📌 Status

**🚧 Work in Progress**

This project is being built step-by-step while learning Python OOP.

The final goal is not simply:

> "A Snake game that works."

It is:

> **"A Snake game that demonstrates strong object-oriented design."** 🐍🔥
