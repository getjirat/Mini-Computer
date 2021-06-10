input.onButtonPressed(Button.A, function () {
    Current_Screen_Selection += -1
})
input.onButtonPressed(Button.B, function () {
    Current_Screen_Selection += 1
})
let Current_Screen_Selection = 1
basic.forever(function () {
    if (Current_Screen_Selection == 1) {
        basic.showString("Compass Screen")
    }
})
