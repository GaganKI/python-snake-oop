class Snake:
    def __init__(self,body = [(5,5)], direction = 'RIGHT', alive = True):
        self.body = body
        self.direction = direction
        self.alive = alive
        
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
        
snake = Snake(body = [(5,5),(4,5),(3,5)],direction = "RIGHT")
snake.move()
snake.change_direction('UP')
print(snake.body)
print(snake.direction)