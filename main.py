import time
import pygame
import math
from circle import Circle

screen_size = (1000, 1000)

FRAMES = 1000

FPS = 25

show_working = False

# grid_scale = (screen_size[0] / grid_size[0], screen_size[1] / grid_size[1])

colour_grad = ((255, 0, 0), (0, 0, 255))

MAX_DEPTH = 8
MIN_DEPTH = 6

clock = pygame.time.Clock()

circles = [Circle([250, 250], 100, [30, 20]),
           Circle([300, 300], 50, [-10, -30]),
           Circle([100, 100], 50, [10, -30]),
           Circle([400, 400], 50, [50, -40])]

depth_colours = (
    (255, 0, 0),
    (200, 0, 0),
    (150, 0, 0),
    (100, 0, 0),
    (50, 0, 0),
    (25, 0, 0),
    (0, 25, 0),
    (0, 50, 0),
    (0, 100, 0),
    (0, 150, 0),
    (0, 200, 0),
    (0, 200, 255),
)

MAX_DEPTH = len(depth_colours) - 2


# (x-xpos)^2 +(y-ypos)^2 = r


def graph_func(pos):
    fx = 0
    for cir in circles:
        try:
            fx += 1 / (math.sqrt(((pos[0] - cir.circle_pos[0]) ** 2 + (pos[1] - cir.circle_pos[1]) ** 2)))
        except ZeroDivisionError:
            fx += 1
    return fx


screen = pygame.display.set_mode(screen_size)

f_indicator = True


def inCircle(x, y):
    return 0.04 < graph_func((x, y))


def testRect(x, y, w, h, depth, mode):
    if depth > MAX_DEPTH:
        return
    elif depth > MIN_DEPTH:
        # pygame.draw.rect(screen, depth_colours[depth], (x, y, w, h))

        in_circle = inCircle(x, y)
        recurse = False

        for i in ((x, y + h), (x + w, y), (x + w, y + h)):
            if inCircle(i[0], i[1]) != in_circle:
                recurse = True
                break

        if not recurse: return []

    if not mode:
        pygame.draw.rect(screen, depth_colours[depth], (x, y, w, h))

    if depth == MAX_DEPTH:
        screen.set_at((x, y), depth_colours[depth])

        return []

    if mode:
        testRect(x, y, int(w / 2) + 1, int(h / 2) + 1, depth + 1, mode)
        testRect(x + int(w / 2), y, int(w / 2) + 1, int(h / 2) + 1, depth + 1, mode)
        testRect(x, y + int(h / 2), int(w / 2) + 1, int(h / 2) + 1, depth + 1, mode)
        testRect(x + int(w / 2), y + int(h / 2), int(w / 2) + 1, int(h / 2) + 1, depth + 1, mode)
    else:
        return [(x, y, int(w / 2) + 1, int(h / 2) + 1),
                (x + int(w / 2), y, int(w / 2) + 1, int(h / 2) + 1),
                (x, y + int(h / 2), int(w / 2) + 1, int(h / 2) + 1),
                (x + int(w / 2), y + int(h / 2), int(w / 2) + 1, int(h / 2) + 1)]


def step_by_step(args, depth):
    new_args = []
    for i in args:
        new_args += testRect(i[0], i[1], i[2], i[3], depth, False)
    return new_args


for f in range(FRAMES):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((0, 0, 0))

    MIN_DEPTH = 5

    if not show_working:
        testRect(0, 0, screen_size[0], screen_size[1], 0, True)
    else:
        args = ((0, 0, screen_size[0], screen_size[1], 0),)
        for i in range(MAX_DEPTH):
            print(i)
            args = step_by_step(args, i)
            pygame.display.update()
            time.sleep(1)

    pygame.display.update()

    for c in circles:
        c.step(1 / FPS, screen_size)

    ms = clock.tick()

    print(f, '/', FRAMES, str(ms) + "ms")
