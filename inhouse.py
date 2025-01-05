import pygame
import sys
import rose_room  # นำเข้า rose_room เพื่อไปยังหน้าต่างนั้นเมื่อกดปุ่ม
import world_view  # นำเข้า world_view เพื่อไปยังหน้าต่างนั้นเมื่อกดปุ่ม

def run_inhouse():
    # กำหนดค่าต่าง ๆ
    WINDOW_WIDTH, WINDOW_HEIGHT = 800, 400  # ขนาดหน้าต่าง
    BOX_WIDTH, BOX_HEIGHT = 90, 150  # ขนาดของกล่อง (90x150)
    BOX_COLOR = (255, 255, 0)  # สีเหลือง
    BACKGROUND_COLOR = (0, 0, 255)  # สีน้ำเงิน (พื้นหลัง)
    WHITE_BOX_COLOR = (255, 255, 255)  # สีของสี่เหลี่ยมสีขาว
    WHITE_BOX_WIDTH, WHITE_BOX_HEIGHT = 50, 250  # ขนาดของสี่เหลี่ยมสีขาว
    BLACK_BOX_COLOR = (0, 0, 0)  # สีของสี่เหลี่ยมสีดำ
    BLACK_BOX_WIDTH, BLACK_BOX_HEIGHT = 50, 250  # ขนาดของสี่เหลี่ยมสีดำ
    GREEN_BOX_COLOR = (0, 255, 0)  # สีเขียว (กล่องใหม่)
    GREEN_BOX_WIDTH, GREEN_BOX_HEIGHT = 150, 280  # ขนาดใหม่ของกล่องสีเขียว (150x280)
    GREY_BOX_COLOR = (169, 169, 169)  # สีเทา (กล่องใหม่)
    GREY_BOX_WIDTH, GREY_BOX_HEIGHT = 150, 280  # ขนาดของกล่องสีเทา
    MOVE_SPEED = 5  # ความเร็วในการเคลื่อนที่

    # ตำแหน่งเริ่มต้นของกล่อง
    box_x = 200
    box_y = WINDOW_HEIGHT - BOX_HEIGHT - 20

    # ตำแหน่งของสี่เหลี่ยม
    white_box_x, white_box_y = 0, WINDOW_HEIGHT - WHITE_BOX_HEIGHT
    black_box_x, black_box_y = WINDOW_WIDTH - BLACK_BOX_WIDTH, WINDOW_HEIGHT - BLACK_BOX_HEIGHT
    green_box_x, green_box_y = black_box_x - GREEN_BOX_WIDTH - 80, WINDOW_HEIGHT - GREEN_BOX_HEIGHT - 20
    grey_box_x, grey_box_y = green_box_x - GREY_BOX_WIDTH - 50, WINDOW_HEIGHT - GREY_BOX_HEIGHT - 20

    # เริ่มต้น pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Inhouse Window")
    clock = pygame.time.Clock()

    # สถานะ
    show_button = False
    show_bathroom_message = False
    show_rose_room_message = False
    show_mom_dad_room_message = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                button_x, button_y = (WINDOW_WIDTH - 200) // 2, (WINDOW_HEIGHT - 70) * 0.8

                if show_button and button_x <= mouse_pos[0] <= button_x + 200 and button_y <= mouse_pos[1] <= button_y + 70:
                    world_view.run_world_view()
                    running = False

                if show_rose_room_message and button_x <= mouse_pos[0] <= button_x + 200 and button_y <= mouse_pos[1] <= button_y + 70:
                    rose_room.run_rose_room()
                    running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            box_x -= MOVE_SPEED
        if keys[pygame.K_RIGHT]:
            box_x += MOVE_SPEED
        box_x = max(0, min(WINDOW_WIDTH - BOX_WIDTH, box_x))

        screen.fill(BACKGROUND_COLOR)

        # วาดสี่เหลี่ยม
        pygame.draw.rect(screen, WHITE_BOX_COLOR, (white_box_x, white_box_y, WHITE_BOX_WIDTH, WHITE_BOX_HEIGHT))
        pygame.draw.rect(screen, BLACK_BOX_COLOR, (black_box_x, black_box_y, BLACK_BOX_WIDTH, BLACK_BOX_HEIGHT))
        pygame.draw.rect(screen, GREEN_BOX_COLOR, (green_box_x, green_box_y, GREEN_BOX_WIDTH, GREEN_BOX_HEIGHT))
        pygame.draw.rect(screen, GREY_BOX_COLOR, (grey_box_x, grey_box_y, GREY_BOX_WIDTH, GREY_BOX_HEIGHT))
        pygame.draw.rect(screen, BOX_COLOR, (box_x, box_y, BOX_WIDTH, BOX_HEIGHT))

        # การชน
        moving_box = pygame.Rect(box_x, box_y, BOX_WIDTH, BOX_HEIGHT)

        if moving_box.colliderect(pygame.Rect(white_box_x, white_box_y, WHITE_BOX_WIDTH, WHITE_BOX_HEIGHT)):
            show_button = True
            font = pygame.font.Font(None, 36)
            text_surface = font.render("Front Door", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
            screen.blit(text_surface, text_rect)
            button_x, button_y = (WINDOW_WIDTH - 200) // 2, (WINDOW_HEIGHT - 70) * 0.8
            pygame.draw.rect(screen, (0, 128, 255), (button_x, button_y, 200, 70))
            button_text = font.render("Open", True, (255, 255, 255))
            button_text_rect = button_text.get_rect(center=(button_x + 100, button_y + 35))
            screen.blit(button_text, button_text_rect)
        else:
            show_button = False

        if moving_box.colliderect(pygame.Rect(black_box_x, black_box_y, BLACK_BOX_WIDTH, BLACK_BOX_HEIGHT)):
            show_bathroom_message = True
        else:
            show_bathroom_message = False

        if moving_box.colliderect(pygame.Rect(green_box_x, green_box_y, GREEN_BOX_WIDTH, GREEN_BOX_HEIGHT)):
            show_rose_room_message = True
        else:
            show_rose_room_message = False

        if moving_box.colliderect(pygame.Rect(grey_box_x, grey_box_y, GREY_BOX_WIDTH, GREY_BOX_HEIGHT)):
            show_mom_dad_room_message = True
        else:
            show_mom_dad_room_message = False

        # แสดงข้อความ
        font = pygame.font.Font(None, 36)
        if show_rose_room_message:
            text = font.render("Rose's Room", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
            screen.blit(text, text_rect)
            button_x, button_y = (WINDOW_WIDTH - 200) // 2, (WINDOW_HEIGHT - 70) * 0.8
            pygame.draw.rect(screen, (0, 128, 255), (button_x, button_y, 200, 70))
            button_text = font.render("Open", True, (255, 255, 255))
            button_text_rect = button_text.get_rect(center=(button_x + 100, button_y + 35))
            screen.blit(button_text, button_text_rect)

        elif show_mom_dad_room_message:
            text = font.render("Mom & Dad Room Lock", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
            screen.blit(text, text_rect)

        elif show_bathroom_message:
            text = font.render("Bathroom Lock", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
            screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
