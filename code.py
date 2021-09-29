#PiPi-GHERKIN - Raspberry Pi PICO
import board
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.hid import HIDModes
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap

gherkin = KMKKeyboard()
gherkin.modules.append(Layers())
gherkin.modules.append(ModTap())

gherkin.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)
gherkin.row_pins = (board.GP8, board.GP9, board.GP10, board.GP11, board.GP12)

gherkin.diode_orientation = DiodeOrientation.COLUMNS

gherkin.debug_enabled = False

gherkin.keymap = [
    [#L0
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,
        KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.ENT,
        KC.MT(KC.Z, KC.LCTRL),
                 KC.MT(KC.X, KC.LALT),
                          KC.LT(3, KC.C),
                                   KC.LT(4, KC.V),
                                            KC.LT(2, KC.B),
                                                     KC.LT(1, KC.N),
                                                              KC.LT(5, KC.M),
                                                                       KC.MT(KC.SPC, KC.RALT),
                                                                                KC.MT(KC.BSPC, KC.RCTRL),
                                                                                         KC.MT(KC.ESC, KC.RSFT),
    ],
    [#L1
        KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,
        KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.DEL,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ],
    [#L2
        KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC, KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,
        KC.F11,  KC.F12,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.GRV,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ],
    [#L3
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MINS, KC.EQL,  KC.LBRC, KC.RBRC, KC.BSLS,
        KC.TAB,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.COMM, KC.DOT,  KC.SLSH, KC.SCLN, KC.QUOT,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT,
    ],
    [#L4
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.UNDS, KC.PLUS, KC.LCBR, KC.RCBR, KC.PIPE,
        KC.TAB,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.LABK, KC.RABK, KC.QUES, KC.COLN, KC.DQUO,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.HOME, KC.PGDN, KC.PGUP, KC.END,
    ],
    [#L5
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MHEN, KC.TRNS, KC.HENK, KC.TRNS, KC.TRNS,
    ],
]

if __name__ == '__main__':
    gherkin.go(hid_type=HIDModes.USB) #Wired USB enable