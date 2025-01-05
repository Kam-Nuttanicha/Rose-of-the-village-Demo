import pygame
import sys
import inhouse  # นำเข้า inhouse.py เพื่อเปลี่ยนหน้าต่าง

def run_rose_room():
    # กำหนดค่าต่าง ๆ
    WINDOW_WIDTH, WINDOW_HEIGHT = 800, 400
    BOX_WIDTH, BOX_HEIGHT = 90, 150
    BOX_COLOR = (255, 255, 0)  # สีเหลือง
    GREEN_BOX_COLOR = (0, 255, 0)  # สีเขียว
    GREEN_BOX_WIDTH, GREEN_BOX_HEIGHT = 150, 280  # ขนาดของสี่เหลี่ยมสีเขียว
    BACKGROUND_COLOR = (0, 0, 255)  # สีน้ำเงิน
    MOVE_SPEED = 5  # ความเร็วในการเคลื่อนที่

    # ตำแหน่งเริ่มต้นของกล่องสีเหลือง
    box_x = 200  # ห่างจากขอบซ้าย 200
    box_y = WINDOW_HEIGHT - BOX_HEIGHT - 20  # ห่างจากขอบล่าง 20

    # ตำแหน่งของสี่เหลี่ยมสีเขียว
    green_box_x = 30  # ห่างจากขอบซ้าย 30
    green_box_y = WINDOW_HEIGHT - GREEN_BOX_HEIGHT - 20  # ห่างจากขอบล่าง 20

    # เริ่มต้น pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Rose's Room")
    clock = pygame.time.Clock()

    # สถานะ
    show_message = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # ตรวจสอบการคลิกปุ่ม "Open"
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if show_message:  # หากข้อความและปุ่มแสดงอยู่
                    button_x = (WINDOW_WIDTH - 200) // 2
                    button_y = (WINDOW_HEIGHT - 70) * 0.8
                    if button_x <= mouse_pos[0] <= button_x + 200 and button_y <= mouse_pos[1] <= button_y + 70:
                        inhouse.run_inhouse()  # เรียกฟังก์ชันจาก inhouse.py
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

        # วาดสี่เหลี่ยมสีเขียว (ด้านหลัง)
        pygame.draw.rect(screen, GREEN_BOX_COLOR, (green_box_x, green_box_y, GREEN_BOX_WIDTH, GREEN_BOX_HEIGHT))

        # วาดกล่องสีเหลือง (ด้านหน้า)
        pygame.draw.rect(screen, BOX_COLOR, (box_x, box_y, BOX_WIDTH, BOX_HEIGHT))

        # ตรวจสอบการชนกันระหว่างกล่องสีเหลืองและสี่เหลี่ยมสีเขียว
        moving_box = pygame.Rect(box_x, box_y, BOX_WIDTH, BOX_HEIGHT)
        green_box = pygame.Rect(green_box_x, green_box_y, GREEN_BOX_WIDTH, GREEN_BOX_HEIGHT)

        if moving_box.colliderect(green_box):
            show_message = True
        else:
            show_message = False

        # แสดงข้อความและปุ่มหากชนกัน
        if show_message:
            font = pygame.font.Font(None, 36)
            text_surface = font.render("Hallway", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
            screen.blit(text_surface, text_rect)

            # วาดปุ่ม "Open"
            button_x = (WINDOW_WIDTH - 200) // 2
            button_y = (WINDOW_HEIGHT - 70) * 0.8
            pygame.draw.rect(screen, (0, 128, 255), (button_x, button_y, 200, 70))
            button_text = font.render("Open", True, (255, 255, 255))
            button_text_rect = button_text.get_rect(center=(button_x + 100, button_y + 35))
            screen.blit(button_text, button_text_rect)

        # อัปเดตหน้าจอ
        pygame.display.flip()

        # จำกัดเฟรมเรต
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_rose_room()
