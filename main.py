import random
class Snake:
    def __init__(self,body = None, direction = 'RIGHT', alive = True):
        if body is None:
            body = [(5,5)]
            
        self.body = body
        self.direction = direction
        self.alive = alive
        self.growing = False
        
    def move(self):
        current_head = self.body[0]
        head_x,head_y = current_head
        if self.direction == 'RIGHT':
            new_head = (head_x + 1,head_y)
        elif self.direction == 'LEFT':
            new_head = (head_x - 1,head_y)
        elif self.direction == 'DOWN':
            new_head = (head_x,head_y + 1)
        elif self.direction == 'UP':
            new_head = (head_x,head_y - 1)
        
        self.body.insert(0,new_head)
        
        if self.growing:
            self.growing = False
        else:
            self.body.pop()
    
    def change_direction(self,new_direction):
        if self.direction == 'RIGHT' and new_direction != 'LEFT':
            self.direction = new_direction
        elif self.direction == 'LEFT' and new_direction != 'RIGHT':
            self.direction = new_direction
        elif self.direction == 'UP' and new_direction != 'DOWN':
            self.direction = new_direction
        elif self.direction == 'DOWN' and new_direction != 'UP':
            self.direction = new_direction
            
    def is_on_apple(self,apple):
        current_head = self.body[0]
        if current_head == apple.position:
            return True
        return False
    
    def occupies(self,position):
        if position in self.body:
            return True
        return False
    
    def grow(self):
        self.growing = True
        
class Apple:
    def __init__(self,position = (10,10), points = 10):
        self.position = position
        self.points = points
        
    def respawn(self,board):
        self.position = board.random_position()
        
class Board:
    def __init__(self,width = 20,height = 20):
        self.width = width
        self.height = height
        
    def random_position(self):
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        
        return (x,y)


class Game:
    def __init__(self):
        self.board = Board()
        self.snake = Snake()
        self.apple = Apple()
        self.score = 0
    
    def spawn_apple(self):
        position = self.board.random_position()
        
        while self.snake.occupies(position):
            position = self.board.random_position()

        self.apple.position = position
        
game = Game()

