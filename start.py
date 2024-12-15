import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Start Screen")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
DARK_BLUE = (30, 100, 200)

# Fonts
font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 50)

# Button settings
button_width = 200
button_height = 70
button_x = (SCREEN_WIDTH - button_width) // 2
button_y = (SCREEN_HEIGHT - button_height) // 2

def draw_button():
    mouse_pos = pygame.mouse.get_pos()
    if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[1] <= button_y + button_height:
        pygame.draw.rect(screen, DARK_BLUE, (button_x, button_y, button_width, button_height))
    else:
        pygame.draw.rect(screen, BLUE, (button_x, button_y, button_width, button_height))
    
    text_surface = button_font.render("Start Game", True, WHITE)
    text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    screen.blit(text_surface, text_rect)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[1] <= button_y + button_height:
                print("Game Started!")
                # Replace this with your game logic or call the main game function

    # Clear screen
    screen.fill(WHITE)

    # Draw title
    title_text = font.render("Welcome to the Game!", True, BLACK)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
    screen.blit(title_text, title_rect)

    # Draw button
    draw_button()

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
