import pygame
import sys

def run_world_view():
    # กำหนดค่าต่าง ๆ
    WORLD_WIDTH, WORLD_HEIGHT = 800, 800  # ขนาดของโลก
    VIEWPORT_WIDTH, VIEWPORT_HEIGHT = 800, 600  # ขนาดของมุมมอง (ปรับเป็น 800x600)
    BOX_WIDTH, BOX_HEIGHT = 30, 50
    BOX_COLOR = (255, 255, 0)  # สีเหลือง
    BACKGROUND_COLOR = (0, 255, 0)  # สีเขียว
    STATIC_BOX_COLOR = (139, 69, 19)  # สีน้ำตาล
    STATIC_BOX_POSITION = (400, 400, 120, 100)  # ตำแหน่งและขนาดของสี่เหลี่ยมสีน้ำตาล

    # สี่เหลี่ยมย่อย
    INNER_BOX_COLOR = (101, 67, 33)  # สีน้ำตาลเข้ม
    INNER_BOX_WIDTH, INNER_BOX_HEIGHT = 50, 20

    # กำหนดการเคลื่อนที่
    MOVE_SPEED = 5

    # เริ่มต้น pygame
    pygame.init()
    screen = pygame.display.set_mode((VIEWPORT_WIDTH, VIEWPORT_HEIGHT))  # ขยายหน้าต่างเป็น 800x600
    pygame.display.set_caption("Camera Follow the Box")
    clock = pygame.time.Clock()

    # สร้าง `Rect` สำหรับกล่องสีน้ำตาล
    static_box = pygame.Rect(*STATIC_BOX_POSITION)

    # คำนวณตำแหน่งของสี่เหลี่ยมย่อย
    inner_box_x = STATIC_BOX_POSITION[0] + (STATIC_BOX_POSITION[2] // 2) - (INNER_BOX_WIDTH // 2)
    inner_box_y = STATIC_BOX_POSITION[1] + STATIC_BOX_POSITION[3] - INNER_BOX_HEIGHT

    inner_box = pygame.Rect(inner_box_x, inner_box_y, INNER_BOX_WIDTH, INNER_BOX_HEIGHT)

    # คำนวณตำแหน่งเริ่มต้นของกล่องสีเหลืองให้อยู่ใต้สี่เหลี่ยมสีน้ำตาลเข้ม (ห่าง 10 พิกเซล)
    box_x = inner_box_x + (INNER_BOX_WIDTH // 2) - (BOX_WIDTH // 2)
    box_y = inner_box_y + INNER_BOX_HEIGHT + 10  # ห่างจาก inner_box 10 พิกเซล

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

        # ตรวจสอบการชนกับสี่เหลี่ยมสีน้ำตาลเข้ม
        if moving_box.colliderect(inner_box):
            print("Reached the inner box!")
            pygame.quit()  # ปิดหน้าต่างปัจจุบัน
            import inhouse  # นำเข้าไฟล์ inhouse.py
            inhouse.run_inhouse()  # เรียกฟังก์ชัน run_inhouse()
            running = False


        # ตรวจสอบการชนกับสี่เหลี่ยมสีน้ำตาลธรรมดา
        if moving_box.colliderect(static_box):
            # หากชน ให้กลับตำแหน่งเดิม
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
        pygame.draw.rect(world_surface, INNER_BOX_COLOR, inner_box)  # วาดสี่เหลี่ยมย่อย
        pygame.draw.rect(world_surface, BOX_COLOR, (box_x, box_y, BOX_WIDTH, BOX_HEIGHT))  # วาดกล่องสีเหลี่ยม

        # ตัดส่วนของโลกตามมุมมอง
        viewport = world_surface.subsurface(camera_x, camera_y, VIEWPORT_WIDTH, VIEWPORT_HEIGHT)

        # แสดงผลบนหน้าจอ
        screen.blit(viewport, (0, 0))
        pygame.display.flip()

        # จำกัดเฟรมเรต
        clock.tick(60)

    pygame.quit()
    sys.exit()
