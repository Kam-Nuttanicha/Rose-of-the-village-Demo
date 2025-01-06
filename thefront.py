import pygame
import sys

def run_thefront():
    # กำหนดค่าต่าง ๆ
    WORLD_WIDTH, WORLD_HEIGHT = 800, 800  # ขนาดของโลก
    VIEWPORT_WIDTH, VIEWPORT_HEIGHT = 800, 600  # ขนาดของมุมมอง
    BOX_WIDTH, BOX_HEIGHT = 30, 50
    BOX_COLOR = (255, 255, 0)  # สีเหลือง
    BACKGROUND_COLOR = (0, 255, 0)  # สีเขียว
    STATIC_BOX_COLOR = (139, 69, 19)  # สีน้ำตาล
    STATIC_BOX_POSITION = (400, 400, 120, 100)  # ตำแหน่งและขนาดของสี่เหลี่ยมสีน้ำตาล

    # สี่เหลี่ยมย่อย
    INNER_BOX_COLOR = (101, 67, 33)  # สีน้ำตาลเข้ม
    INNER_BOX_WIDTH, INNER_BOX_HEIGHT = 50, 20

    # กล่องสีม่วง
    PURPLE_BOX_COLOR = (128, 0, 128)  # สีม่วง
    PURPLE_BOX_WIDTH, PURPLE_BOX_HEIGHT = STATIC_BOX_POSITION[2], STATIC_BOX_POSITION[3]
    PURPLE_BOX_POSITION = (80, 100, PURPLE_BOX_WIDTH, PURPLE_BOX_HEIGHT)

    # กล่องสีดำ
    BLACK_BOX_COLOR = (0, 0, 0)  # สีดำ
    BLACK_BOX_WIDTH, BLACK_BOX_HEIGHT = 50, 20
    black_box_x = PURPLE_BOX_POSITION[0] + (PURPLE_BOX_WIDTH // 2) - (BLACK_BOX_WIDTH // 2)
    black_box_y = PURPLE_BOX_POSITION[1] + PURPLE_BOX_HEIGHT - BLACK_BOX_HEIGHT
    black_box = pygame.Rect(black_box_x, black_box_y, BLACK_BOX_WIDTH, BLACK_BOX_HEIGHT)

    # กำหนดการเคลื่อนที่
    MOVE_SPEED = 5

    # เริ่มต้น pygame
    pygame.init()
    screen = pygame.display.set_mode((VIEWPORT_WIDTH, VIEWPORT_HEIGHT))  # หน้าต่าง 800x600
    pygame.display.set_caption("Camera Follow the Box")
    clock = pygame.time.Clock()

    # สร้าง `Rect` สำหรับกล่องสีน้ำตาลและสีม่วง
    static_box = pygame.Rect(*STATIC_BOX_POSITION)
    purple_box = pygame.Rect(*PURPLE_BOX_POSITION)

    # คำนวณตำแหน่งของสี่เหลี่ยมย่อย
    inner_box_x = STATIC_BOX_POSITION[0] + (STATIC_BOX_POSITION[2] // 2) - (INNER_BOX_WIDTH // 2)
    inner_box_y = STATIC_BOX_POSITION[1] + STATIC_BOX_POSITION[3] - INNER_BOX_HEIGHT
    inner_box = pygame.Rect(inner_box_x, inner_box_y, INNER_BOX_WIDTH, INNER_BOX_HEIGHT)
    
    # คำนวณตำแหน่งเริ่มต้นของกล่องสีเหลืองให้อยู่ใต้สี่เหลี่ยมสีน้ำตาลเข้ม (ห่าง 10 พิกเซล)
    box_x = 125
    box_y = 210

    # ลูปหลัก
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # ตำแหน่งเดิมของกล่อง (ก่อนเคลื่อนที่)
        prev_x, prev_y = box_x, box_y

        # กดปุ่มเพื่อเคลื่อนที่
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            box_y -= MOVE_SPEED
        if keys[pygame.K_DOWN]:
            box_y += MOVE_SPEED
        if keys[pygame.K_LEFT]:
            box_x -= MOVE_SPEED
        if keys[pygame.K_RIGHT]:
            box_x += MOVE_SPEED

        # สร้าง `Rect` สำหรับกล่องสีเหลือง
        moving_box = pygame.Rect(box_x, box_y, BOX_WIDTH, BOX_HEIGHT)

        # ตรวจสอบการชนกับกล่องสีดำ
        if moving_box.colliderect(black_box):
            print("Collision with black box! Moving to church.")
            pygame.quit()
            import church  # นำเข้าไฟล์ church.py
            church.run_church()  # เรียกฟังก์ชัน run_church()
            running = False

        # ตรวจสอบการชนกับสี่เหลี่ยมย่อย
        if moving_box.colliderect(inner_box):
            print("Reached the inner box!")
            pygame.quit()
            import inhouse
            inhouse.run_inhouse()
            running = False

        # ตรวจสอบการชนกับสี่เหลี่ยมสีน้ำตาลและสีม่วง
        if moving_box.colliderect(static_box) or moving_box.colliderect(purple_box):
            box_x, box_y = prev_x, prev_y

        # ตรวจสอบไม่ให้กล่องหลุดขอบของโลก
        box_x = max(0, min(WORLD_WIDTH - BOX_WIDTH, box_x))
        box_y = max(0, min(WORLD_HEIGHT - BOX_HEIGHT, box_y))

        # คำนวณมุมมอง (Viewport)
        camera_x = max(0, min(WORLD_WIDTH - VIEWPORT_WIDTH, box_x + BOX_WIDTH // 2 - VIEWPORT_WIDTH // 2))
        camera_y = max(0, min(WORLD_HEIGHT - VIEWPORT_HEIGHT, box_y + BOX_HEIGHT // 2 - VIEWPORT_HEIGHT // 2))

        # วาดภาพในโลก (World)
        world_surface = pygame.Surface((WORLD_WIDTH, WORLD_HEIGHT))
        world_surface.fill(BACKGROUND_COLOR)  # เติมพื้นหลังสีเขียว
        pygame.draw.rect(world_surface, STATIC_BOX_COLOR, static_box)  # วาดสี่เหลี่ยมสีน้ำตาล
        pygame.draw.rect(world_surface, PURPLE_BOX_COLOR, purple_box)  # วาดกล่องสีม่วง
        pygame.draw.rect(world_surface, BLACK_BOX_COLOR, black_box)  # วาดกล่องสีดำ
        pygame.draw.rect(world_surface, INNER_BOX_COLOR, inner_box)  # วาดสี่เหลี่ยมย่อย
        pygame.draw.rect(world_surface, BOX_COLOR, (box_x, box_y, BOX_WIDTH, BOX_HEIGHT))  # วาดกล่องสีเหลือง

        # ตัดส่วนของโลกตามมุมมอง
        viewport = world_surface.subsurface(camera_x, camera_y, VIEWPORT_WIDTH, VIEWPORT_HEIGHT)

        # แสดงผลบนหน้าจอ
        screen.blit(viewport, (0, 0))
        pygame.display.flip()

        # จำกัดเฟรมเรต
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_thefront()
