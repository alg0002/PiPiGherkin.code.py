#PiPi-GHERKIN - Raspberry Pi PICO
import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    row_pins = (board.GP8, board.GP9, board.GP10, board.GP11, board.GP12)
    col_pins = (
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7
    )
    diode_orientation = DiodeOrientation.COLUMNS
    debug_enabled = False