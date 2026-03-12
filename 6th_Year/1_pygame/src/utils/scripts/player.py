import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg  # type: ignore
import math
from ..settings.settings import load_settings # type: ignore

setts = load_settings()

screen_w, screen_h = setts["SCREEN_DIMS"]


class Player:
    """
    CS-style circle player with velocity-based movement and drag.

    Drag model
    ----------
    Each frame the velocity decays by a factor of ``drag``:
        v *= (1 - drag * dt)

    Acceleration is set to ``max_vel * drag`` so that the player
    naturally approaches ``max_vel`` as the terminal velocity.
    Counter-strafing (pressing the opposite direction key) adds
    velocity in the opposite direction, which—combined with the
    existing negative acceleration—halts movement very quickly.

    Controls (per index)
    --------------------
    0: WASD        (W / S / A / D)
    1: Arrow keys  (UP / DOWN / LEFT / RIGHT) = Arrow keys
    2: IJKL        (I / K / J / L)
    """

    MAX_PLAYERS = setts["MAX_PLAYERS"]

    # Key bindings for each player slot
    _CONTROLS: list[dict[str, int]] = [
        {  # Player 0 — WASD
            "up":    pg.K_w,
            "down":  pg.K_s,
            "left":  pg.K_a,
            "right": pg.K_d,
        },
        {  # Player 1 — arrow keys
            "up":    pg.K_UP,
            "down":  pg.K_DOWN,
            "left":  pg.K_LEFT,
            "right": pg.K_RIGHT,
        },
        {  # Player 2 — IJKL
            "up":    pg.K_i,
            "down":  pg.K_k,
            "left":  pg.K_j,
            "right": pg.K_l,
        },
    ]

    # Class-level registry so the constructor can auto-assign an index
    _registry: list["Player"] = []

    # ------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------

    def __init__(
        self,
        screen: pg.Surface,
        max_vel: float,
        drag: float,
        color: str | tuple | pg.Color,
        radius: int,
    ) -> None:
        if len(Player._registry) >= Player.MAX_PLAYERS:
            raise RuntimeError(
                f"Cannot create more than {Player.MAX_PLAYERS} players."
            )

        self.index: int = len(Player._registry)
        Player._registry.append(self)

        self.screen = screen
        self.max_vel = max_vel
        self.drag = drag          # deceleration coefficient (higher = snappier stop)
        self.accel = max_vel * drag  # acceleration that balances drag at max_vel
        self.color = color
        self.radius = radius

        # Spread starting positions across the screen width
        sections = Player.MAX_PLAYERS + 1
        self.x: float = screen_w * (self.index + 1) / sections
        self.y: float = screen_h / 2

        self.vx: float = 0.0
        self.vy: float = 0.0
        self.score: int = 0

        self.controls = Player._CONTROLS[self.index]

    # ------------------------------------------------------------------
    # Class helpers
    # ------------------------------------------------------------------

    @classmethod
    def reset_registry(cls) -> None:
        """Clear the player registry (call before re-creating players)."""
        cls._registry.clear()

    @classmethod
    def update_all(cls, keys: pg.key.ScancodeWrapper, dt: float) -> None:
        for player in cls._registry:
            player.update(keys, dt)
        cls.resolve_all_collisions()

    @classmethod
    def resolve_all_collisions(cls) -> None:
        """Resolve elastic collisions between every pair of players."""
        registry = cls._registry
        for i in range(len(registry)):
            for j in range(i + 1, len(registry)):
                registry[i].resolve_collision(registry[j])

    @classmethod
    def draw_all(cls) -> None:
        for player in cls._registry:
            player.draw()

    # ------------------------------------------------------------------
    # Per-frame logic
    # ------------------------------------------------------------------

    def update(self, keys: pg.key.ScancodeWrapper, dt: float) -> None:
        ctrl = self.controls

        # Apply acceleration in the pressed direction(s)
        if keys[ctrl["up"]]:
            self.vy -= self.accel * dt
        if keys[ctrl["down"]]:
            self.vy += self.accel * dt
        if keys[ctrl["left"]]:
            self.vx -= self.accel * dt
        if keys[ctrl["right"]]:
            self.vx += self.accel * dt

        # Drag — true exponential decay (always positive; avoids sign-flip when drag*dt > 1)
        decay = math.exp(-self.drag * dt)
        self.vx *= decay
        self.vy *= decay

        # Clamp to max speed (diagonal movement shouldn't be faster)
        speed = math.hypot(self.vx, self.vy)
        if speed > self.max_vel:
            scale = self.max_vel / speed
            self.vx *= scale
            self.vy *= scale

        # Integrate position
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Wall collision — elastic bounce off screen borders
        if self.x + self.radius > screen_w:
            self.x = screen_w - self.radius
            self.vx = -self.vx
        elif self.x - self.radius < 0:
            self.x = self.radius
            self.vx = -self.vx

        if self.y + self.radius > screen_h:
            self.y = screen_h - self.radius
            self.vy = -self.vy
        elif self.y - self.radius < 0:
            self.y = self.radius
            self.vy = -self.vy

    def resolve_collision(self, other: "Player") -> None:
        """
        Elastic collision between two circles of equal mass.

        Steps
        -----
        1. Measure the distance between centres.
        2. If they overlap, push them apart along the collision normal.
        3. Exchange velocity components along the normal (elastic, equal mass).
        """
        dx = self.x - other.x
        dy = self.y - other.y
        dist = math.hypot(dx, dy)
        min_dist = self.radius + other.radius

        if dist == 0 or dist >= min_dist:
            return  # no overlap (or perfectly coincident — skip)

        # Unit normal pointing from other → self
        nx = dx / dist
        ny = dy / dist

        # Separate the circles so they are exactly touching
        overlap = min_dist - dist
        self.x  += nx * overlap / 2
        self.y  += ny * overlap / 2
        other.x -= nx * overlap / 2
        other.y -= ny * overlap / 2

        # Relative velocity projected onto the normal
        # For equal masses, the normal components are simply swapped.
        v1n = self.vx * nx + self.vy * ny
        v2n = other.vx * nx + other.vy * ny

        # Only resolve if the balls are moving toward each other
        if v1n - v2n >= 0:
            return

        # Exchange normal-component velocities (elastic, equal mass)
        delta = v1n - v2n
        self.vx  -= delta * nx
        self.vy  -= delta * ny
        other.vx += delta * nx
        other.vy += delta * ny

    def draw(self) -> None:
        pg.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)
