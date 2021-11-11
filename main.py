score_a = 0

def on_button_pressed_a():
    global score_a
    score_a = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global score_a
    score_a = score_a + 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global score_a
    score_a += 2
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global score_a
    score_a = 0
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    basic.show_number(score_a)
basic.forever(on_forever)
