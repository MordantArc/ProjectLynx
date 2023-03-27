import time
from machine import Pin, PWM

test_param = 'test'

def accelerating_pinout(pin_no=type(int)):
    led = Pin(pin_no, Pin.OUT)
    for x in range(2,76):
        led.on()
        time.sleep(1/x)
        led.off()
        time.sleep(1/x)

def tic(buzzer_pin=None):
    if buzzer_pin!=None:
        bzr = Pin(buzzer_pin,Pin.OUT)
        leds = Pin('LED',Pin.OUT)
        bzr.on()
        leds.on()
        time.sleep(0.00000000001)
        bzr.off()
        leds.off()
    else:
        leds = Pin('LED',Pin.OUT)
        leds.on()
        time.sleep(0.00000000001)
        leds.off()

if __name__ == '__main__':
    while True:
        accelerating_pinout(25)