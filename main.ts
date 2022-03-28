radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        pins.digitalWritePin(DigitalPin.P1, 0)
    } else if (receivedNumber == 1) {
        pins.digitalWritePin(DigitalPin.P1, 1)
    } else if (receivedNumber == 2) {
        pins.digitalWritePin(DigitalPin.P0, 0)
    } else if (receivedNumber == 3) {
        pins.digitalWritePin(DigitalPin.P0, 1)
    }
})
radio.setGroup(1)
basic.forever(function () {
	
})
