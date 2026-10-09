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
└── respawn()
```

The Apple no longer needs to know the board dimensions directly.

---

## ✅ Board Class

A `Board` class was introduced to handle the playing area.

```text
Board
├── width
├── height
└── random_position()
```

The board is responsible for generating valid random coordinates.

Example:

```python
board = Board(width=50, height=30)
position = board.random_position()
```

This generates:

```text
0 <= x <= 49
0 <= y <= 29
```

This avoids hardcoding board dimensions inside other classes.

---

## ✅ Game Class

A `Game` class has now been introduced as the coordinator of the game.

```text
Game
├── Board
├── Snake
├── Apple
└── score
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

This introduced an important OOP concept:

### Composition

A `Game` object contains other objects:

```text
Game
 ├── Board
 ├── Snake
 └── Apple
```

The Game does not need to implement everything itself.

Instead, it coordinates specialized objects.

---

# 🍎 Safe Apple Spawning

The project now prevents an Apple from spawning inside the Snake.

The current approach is:

```text
Game
 ↓
Ask Board for random position
 ↓
Ask Snake if it occupies that position
 ↓
Occupied?
 ├── YES → generate another position
 └── NO  → use the position
```

Current implementation:

```python
def spawn_apple(self):
    position = self.board.random_position()

    while self.snake.occupies(position):
        position = self.board.random_position()

    self.apple.position = position
```

This introduced another important concept:

### Object-to-object collaboration

Game coordinates:

```python
self.board.random_position()
```

and:

```python
self.snake.occupies(position)
```

instead of directly knowing how either object performs its job.

---

# 🧠 OOP Concepts Practiced So Far

## 1. Classes and Objects

A class defines the structure and behavior.

An object is an instance of that class.

```python
snake = Snake()
apple = Apple()
board = Board()
```

---

## 2. `__init__`

Used to initialize an object's state.

```python
def __init__(self):
    self.score = 0
```

---

## 3. `self`

`self` refers to the current object.

```python
self.body
self.position
self.score
```

---

## 4. Instance Attributes

Each object maintains its own state.

```python
self.body
self.direction
self.position
self.points
```

---

## 5. Instance Methods

Objects define behavior through methods.

Examples:

```python
snake.move()
snake.grow()
apple.respawn()
board.random_position()
```

---

## 6. Encapsulation

Objects manage their own state and behavior.

For example:

```python
snake.occupies(position)
```

allows Snake to answer whether a position belongs to its body without other objects needing to understand how its body is stored.

---

## 7. Composition

`Game` contains other objects:

```python
self.board = Board()
self.snake = Snake()
self.apple = Apple()
```

This is one of the major OOP concepts being practiced in this project.

---

## 8. Separation of Responsibilities

The project is gradually assigning each responsibility to the appropriate object.

```text
Snake
→ Owns and manages its body

Apple
→ Owns and manages its position and points

Board
→ Knows the dimensions of the playing area
→ Generates valid board positions

Game
→ Coordinates the objects
→ Manages overall game state
```

This is helping develop the intuition:

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
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
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

### Mutable Default Arguments

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

---

### Tuples for Coordinates

Coordinates are represented using tuples:

```python
(5, 5)
```

while the Snake body is a list of coordinate tuples:

```python
[(5, 5), (4, 5), (3, 5)]
```

This allows the body to change while individual coordinates remain immutable.

---

### Boolean State

Game state uses actual Boolean values:

```python
True
False
```

rather than:

```python
'True'
'False'
```

---

# 🚧 Current Development Status

### Completed

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
- [x] Safe Apple spawning logic
- [x] Separation of object responsibilities

### Currently Working On

- [ ] Improve Apple `respawn()` design
- [ ] Connect `Game.spawn_apple()` with `Apple.respawn()`
- [ ] Game update loop
- [ ] User input
- [ ] Wall collision
- [ ] Self collision
- [ ] Game-over logic
- [ ] Score management

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

Instead of learning OOP theoretically and then trying to apply it later, each feature introduces a new design problem.

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

> **"Which object should be responsible for this?"**

---

# 📖 Reference

The initial Snake implementation was inspired by:

**Programming Project #5: Snake — Robert Heaton**

https://robertheaton.com/2018/12/02/programming-project-5-snake/

The project is being extended significantly beyond the original implementation to serve as an OOP learning project.

---

# 📌 Status

**🚧 Work in Progress**

This project is being built step-by-step while learning Python OOP.

The final goal is not simply:

> "A Snake game that works."

It is:

> **"A Snake game that demonstrates strong object-oriented design."** 🐍🔥
