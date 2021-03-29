import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

def title():
    arcade.draw_text("Camel Game", WINDOW_WIDTH/2.5, 600, (10, 10, 10))
def guide():
    arcade.draw_text("Yiu're a nigerian", 640, 360, (10, 10, 10))
def on_draw(delta_time):
    guide()

def main():
    arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Camel Game")
    arcade.set_background_color(arcade.csscolor.LIGHT_CYAN)
    arcade.start_render()
    title()
    arcade.schedule(on_draw, 1 / 60)
    arcade.finish_render()
    arcade.run()




main()