import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colorful Bounce")
clock = pygame.time.Clock()

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = random.randint(10, 30)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        self.color = [random.randint(50, 255) for _ in range(3)]
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)))
        self.vx = random.choice([-1, 1]) * random.randint(3, 7)
        self.vy = random.choice([-1, 1]) * random.randint(3, 7)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.vx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.vy *= -1

balls = pygame.sprite.Group()
for _ in range(10):
    balls.add(Ball())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30,100,200))
    balls.update()
    balls.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
