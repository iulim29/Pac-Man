import pygame
import random

screen_width = 620
screen_height =640
cell_size = 21
score = 0
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.collided = False


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pac-Man')

walls = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

pacman_image = pygame.image.load('C:/Users/iulia/Desktop/PacManSS/pacman.png').convert_alpha()
pacman_left = pygame.transform.rotate(pacman_image, 180)
pacman_right = pacman_image
pacman_up = pygame.transform.rotate(pacman_image, 90)
pacman_down = pygame.transform.rotate(pacman_image, 270)
pacman_images = {
    pygame.K_LEFT: pacman_left,
    pygame.K_RIGHT: pacman_right,
    pygame.K_UP: pacman_up,
    pygame.K_DOWN: pacman_down
}
pacman_rect = pacman_image.get_rect()
pacman_rect.x = screen_width // 2
pacman_rect.y = screen_height // 2


ghost_image = pygame.image.load('C:/Users/iulia/Desktop/PacManSS/blue_ghost.png')
ghost_width = ghost_image.get_width()
ghost_height = ghost_image.get_height()
ghost_rect = ghost_image.get_rect()

while True:
    ghost_rect.x = random.randint(0, screen_width - ghost_width)
    ghost_rect.y = random.randint(0, screen_height - ghost_height - 40)
    if not any(walls[row][col] and ghost_rect.colliderect(
            pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)) for row in range(len(walls)) for col in
               range(len(walls[0]))):
        break
dots = []
dots = list(set(dots))
for row in range(len(walls)):
    for col in range(len(walls[0])):
        if walls[row][col] == 1:  # Wall
            wall_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (0, 128, 255), wall_rect)
        elif walls[row][col] == 0 and (row % 2 == 0 or col % 2 == 0):  # Empty space, every other cell
            dot = Dot(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2)
            dots.append(dot)  # add dot to the dots list
            pygame.draw.circle(screen, (255, 255, 0), (dot.x, dot.y), 2)



current_pacman_image = pacman_image

running = True
while running:
    # Handle events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game state
    # Assuming that `walls` is a list of Rect objects representing the walls in your game

    wall_color = (0, 128, 255)
    wall_width = 5
    for row in range(len(walls)):
        for col in range(len(walls[row])):
            if walls[row][col] == 1:
                pygame.draw.rect(screen, wall_color, (col * cell_size, row * cell_size, cell_size, cell_size),
                                 wall_width)
    pygame.display.update()

    # Add boundary checks after the collision detection to prevent Pacman from moving out of the screen
    if pacman_rect.left < 0:
        pacman_rect.left = 0
    if pacman_rect.right > screen_width:
        pacman_rect.right = screen_width
    if pacman_rect.top < 0:
        pacman_rect.top = 0
    if pacman_rect.bottom > screen_height:
        pacman_rect.bottom = screen_height

    # Keep the rect within the bounds of the screen
    pacman_rect.clamp_ip(screen.get_rect())


    screen.blit(ghost_image, ghost_rect)

    screen.fill((0, 0, 0))

    screen.blit(ghost_image, ghost_rect)





    font = pygame.font.Font(None, 30)
    if pacman_rect.colliderect(ghost_rect):
        text = font.render("Game Over", True, (255, 0, 0))
        text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()

    for dot in dots:
        dot_rect = pygame.Rect(dot.x, dot.y, 4, 4)
        pygame.draw.rect(screen, (255, 255, 0), dot_rect)
        if pacman_rect.colliderect(dot_rect):
            if not dot.collided:
                dot.collided = True
                dots.remove(dot)
                score += 1
                # Move the following line outside the if block
                # to update the screen after a dot has been eaten
                pygame.display.update()

    speed = 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        current_pacman_image = pacman_left
        next_cell = walls[pacman_rect.top // cell_size][(pacman_rect.left - speed) // cell_size]
        if not next_cell:
            pacman_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        current_pacman_image = pacman_right
        next_cell = walls[pacman_rect.top // cell_size][(pacman_rect.right + speed) // cell_size]
        if not next_cell:
            pacman_rect.x += speed
    if keys[pygame.K_UP]:
        current_pacman_image = pacman_up
        next_cell = walls[(pacman_rect.top - speed) // cell_size][pacman_rect.left // cell_size]
        if not next_cell:
            pacman_rect.y -= speed
    if keys[pygame.K_DOWN]:
        current_pacman_image = pacman_down
        next_cell = walls[(pacman_rect.bottom + speed) // cell_size][pacman_rect.left // cell_size]
        if not next_cell:
            pacman_rect.y += speed
    screen.blit(current_pacman_image, pacman_rect)
    # Render the score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    score_rect = score_text.get_rect(bottomleft=(10, 630))
    screen.blit(score_text, score_rect)

    # Update the display
    #pygame.display.update()


