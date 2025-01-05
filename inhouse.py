import pygame
import sys

# นำเข้า world_view เพื่อไปยังหน้าต่างนั้นเมื่อกดปุ่ม
import world_view

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
    box_x = 60
    box_y = WINDOW_HEIGHT - BOX_HEIGHT - 20

    # ตำแหน่งของสี่เหลี่ยมสีขาว (ชิดขอบซ้ายล่าง)
    white_box_x = 0
    white_box_y = WINDOW_HEIGHT - WHITE_BOX_HEIGHT

    # ตำแหน่งของสี่เหลี่ยมสีดำ (ชิดขอบขวาล่าง)
    black_box_x = WINDOW_WIDTH - BLACK_BOX_WIDTH
    black_box_y = WINDOW_HEIGHT - BLACK_BOX_HEIGHT

    # ตำแหน่งของสี่เหลี่ยมสีเขียว (ห่างจากขอบขวาของสี่เหลี่ยมสีดำ 80 พิกเซล และห่างจากขอบล่าง 20 พิกเซล)
    green_box_x = black_box_x - GREEN_BOX_WIDTH - 80  # ห่างจากขอบขวาของสี่เหลี่ยมสีดำ 80 พิกเซล
    green_box_y = WINDOW_HEIGHT - GREEN_BOX_HEIGHT - 20  # ห่างจากขอบล่าง 20 พิกเซล

    # ตำแหน่งของสี่เหลี่ยมสีเทา (ห่างจากขอบขวาของสี่เหลี่ยมสีเขียว 50 พิกเซล และห่างจากขอบล่าง 20 พิกเซล)
    grey_box_x = green_box_x - GREY_BOX_WIDTH - 50  # ห่างจากขอบขวาของสี่เหลี่ยมสีเขียว 50 พิกเซล
    grey_box_y = WINDOW_HEIGHT - GREY_BOX_HEIGHT - 20  # ห่างจากขอบล่าง 20 พิกเซล

    # เริ่มต้น pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Inhouse Window")
    clock = pygame.time.Clock()

    # สถานะที่ใช้เช็คว่ากล่องสีเหลืองชนกับสี่เหลี่ยมสีขาวหรือไม่
    show_button = False
    show_bathroom_message = False  # ใช้เช็คว่าแสดงข้อความ "Bathroom lock" หรือไม่
    show_rose_room_message = False  # ใช้เช็คว่าแสดงข้อความ "Rose's Room" หรือไม่
    show_mom_dad_room_message = False  # ใช้เช็คว่าแสดงข้อความ "Mom & Dad Room Lock" หรือไม่

    # ลูปหลัก
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # ตรวจสอบการคลิกปุ่ม "Open Door"
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if show_button:  # หากปุ่มแสดงอยู่
                    button_x = (WINDOW_WIDTH - 200) // 2
                    button_y = (WINDOW_HEIGHT - 70) * 0.8  # ตำแหน่งกลางค่อนไปขอบล่าง
                    if button_x <= mouse_pos[0] <= button_x + 200 and button_y <= mouse_pos[1] <= button_y + 70:
                        world_view.run_world_view()  # เรียกฟังก์ชันจาก world_view.py
                        running = False

        # การควบคุมการเคลื่อนที่
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            box_x -= MOVE_SPEED
        if keys[pygame.K_RIGHT]:
            box_x += MOVE_SPEED

        # จำกัดการเคลื่อนที่ให้อยู่ในกรอบหน้าต่าง
        box_x = max(0, min(WINDOW_WIDTH - BOX_WIDTH, box_x))

        # ล้างหน้าจอ
        screen.fill(BACKGROUND_COLOR)

        # วาดสี่เหลี่ยมสีขาว
        pygame.draw.rect(screen, WHITE_BOX_COLOR, (white_box_x, white_box_y, WHITE_BOX_WIDTH, WHITE_BOX_HEIGHT))

        # วาดสี่เหลี่ยมสีดำ
        pygame.draw.rect(screen, BLACK_BOX_COLOR, (black_box_x, black_box_y, BLACK_BOX_WIDTH, BLACK_BOX_HEIGHT))

        # วาดสี่เหลี่ยมสีเขียว (ขนาดใหม่ 150x280)
        pygame.draw.rect(screen, GREEN_BOX_COLOR, (green_box_x, green_box_y, GREEN_BOX_WIDTH, GREEN_BOX_HEIGHT))

        # วาดสี่เหลี่ยมสีเทา (ขนาด 150x280)
        pygame.draw.rect(screen, GREY_BOX_COLOR, (grey_box_x, grey_box_y, GREY_BOX_WIDTH, GREY_BOX_HEIGHT))

        # วาดกล่องสีเหลือง
        pygame.draw.rect(screen, BOX_COLOR, (box_x, box_y, BOX_WIDTH, BOX_HEIGHT))

        # เช็คว่ากล่องสีเหลืองชนกับสี่เหลี่ยมสีขาว
        moving_box = pygame.Rect(box_x, box_y, BOX_WIDTH, BOX_HEIGHT)
        white_box = pygame.Rect(white_box_x, white_box_y, WHITE_BOX_WIDTH, WHITE_BOX_HEIGHT)

        if moving_box.colliderect(white_box):
            # ถ้าชนให้แสดงข้อความและปุ่ม
            show_button = True
            font = pygame.font.Font(None, 36)
            text_surface = font.render("Front Door", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
            screen.blit(text_surface, text_rect)

            # วาดปุ่ม "Open Door"
            button_x = (WINDOW_WIDTH - 200) // 2
            button_y = (WINDOW_HEIGHT - 70) * 0.8  # ตำแหน่งกลางค่อนไปขอบล่าง
            pygame.draw.rect(screen, (0, 128, 255), (button_x, button_y, 200, 70))
            button_text = font.render("Open Door", True, (255, 255, 255))
            button_text_rect = button_text.get_rect(center=(button_x + 100, button_y + 35))
            screen.blit(button_text, button_text_rect)

        else:
            # ถ้าไม่ชนไม่แสดงปุ่มและข้อความ
            show_button = False

        # เช็คว่ากล่องสีเหลืองชนกับสี่เหลี่ยมสีดำ
        black_box = pygame.Rect(black_box_x, black_box_y, BLACK_BOX_WIDTH, BLACK_BOX_HEIGHT)
        if moving_box.colliderect(black_box):
            # ถ้าชนให้แสดงข้อความ "Bathroom lock"
            show_bathroom_message = True
        else:
            show_bathroom_message = False

        # เช็คว่ากล่องสีเหลืองชนกับสี่เหลี่ยมสีเขียว
        green_box = pygame.Rect(green_box_x, green_box_y, GREEN_BOX_WIDTH, GREEN_BOX_HEIGHT)
        if moving_box.colliderect(green_box):
            # ถ้าชนให้แสดงข้อความ "Rose's Room" และปุ่ม
            show_rose_room_message = True
        else:
            show_rose_room_message = False

        # เช็คว่ากล่องสีเหลืองชนกับสี่เหลี่ยมสีเทา
        grey_box = pygame.Rect(grey_box_x, grey_box_y, GREY_BOX_WIDTH, GREY_BOX_HEIGHT)
        if moving_box.colliderect(grey_box):
            # ถ้าชนให้แสดงข้อความ "Mom & Dad Room Lock"
            show_mom_dad_room_message = True
        else:
            show_mom_dad_room_message = False

        # แสดงข้อความตามสถานะ
        font = pygame.font.Font(None, 36)
        if show_rose_room_message:
            rose_room_text = font.render("Rose's Room", True, (255, 255, 255))
            rose_room_text_rect = rose_room_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
            screen.blit(rose_room_text, rose_room_text_rect)

            # วาดปุ่ม "Open"
            button_x = (WINDOW_WIDTH - 200) // 2
            button_y = (WINDOW_HEIGHT - 70) * 0.8  # ตำแหน่งกลางค่อนไปขอบล่าง
            pygame.draw.rect(screen, (0, 128, 255), (button_x, button_y, 200, 70))
            button_text = font.render("Open", True, (255, 255, 255))
            button_text_rect = button_text.get_rect(center=(button_x + 100, button_y + 35))
            screen.blit(button_text, button_text_rect)

        elif show_mom_dad_room_message:
            mom_dad_room_text = font.render("Mom & Dad Room Lock", True, (255, 255, 255))
            mom_dad_room_text_rect = mom_dad_room_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
            screen.blit(mom_dad_room_text, mom_dad_room_text_rect)

        elif show_bathroom_message:
            bathroom_text = font.render("Bathroom Lock", True, (255, 255, 255))
            bathroom_text_rect = bathroom_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
            screen.blit(bathroom_text, bathroom_text_rect)

        # อัปเดตหน้าจอ
        pygame.display.flip()

        # จำกัดเฟรมเรต
        clock.tick(60)

    pygame.quit()
    sys.exit()
