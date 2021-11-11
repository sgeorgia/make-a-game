let score_a = 0
input.onButtonPressed(Button.A, function () {
    basic.showNumber(score_a)
    score_a = 1
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(score_a)
    score_a = 3
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(score_a)
    score_a += 2
})
input.onGesture(Gesture.Shake, function () {
    score_a = 0
})
basic.forever(function () {
    if (score_a > 15) {
        basic.showString("winner")
    }
})
