from enum import Enum
import pygame

class Snake:
    def __init__(self, x,y):
        self.vel = 4
        self.head_vel = [4,0]
        self.size = 32
        self.distancia = 36

        self.snake = [
                [
                pygame.Rect(x, y,self.size,self.size),
                pygame.Rect(x, y,self.size,self.size)
                ],
                [
                pygame.Rect(x -self.distancia, y,self.size,self.size), 
                pygame.Rect(x -2*self.distancia, y,self.size,self.size)
                ],
                [
                pygame.Rect(x -2*self.distancia, y,self.size,self.size),
                pygame.Rect(x -3*self.distancia, y,self.size,self.size)
                ],
                [
                pygame.Rect(x -3*self.distancia, y,self.size,self.size),
                pygame.Rect(x -4*self.distancia, y,self.size,self.size)
                ],
                [
                pygame.Rect(x -4*self.distancia, y,self.size,self.size),
                pygame.Rect(x -5*self.distancia, y,self.size,self.size)
                ],
                [
                pygame.Rect(x -5*self.distancia, y,self.size,self.size),
                pygame.Rect(x -6*self.distancia, y,self.size,self.size)
                ]
            ]


        self.travelled = 0
        self.direction = Direction.RIGHT
        self.c = 0
    
    def move(self):
        self.c += 1

        for i, part in enumerate(self.snake):
            if i == 0:
                part[1] = part[0].copy()
                part[0].x += self.head_vel[0]
                part[0].y += self.head_vel[1]
            else:

                if part[0].x < self.snake[i-1][1].x and part[0].y == part[1].y:
                    part[1] = part[0].copy()
                    part[0].x += self.vel
                elif part[0].y < self.snake[i-1][1].y and part[0].x == part[1].x:
                    part[1] = part[0].copy()
                    part[0].y += self.vel
                    
                elif part[0].x > self.snake[i-1][1].x and part[0].y == part[1].y:
                    part[1] = part[0].copy()
                    part[0].x -= self.vel
                elif part[0].y > self.snake[i-1][1].y and part[0].x == part[1].x:
                    part[1] = part[0].copy()
                    part[0].y -= self.vel
                else:
                    part[1] = part[0].copy()
                    if self.snake[i-1][1].x < self.snake[i-1][0].x:
                        part[0].x += self.vel
                    elif self.snake[i-1][1].x > self.snake[i-1][0].x:
                        part[0].x -= self.vel
                    elif self.snake[i-1][1].y < self.snake[i-1][0].y:
                        part[0].y += self.vel
                    elif self.snake[i-1][1].y > self.snake[i-1][0].y:
                        part[0].y -= self.vel
            
        self.travelled += self.vel



    def old_move(self):
        for i, part in enumerate(self.snake):
            if i == 0:
                part[1] = part[0].copy()
                part[0].x += self.head_vel[0]
                part[0].y += self.head_vel[1]
            else:
                print(f'{part[0].y} == {part[1].y}')
                if part[0].x != self.snake[i-1][1].x and part[0].y == part[1].y:
                    part[1] = part[0].copy()
                    if part[0].x < self.snake[i-1][0].x:
                        part[0].x += self.vel
                    elif part[0].x > self.snake[i-1][0].x:
                        part[0].x -= self.vel
                    continue

                if part[0].y != self.snake[i-1][0].y:
                    part[1] = part[0].copy()
                    if part[0].y < self.snake[i-1][0].y:
                        part[0].y += self.vel
                    elif part[0].y > self.snake[i-1][0].y:
                        part[0].y -= self.vel
                    continue
                
                
                part[1] = part[0].copy()
                #part[0].x += self.head_vel[0]
                #part[0].y += self.head_vel[1]

    def snake_events(self, event):
        if event.type == pygame.KEYDOWN and self.travelled >= self.distancia:

            if event.key == pygame.K_UP and self.direction != Direction.DOWN:
                self.key_handler(Direction.UP, [0,-4])

            if event.key == pygame.K_DOWN and self.direction != Direction.UP:
                self.key_handler(Direction.DOWN, [0, 4])

            if event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                self.key_handler(Direction.LEFT, [-4,0])

            if event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                self.key_handler(Direction.RIGHT, [4,0])
            

    def key_handler(self, direction, vel):

        self.direction = direction
        self.travelled = 0
        self.head_vel = vel

    def draw(self, surface):

        for part_i, part in enumerate(self.snake):
            if part_i == 0:
                pygame.draw.rect(surface, 'green', part[0])
            elif part_i == len(self.snake) - 1:
                pygame.draw.rect(surface, 'blue', part[0])
            else:
                pygame.draw.rect(surface, 'red', part[0])

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
