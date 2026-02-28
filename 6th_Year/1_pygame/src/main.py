import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

# pygame
import pygame as pg  # type: ignore



# fps counter
from utils.scripts.fpscounter import FPSCounter

# settings
from utils.settings.settings import load_settings

# player
from utils.scripts.player import Player


def main():
    # Load settings
    setts = load_settings()

    # Img path
    IMG_FOLDER = setts.get("IMG_FOLDER", os.path.dirname(__file__))
    
    # Screen dims
    (screen_w, screen_h) = setts.get("SCREEN_DIMS", (640, 360))

    # max_fps (start)
    max_fps = setts.get("START_FPS", 60)

    # pygame initialization
    pg.init()
    screen = pg.display.set_mode((screen_w, screen_h))
    pg.display.set_caption("Anger burds")
    pg.display.set_icon(pg.image.load(os.path.join(IMG_FOLDER, "Chuck-1.png")))
    clock = pg.time.Clock()

    # Fps counter
    fps_counter = FPSCounter(
        screen, pg.font.Font(None, 24), clock, (255, 255, 255), (5, 0, 75, 30)
    )

    # Players (max 3) — index auto-assigned; controls: arrows / WASD / IJKL
    # The Player constructor registers each instance in Player._registry automatically.
    Player.reset_registry()
    Player(screen, max_vel=500, drag=1, color="red", radius=25)  # index 0 — WASD
    Player(screen, max_vel=250, drag=8, color="blue", radius=25)  # index 1 — arrow keys
    Player(screen, max_vel=250, drag=20, color="green", radius=25)  # index 2 — IJKL

    # region variables

    running = True
    allow_fps_change = True

    dt = 1 / max_fps

    # events
    FPS_CHANGE_EVENT = pg.USEREVENT + 1

    # event timers
    pg.time.set_timer(FPS_CHANGE_EVENT, 100)

    # endregion variables

    # main game loop
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == FPS_CHANGE_EVENT:
                allow_fps_change = True

        # also quit if esc is pressed
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            running = False

        if allow_fps_change:
            if keys[pg.K_LSHIFT] or keys[pg.K_RSHIFT]:
                if keys[pg.K_PAGEUP]:
                    max_fps += 10
                elif keys[pg.K_PAGEDOWN]:
                    max_fps -= 10
                allow_fps_change = False
            else:
                if keys[pg.K_PAGEUP]:
                    max_fps += 1
                elif keys[pg.K_PAGEDOWN]:
                    max_fps -= 1
                allow_fps_change = False

            if max_fps < 10:
                max_fps = 10
            elif max_fps > 350:
                max_fps = 350

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # region update

        # Player movement + wall collision (handled inside each Player)
        Player.update_all(keys, dt)

        # update the fps text
        max_fps_text = "FPS Limit: " + str(max_fps)
        fps_font = pg.font.Font(None, 24)
        fps_text = fps_font.render(max_fps_text, True, (255, 255, 255))
        fps_text_rect = fps_text.get_rect(center=(screen_w / 2, 15))

        fps_counter.update()

        # endregion update

        # region drawing

        Player.draw_all()
        screen.blit(fps_text, fps_text_rect)
        fps_counter.draw()

        # flip
        pg.display.flip()

        # endregion drawing

        # update the dt
        dt = clock.tick(max_fps) / 1000

    # Quit the pygame context
    pg.quit()

    print("Pygame ran succesfully!")


if __name__ == "__main__":
    main()
