import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg
from utils.scripts.fpscounter import FPSCounter

# region consts

fps_max: int = 0
screen_dims = (1280, 720)
screen_w, screen_h = screen_dims
radius = int(input("Fill in a goddamn radius: "))


# endregion consts


pg.init()
screen = pg.display.set_mode(screen_dims)
pg.display.set_caption("Anger burds")
clock = pg.time.Clock()
running = True

# Fps counter
fps_counter = FPSCounter(
    screen, pg.font.Font(None, 24), clock, (255, 255, 255), (5, 0, 75, 30)
)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # also quit if esc is pressed
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    # region update

    fps_counter.update()
    pg.draw.circle(screen, "red", (screen_w / 2, screen_h / 2), radius)
    pg.draw.circle(screen, "black", (screen_w / 2, screen_h / 2), radius - 5)

    # endregion update

    # region drawing

    fps_counter.draw()

    # endregion drawing

    # flip
    pg.display.flip()

    # update the dt
    dt = clock.tick(fps_max) / 1000


# Quit the pygame context
pg.quit()
