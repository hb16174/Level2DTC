import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 300


def ground():
    arcade.draw_lrtb_rectangle_filled(0, WINDOW_WIDTH, 100, 0, arcade.csscolor.GRAY)


def cactus(cactus_x):
    arcade.draw_rectangle_filled(cactus_x, 120, 20, 40, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(cactus_x + 10, 120, 10, 30, arcade.csscolor.BLACK)


def dinosaur(dino_y):
    arcade.draw_rectangle_filled(100, dino_y, 40, 50, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(90, dino_y + 7, 7, 7, arcade.csscolor.WHITE)
    arcade.draw_rectangle_filled(110, dino_y + 7, 7, 7, arcade.csscolor.WHITE)

def cacti_pos():
    if on_draw.cactus_x >= 170 and on_draw.cactus_x < 180:
        # on_draw.jump = 1
        on_draw.dino_y += 20
    if on_draw.cactus_x >= 140 and on_draw.cactus_x < 150:
        on_draw.dino_y += 20

    if on_draw.cactus_x <= 59 and on_draw.cactus_x > 50:
        on_draw.dino_y -= 20
    if on_draw.cactus_x <= 39 and on_draw.cactus_x > 30:
        on_draw.dino_y = 120

    if on_draw.cactus2_x >= 170 and on_draw.cactus2_x < 180:
        on_draw.dino_y += 20
    if on_draw.cactus2_x >= 140 and on_draw.cactus2_x < 150:
        on_draw.dino_y += 20

    if on_draw.cactus2_x <= 59 and on_draw.cactus2_x > 50:
        on_draw.dino_y -= 20
    if on_draw.cactus2_x <= 39 and on_draw.cactus2_x > 30:
        on_draw.dino_y = 120

    if on_draw.cactus3_x >= 170 and on_draw.cactus3_x < 180:
        on_draw.dino_y += 20
    if on_draw.cactus3_x >= 140 and on_draw.cactus3_x < 150:
        on_draw.dino_y += 20

    if on_draw.cactus3_x <= 59 and on_draw.cactus3_x > 50:
        on_draw.dino_y -= 20
    if on_draw.cactus3_x <= 39 and on_draw.cactus3_x > 30:
        on_draw.dino_y = 120



def on_draw(delta_time):
    if on_draw.cactus_x <= 0:
        on_draw.cactus_x = 1280
    if on_draw.cactus2_x <= 0:
        on_draw.cactus2_x = 1280
    if on_draw.cactus3_x <= 0:
        on_draw.cactus3_x = 1280

    cacti_pos()

    arcade.start_render()
    ground()
    dinosaur(on_draw.dino_y)
    cactus(on_draw.cactus_x)
    cactus(on_draw.cactus2_x)
    cactus(on_draw.cactus3_x)

    on_draw.cactus_x -= 5
    on_draw.cactus2_x -= 5
    on_draw.cactus3_x -= 5


on_draw.cactus_x = 1280
on_draw.cactus2_x = 853
on_draw.cactus3_x = 426

on_draw.dino_y = 120
on_draw.jump_clock = 0
on_draw.jump = 0


def main():
    arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Dinosaur")
    arcade.set_background_color(arcade.csscolor.LIGHT_GRAY)
    arcade.start_render()

    arcade.schedule(on_draw, 1 / 60)

    arcade.run()


main()
