from enum import Enum
import pygame

class Snake:
    def __init__(self, x,y):
        # Define velocity of the head and body separately,
        # and define size of the rect and distance between one rect
        # and another
        self.vel = 4
        self.head_vel = [4,0]
        self.size = 32
        self.distance = 36

        self.snake = [
                pygame.Rect(x, y,self.size,self.size),
                pygame.Rect(x - self.distance, y,self.size,self.size),
                pygame.Rect(x -2*self.distance, y,self.size,self.size),
                pygame.Rect(x -3*self.distance, y,self.size,self.size),
                pygame.Rect(x -4*self.distance, y,self.size,self.size),
                pygame.Rect(x -5*self.distance, y,self.size,self.size)
            ]
        # Don't do anything here is just being initalized
        # is being updated every time a move happen
        self.last_pos = [
                [x, y],
                [x - 2 * self.distance, y],
                [x - 3 * self.distance, y],
                [x - 4 * self.distance, y],
                [x - 5 * self.distance, y],
                [x - 6 * self.distance, y]
            ]

        # Variables to keep track of the distance travelled
        # and direction
        self.travelled = 0
        self.direction = Direction.RIGHT
        self.c = 0
    
    def move(self):
        self.c += 1

        for i, part in enumerate(self.snake):
            if i == 0:
                self.last_pos[i] = [part.x, part.y]
                part.x += self.head_vel[0]
                part.y += self.head_vel[1]
            else:
                if part.x < self.last_pos[i-1][0] and part.y == self.last_pos[i][1]:
                    # Test if the previous rect is going to the right and the y now is equal the previous y
                    # the y condition is to prevent this condition to be falsely activated
                    self.last_pos[i] = [part.x, part.y]
                    part.x += self.vel
                elif part.y < self.last_pos[i-1][1] and part.x == self.last_pos[i][0]:
                    # Test if the previous rect is going down and the x now is equal the previous x
                    # the x condition is to prevent this condition to be falsely activated
                    self.last_pos[i] = [part.x, part.y]
                    part.y += self.vel
                elif part.x > self.last_pos[i-1][0] and part.y == self.last_pos[i][1]:
                    # Test if the previous rect is going to the left and the y now is equal the previous y
                    # the y condition is to prevent this condition to be falsely activated
                    self.last_pos[i] = [part.x, part.y]
                    part.x -= self.vel
                elif part.y > self.last_pos[i-1][1] and part.x == self.last_pos[i][0]:
                    # Test if the previous rect is going up and the x now is equal the previous x
                    # the x condition is to prevent this condition to be falsely activated
                    self.last_pos[i] = [part.x, part.y]
                    part.y -= self.vel
                else:
                    # Some cases the part cannot activate the ifs
                    # so, is needed to test based on the previous part
                    # to decide where to go
                    self.last_pos[i] = [part.x, part.y]
                    if self.last_pos[i-1][0] < self.snake[i-1].x:
                        part.x += self.vel
                    elif self.last_pos[i-1][0] > self.snake[i-1].x:
                        part.x -= self.vel
                    elif self.last_pos[i-1][1] < self.snake[i-1].y:
                        part.y += self.vel
                    elif self.last_pos[i-1][1] > self.snake[i-1].y:
                        part.y -= self.vel
        

        self.travelled += self.vel


    def snake_events(self, event):
        if event.type == pygame.KEYDOWN:

            if self.travelled >= self.distance + self.vel:
                # Test if the distance travelled is greater than the
                # distance between the rects plus the current vel
                # It avoids the rects overlaps with each other

                if event.key == pygame.K_UP and self.direction != Direction.DOWN:
                    self.key_handler(Direction.UP, [0,-4])

                if event.key == pygame.K_DOWN and self.direction != Direction.UP:
                    self.key_handler(Direction.DOWN, [0, 4])

                if event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                    self.key_handler(Direction.LEFT, [-4,0])

                if event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                    self.key_handler(Direction.RIGHT, [4,0])
            

    def key_handler(self, direction, vel):
        # reset travelled every time that a key of movement is pressed
        # and update the following variables for the determined key
        self.direction = direction
        self.travelled = 0
        self.head_vel = vel

    def draw(self, surface):
        # Draw just that, loop through every part of the snake and draw
        for part_i, part in enumerate(self.snake):
            if part_i == 0:
                pygame.draw.rect(surface, 'green', part)
            elif part_i == len(self.snake) - 1:
                pygame.draw.rect(surface, 'blue', part)
            else:
                pygame.draw.rect(surface, 'red', part)


class Direction(Enum):
    # Class to assign a int to a direction why? don't know
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
