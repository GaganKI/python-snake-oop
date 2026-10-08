# 🐍 Snake — OOP Learning Project

A Snake game built from scratch in Python as a hands-on project to master **Object-Oriented Programming (OOP)**, Python fundamentals, and software design.

This project is being developed incrementally instead of starting from a completed implementation. Each feature is introduced to solve an actual problem in the game and reinforce an OOP concept.

## 🎯 Project Goal

The main goal of this project is not simply to build Snake.

The goal is to become confident with Python OOP by building a complete project from scratch.

Topics that will be explored throughout the project include:

- Classes and objects
- Constructors and `__init__`
- Instance attributes
- Instance methods
- Encapsulation
- Composition
- Inheritance
- Polymorphism
- Abstraction
- Abstract classes
- Class methods
- Static methods
- Properties
- Dunder methods
- Dataclasses
- Enums
- SOLID principles
- Design patterns
- Refactoring
- Clean code
- Object-oriented design

## 🛠️ Tech Stack

- **Python 3**
- Git
- GitHub

Additional libraries will be introduced as the project grows.

---

# 🚧 Current Progress

## Phase 1 — Core Game Objects

### 🐍 Snake

- [x] Create `Snake` class
- [x] Add snake body coordinates
- [x] Add direction
- [x] Add alive state
- [x] Implement movement
- [x] Support RIGHT movement
- [x] Support LEFT movement
- [x] Support UP movement
- [x] Support DOWN movement
- [x] Prevent direct opposite-direction movement
- [x] Implement snake growth
- [x] Detect Apple collision

### 🍎 Apple

- [x] Create `Apple` class
- [x] Add Apple position
- [x] Add Apple points
- [ ] Random Apple spawning
- [ ] Apple respawning after being eaten

### 🎮 Game

- [ ] Create `Game` class
- [ ] Game loop
- [ ] User input
- [ ] Board
- [ ] Score management
- [ ] Wall collision
- [ ] Self collision
- [ ] Game-over state

---

# 🧱 Current Architecture

The project currently contains two core classes:

```text
Snake
├── body
├── direction
├── alive
├── growing
│
├── move()
├── change_direction()
├── is_on_apple()
└── grow()


Apple
├── position
└── points
```

## 🐍 Snake

The Snake stores its current state:

```python
body
direction
alive
growing
```

The body is represented as a list of coordinate tuples:

```python
[(5, 5), (4, 5), (3, 5)]
```

The first coordinate represents the head and the last coordinate represents the tail.

### Movement

Snake movement works by:

1. Finding the current head.
2. Calculating a new head based on the current direction.
3. Inserting the new head at the beginning of the body.
4. Removing the tail during normal movement.

Example:

```text
Before:

[(5,5), (4,5), (3,5)]

Move RIGHT

[(6,5), (5,5), (4,5)]
```

### Growth

When the Snake needs to grow, the `growing` state is temporarily set to `True`.

During the next movement:

- A new head is added.
- The tail is not removed.
- The Snake becomes one segment longer.
- The `growing` state returns to `False`.

Example:

```text
Before:

[(5,5), (4,5), (3,5)]

After growth + movement:

[(6,5), (5,5), (4,5), (3,5)]
```

---

# 🍎 Apple

The Apple currently stores:

```python
position
points
```

Example:

```python
apple = Apple(position=(10,10), points=10)
```

The Snake can check whether its head is currently on the Apple:

```python
snake.is_on_apple(apple)
```

The current interaction is:

```text
Snake
  │
  │ checks head position
  ↓
Apple
  │
  ↓
Collision detected
  │
  ↓
snake.grow()
```

Random spawning and Apple respawning will be implemented in a later stage.

---

# 🧠 OOP Concepts Practiced So Far

## Classes and Objects

Classes act as blueprints:

```python
class Snake:
    ...
```

Objects are instances of those classes:

```python
snake = Snake()
apple = Apple()
```

