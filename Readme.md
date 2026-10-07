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

More libraries may be introduced later if the project requires them.

## 🚧 Current Progress

### Phase 1 — Snake Foundation

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
- [ ] Create `Apple` class
- [ ] Detect snake/apple collision
- [ ] Grow snake after eating an apple
- [ ] Implement score
- [ ] Create game loop
- [ ] Add board
- [ ] Add collision with walls
- [ ] Add self-collision
- [ ] Add user input
- [ ] Add game-over state

## 🐍 Current Snake Design

The current `Snake` object contains:

### Attributes

```text
body
direction
alive
```

### Methods

```text
move()
change_direction()
```

The snake body is represented using coordinates:

```python
[(5, 5), (4, 5), (3, 5)]
```

The first coordinate represents the head and the last coordinate represents the tail.

For example:

```text
HEAD                    TAIL
 ↓                       ↓
(5,5) → (4,5) → (3,5)
```

## 🔄 Snake Movement

Movement works by:

1. Finding the current head.
2. Calculating a new head position based on the direction.
3. Inserting the new head at the beginning of the body.
4. Removing the tail.

Example:

```text
Before:

[(5,5), (4,5), (3,5)]

Move RIGHT

[(6,5), (5,5), (4,5)]
```

This allows the snake to move without unnecessarily increasing its length.

## 🧠 OOP Concepts Practiced So Far

### Classes

The `Snake` class acts as a blueprint for Snake objects.

```python
class Snake:
    ...
```

### Objects

An actual Snake object can be created using:

```python
snake = Snake()
```

### Instance Attributes

The Snake stores its state using:

```python
self.body
self.direction
self.alive
```

### Instance Methods

The Snake contains behavior through methods:

```python
snake.move()
snake.change_direction("UP")
```

### Encapsulation

Instead of modifying the direction directly from outside:

```python
snake.direction = "UP"
```

the project introduces:

```python
snake.change_direction("UP")
```

This allows the Snake object to control whether a direction change is valid.

For example:

```text
RIGHT → LEFT ❌
RIGHT → UP   ✅
RIGHT → DOWN ✅
```

## 📚 Learning Approach

This project is intentionally being built incrementally.

Instead of copying a finished Snake implementation:

1. Design the object.
2. Identify its state.
3. Identify its responsibilities.
4. Implement a small feature.
5. Test it.
6. Find bugs.
7. Refactor when necessary.
8. Introduce new OOP concepts when the project requires them.

The goal is to understand **why** a particular OOP feature is useful, rather than simply memorizing its syntax.

## 🗺️ Planned Roadmap

### Phase 1 — Basic Snake

- Snake
- Apple
- Board
- Movement
- Eating
- Growth
- Score
- Collision

### Phase 2 — OOP Expansion

- Composition
- Better class responsibilities
- Game state
- Input handling
- Rendering

### Phase 3 — Advanced OOP

- Inheritance
- Polymorphism
- Abstract classes
- Interfaces/design contracts
- Properties
- Class methods
- Static methods

### Phase 4 — Python Object Model

- `__str__`
- `__repr__`
- `__eq__`
- `__len__`
- `__contains__`
- Other useful dunder methods

### Phase 5 — Better Data Modeling

- `dataclass`
- `Enum`
- Type hints
- Validation

### Phase 6 — Software Design

- SOLID principles
- Composition over inheritance
- Dependency injection
- Refactoring
- Design patterns

### Phase 7 — Advanced Features

- Multiple apple types
- Special food
- Obstacles
- Levels
- Increasing difficulty
- Multiple game modes
- High-score persistence
- AI-controlled Snake
- Player vs AI

## 📖 Reference

Initial project inspiration:

Robert Heaton's Snake programming project:

https://robertheaton.com/2018/12/02/programming-project-5-snake/

The implementation in this repository is being developed independently and expanded significantly for the purpose of learning Python OOP.

## 🚀 Status

**Work in Progress**

The project is being built step-by-step with the goal of turning a simple Snake game into a comprehensive Python OOP learning project.