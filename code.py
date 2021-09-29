#PiPi-GHERKIN - Raspberry Pi PICO
import board
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.hid import HIDModes
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap

keyboard = KMKKeyboard()

modtap = ModTap()
layers_ext = Layers()
keyboard.modules = [layers_ext, modtap]

keyboard.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)
keyboard.row_pins = (board.GP8, board.GP9, board.GP10, board.GP11, board.GP12)

keyboard.diode_orientation = DiodeOrientation.COLUMNS

keyboard.debug_enabled = False

# Cleaner key names
_______ = KC.TRNS

CTL_Z = KC.MT(KC.Z, KC.LCTRL)
ALT_X = KC.MT(KC.X, KC.LALT)
LT3_C = KC.LT(3, KC.C)
LT4_V = KC.LT(4, KC.V)
LT2_B = KC.LT(2, KC.B)
LT1_N = KC.LT(1, KC.N)
LT5_M = KC.LT(5, KC.M)
ALT_SPC = KC.MT(KC.SPC, KC.RALT)
CTL_BS = KC.MT(KC.BSPC, KC.RCTRL)
SFT_ESC = KC.MT(KC.ESC, KC.RSFT)

keyboard.keymap = [
    [
        # Layer 0
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,
        KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.ENT,
        CTL_Z,   ALT_X,   LT3_C,   LT4_V,   LT2_B,   LT1_N,   LT5_M,   ALT_SPC, CTL_BS,  SFT_ESC,
    ],
    [
        # Layer 1
        KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,
        KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,
        _______, _______, _______, _______, KC.DEL,  _______, _______, _______, _______, _______,
    ],
    [
        # Layer 2
        KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC, KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,
        KC.F11,  KC.F12,  _______, _______, _______, _______, _______, _______, _______, KC.GRV,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
    ],
    [
        # Layer 3
        _______, _______, _______, _______, _______, KC.MINS, KC.EQL,  KC.LBRC, KC.RBRC, KC.BSLS,
        KC.TAB,  _______, _______, _______, _______, KC.COMM, KC.DOT,  KC.SLSH, KC.SCLN, KC.QUOT,
        _______, _______, _______, _______, _______, _______, KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT,
    ],
    [
        # Layer 4
        _______, _______, _______, _______, _______, KC.UNDS, KC.PLUS, KC.LCBR, KC.RCBR, KC.PIPE,
        KC.TAB,  _______, _______, _______, _______, KC.LABK, KC.RABK, KC.QUES, KC.COLN, KC.DQUO,
        _______, _______, _______, _______, _______, _______, KC.HOME, KC.PGDN, KC.PGUP, KC.END,
    ],
    [
        # Layer 5
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, KC.MHEN, _______, KC.HENK, _______, _______,
    ],
]

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.USB) #Wired USB enable