## Instance Attributes

Objects maintain their own state:

```python
self.body
self.direction
self.alive
self.growing
```

## Instance Methods

Objects contain behavior:

```python
snake.move()
snake.change_direction("UP")
snake.grow()
```

## Encapsulation

The Snake controls its own behavior instead of allowing external code to directly manipulate its internal state.

For example:

```python
snake.change_direction("UP")
```

rather than relying entirely on:

```python
snake.direction = "UP"
```

The `Snake` class can therefore enforce rules such as preventing direct reversal:

```text
RIGHT → LEFT ❌
LEFT  → RIGHT ❌
UP    → DOWN ❌
DOWN  → UP ❌
```

## Object Interaction

The Snake and Apple now interact with each other:

```python
snake.is_on_apple(apple)
```

This is the beginning of designing multiple objects that cooperate rather than putting the entire game into one class.

## Mutable Default Arguments

The project also encountered and fixed a common Python issue.

Instead of:

```python
def __init__(self, body=[(5,5)]):
```

the constructor now uses:

```python
def __init__(self, body=None):
    if body is None:
        body = [(5,5)]
```

This ensures that different Snake objects don't accidentally share the same mutable list.

---

# 📚 Learning Approach

This project is intentionally being built incrementally.

Instead of copying a finished Snake implementation:

1. Design the object.
2. Identify its state.
3. Identify its responsibilities.
4. Implement a small feature.
5. Test it.
6. Find bugs.
7. Understand why the bug occurred.
8. Refactor when necessary.
9. Introduce new OOP concepts when the project requires them.

The goal is to understand **why** a particular OOP feature is useful rather than simply memorizing its syntax.

---

# 🗺️ Planned Roadmap

## Phase 1 — Basic Snake

- [x] Snake
- [x] Apple
- [x] Movement
- [x] Direction control
- [x] Snake growth
- [x] Snake/Apple collision detection
- [ ] Random Apple spawning
- [ ] Apple respawning
- [ ] Score
- [ ] Game loop
- [ ] Board
- [ ] Wall collision
- [ ] Self collision
- [ ] Game over

## Phase 2 — OOP Expansion

- [ ] Game class
- [ ] Composition
- [ ] Game state
- [ ] Input handling
- [ ] Rendering
- [ ] Better separation of responsibilities

## Phase 3 — Advanced OOP

- [ ] Inheritance
- [ ] Polymorphism
- [ ] Abstract classes
- [ ] Interfaces/design contracts
- [ ] Properties
- [ ] Class methods
- [ ] Static methods

## Phase 4 — Python Object Model

- [ ] `__str__`
- [ ] `__repr__`
- [ ] `__eq__`
- [ ] `__len__`
- [ ] `__contains__`
- [ ] Other useful dunder methods

## Phase 5 — Better Data Modeling

- [ ] Dataclasses
- [ ] Enums
- [ ] Type hints
- [ ] Validation

## Phase 6 — Software Design

- [ ] SOLID principles
- [ ] Composition over inheritance
- [ ] Dependency injection
- [ ] Refactoring
- [ ] Design patterns

## Phase 7 — Advanced Features

- [ ] Multiple Apple types
- [ ] Special food
- [ ] Obstacles
- [ ] Levels
- [ ] Increasing difficulty
- [ ] Multiple game modes
- [ ] High-score persistence
- [ ] AI-controlled Snake
- [ ] Player vs AI

---

# 📖 Reference

Initial project inspiration:

Robert Heaton's Snake programming project:

https://robertheaton.com/2018/12/02/programming-project-5-snake/

The implementation in this repository is being developed independently and expanded significantly for the purpose of learning Python OOP.

---

# 🚀 Status

**Work in Progress**

Current focus:

> Building the core Snake and Apple objects while learning Python OOP through implementation, debugging, and refactoring.

The project will continue evolving from a simple Snake game into a larger OOP-based application.