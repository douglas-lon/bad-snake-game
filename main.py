import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.playing = True
        self.x = 100
        self.y = 100
        self.vel = [4,0]

        self.screen = pygame.display.set_mode((800,600))
        self.snake = [
            pygame.Rect(self.x, self.y,32,32),
            pygame.Rect(self.x -36, self.y,32,32),
            pygame.Rect(self.x -2*36, self.y,32,32),
            pygame.Rect(self.x -3*36, self.y,32,32)
            ]

        self.offset = [-36,0]

        pygame.display.set_caption('Cobrinha')
        self.direction = 'right'
        self.clock = pygame.time.Clock()
        self.travelled = 0
        

    
    def run(self):
        while self.playing:
            self.clock.tick(60)
            self.update()
            self.draw()
            self.events()

        pygame.quit()

    def update(self):
        self.snake[0].x += self.vel[0]
        self.snake[0].y += self.vel[1]

        for i, part in enumerate(self.snake):
            if i != 0:
                if self.direction == 'down':
                    if part.x < self.snake[i-1].x:
                        part.x += 4
                    elif part.x > self.snake[i-1].x:
                        part.x -= 4
                    else:
                        part.y += 4
                elif self.direction == 'left':
                    if part.y < self.snake[i-1].y:
                        part.y += 4
                    elif part.y > self.snake[i-1].y:
                        part.y -= 4
                    else:
                        part.x -= 4
                elif self.direction == 'right':
                    if part.y < self.snake[i-1].y:
                        part.y += 4
                    elif part.y > self.snake[i-1].y:
                        part.y -= 4
                    else:
                        part.x += 4
                elif self.direction == 'up':
                    if part.x > self.snake[i-1].x:
                        part.x -= 4
                    elif part.x < self.snake[i-1].x:
                        part.x += 4
                    else:
                        part.y -= 4



        if self.direction == 'right' and self.travelled >= 32:
            self.offset = [-36,0]
            self.vel = [4,0]
        elif self.direction == 'left' and self.travelled >= 32:
            self.vel = [-4,0]
            self.offset = [36,0]    
        elif self.direction == 'up' and self.travelled >= 32:
            self.vel = [0,-4]
            self.offset = [0,36]
        elif self.direction == 'down' and self.travelled >= 32:
            self.vel = [0,4]
            self.offset = [0,-36]

        if self.turned:
            self.turned = False
        self.travelled += 4


    def draw(self):
        self.screen.fill('black')
        
        for i, part in enumerate(self.snake):

            if i == 0:
                pygame.draw.rect(self.screen, 'green', part)
            elif i == len(self.snake) - 1:
                pygame.draw.rect(self.screen, 'blue', part)
            else:
                pygame.draw.rect(self.screen, 'red', part)

        pygame.display.update()

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.playing = False
            if event.type == pygame.KEYDOWN:
                self.travelled_body = 0
                if event.key == pygame.K_RIGHT:
                    self.direction = 'right'
                    self.turned = True
                    self.travelled = 0
                if event.key == pygame.K_LEFT:
                    self.direction = 'left'
                    self.turned = True
                    self.travelled = 0
                if event.key == pygame.K_UP:
                    self.direction = 'up'
                    self.turned = True
                    self.travelled = 0
                if event.key == pygame.K_DOWN:
                    self.direction = 'down'
                    self.turned = True
                    self.travelled = 0
                


if __name__ == '__main__':
    g = Game()
    g.run()