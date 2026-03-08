import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap

keyboard = KMKKeyboard()

# Enable macros
macros = Macros()
keyboard.modules.append(macros)

# GPIOs wired to buttons (order matters)
PINS = [
    board.D3,   # Button1
    board.D4,   # Button2
    board.D2,   # Button3
    board.D1,   # Button4
    board.D10,   # Button5
    board.A1,   # Button6
    board.D9,   # Button7
    board.A3,   # Button8
    board.D0,   # Button9
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# ---- MACROS ----
COPY = KC.Macro(
    Press(KC.LCMD),
    Tap(KC.C),
    Release(KC.LCMD),
)

PASTE = KC.Macro(
    Press(KC.LCMD),
    Tap(KC.V),
    Release(KC.LCMD),
)

SPOTLIGHT = KC.Macro(
    Press(KC.LCMD),
    Tap(KC.SPACE),
    Release(KC.LCMD),
)

# ---- KEYMAP (9 buttons) ----
keyboard.keymap = [
    [
        COPY,                   # Button1
        PASTE,                  # Button2
        SPOTLIGHT,              # Button3
        KC.MEDIA_PLAY_PAUSE,    # Button4
        KC.C,                   # Button5
        KC.R,                   # Button6
        KC.L,                   # Button7
        KC.E,                   # Button8
        KC.NO,                  # Button9 (unused for now)
    ]
]

if __name__ == '__main__':
    keyboard.go()
