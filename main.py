radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 2) {
        NPNLCD.on()
    } else if (receivedNumber == 3) {
        NPNLCD.off()
    } else if (receivedNumber == 4) {
        NPNBitKit.Buzzer(DigitalPin.P4, true)
    } else if (receivedNumber == 5) {
        NPNBitKit.Buzzer(DigitalPin.P4, false)
    }
})
function LCD () {
    NPNLCD.clear()
    NPNLCD.ShowString("\"people in room\"", 0, 0)
    NPNLCD.ShowNumber(count_people, 0, 1)
}
function IR_sensor () {
    if (pins.digitalReadPin(DigitalPin.P2) == 0) {
        NPNBitKit.Led2Color(DigitalPin.P1, true, DigitalPin.P6, false)
    } else {
        NPNBitKit.Led2Color(DigitalPin.P1, false, DigitalPin.P6, false)
    }
}
function Magnetic_in () {
    if (NPNBitKit.ButtonDoorOpen(DigitalPin.P5)) {
        count_people += count_people + 1
        if (count_people > 10) {
            NPNBitKit.Buzzer(DigitalPin.P4, true)
            basic.pause(5000)
        }
    }
}
function Magnetic_out () {
    if (NPNBitKit.ButtonDoorOpen(DigitalPin.P6)) {
        count_people += count_people - 1
    }
}
let count_people = 0
radio.setGroup(1)
count_people = 0
NPNLCD.LcdInit()
NPNLCD.ShowString("\" Welcome to my room\"", 0, 0)
basic.forever(function () {
    IR_sensor()
    Magnetic_in()
    Magnetic_out()
    LCD()
})
