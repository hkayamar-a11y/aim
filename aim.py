import time
import random
import pyautogui
import vgamepad as vg

pyautogui.FAILSAFE = False
g = vg.VX360Gamepad()


def m(x, y):
    cx, cy = pyautogui.position()
    s = random.randint(15, 30)
    for i in range(s + 1):
        p = i / s
        e = p * p * (3 - 2 * p)
        pyautogui.moveTo(
            cx + (x - cx) * e + random.uniform(-1, 1),
            cy + (y - cy) * e + random.uniform(-1, 1),
        )
        time.sleep(random.uniform(0.005, 0.015))


def b(btn, d=None):
    g.press_button(btn)
    g.update()
    time.sleep(d if d else random.uniform(0.08, 0.15))
    g.release_button(btn)
    g.update()
