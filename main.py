Current_Screen_Selection = 0

def on_button_pressed_a():
    global Current_Screen_Selection
    Current_Screen_Selection += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
