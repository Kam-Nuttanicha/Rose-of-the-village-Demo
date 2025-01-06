import pygame
import sys
import thefront  # เพิ่มการ import thefront.py

def run_church():
    WINDOW_WIDTH, WINDOW_HEIGHT = 800, 400
    BOX_WIDTH, BOX_HEIGHT = 90, 150
    BOX_COLOR = (255, 255, 0)  # สีเหลือง
    GREEN_BOX_COLOR = (0, 255, 0)  # สีเขียว
    GREEN_BOX_WIDTH, GREEN_BOX_HEIGHT = 150, 280
    BACKGROUND_COLOR = (0, 0, 255)
    MOVE_SPEED = 5

    box_x = 200
    box_y = WINDOW_HEIGHT - BOX_HEIGHT - 20

    green_box_x = 30
    green_box_y = WINDOW_HEIGHT - GREEN_BOX_HEIGHT - 20

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Rose's Room")
    clock = pygame.time.Clock()

    show_message = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if show_message:
                    button_x = (WINDOW_WIDTH - 200) // 2
                    button_y = (WINDOW_HEIGHT - 70) * 0.8
                    if button_x <= mouse_pos[0] <= button_x + 200 and button_y <= mouse_pos[1] <= button_y + 70:
                        thefront.run_thefront()  # เรียกใช้ฟังก์ชันจาก thefront.py
                        running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            box_x -= MOVE_SPEED
        if keys[pygame.K_RIGHT]:
            box_x += MOVE_SPEED

        box_x = max(0, min(WINDOW_WIDTH - BOX_WIDTH, box_x))

        screen.fill(BACKGROUND_COLOR)

        pygame.draw.rect(screen, GREEN_BOX_COLOR, (green_box_x, green_box_y, GREEN_BOX_WIDTH, GREEN_BOX_HEIGHT))
        pygame.draw.rect(screen, BOX_COLOR, (box_x, box_y, BOX_WIDTH, BOX_HEIGHT))

        moving_box = pygame.Rect(box_x, box_y, BOX_WIDTH, BOX_HEIGHT)
        green_box = pygame.Rect(green_box_x, green_box_y, GREEN_BOX_WIDTH, GREEN_BOX_HEIGHT)

        if moving_box.colliderect(green_box):
            show_message = True
        else:
            show_message = False

        if show_message:
            font = pygame.font.Font(None, 36)
            text_surface = font.render("Hallway", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
            screen.blit(text_surface, text_rect)

            button_x = (WINDOW_WIDTH - 200) // 2
            button_y = (WINDOW_HEIGHT - 70) * 0.8
            pygame.draw.rect(screen, (0, 128, 255), (button_x, button_y, 200, 70))
            button_text = font.render("Open", True, (255, 255, 255))
            button_text_rect = button_text.get_rect(center=(button_x + 100, button_y + 35))
            screen.blit(button_text, button_text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_church()
