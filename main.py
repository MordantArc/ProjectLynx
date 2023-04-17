from flashlight import *
from parameters import *
import time
from machine import Pin, PWM, SPI
import os

"""
[][]
"""

#IMPORTANT! SITL MUST BE OFF BEFORE FLIGHT!
sitl = False


tickRate = 10 #hertz. How many times per second a dataset is logged.

master_state='START'

active_pins = []
active_servos = []

def terminal(string=type(str)):
    global recordData
    print(string)
    if recordData['state'] and recordData['dir'] != None:
        with open(recordData['dir'],'a') as file:
            file.write(string)
    tic()

def get_pwm(input): # -100 to 100, floats ok
    input += 100 # 0 to 200
    input=(input/200) # 0 to 1, !! FLOAT !!
    input*=servo_throw
    input+=(1000+(servo_max_lims-servo_throw)/2)
    print(input)
    return int(round(input,0))

def start_func():
    terminal('\n\nINIT\n\n')
    accelerating_pinout(onboard_LED)
    if silent == False:
        accelerating_pinout(buzzer)
    for x in servoList:
        tmp2 = PWM(Pin(x[1]))
        active_pins.append(tmp2)
        active_servos.append(tmp2)
        tmp2.freq(50) # 50hz
        tmp2.duty_u16(get_pwm(-100)) # full on
        time.sleep(0.3)
        tmp2.duty_u16(get_pwm(100)) # full off
        time.sleep(0.3)
        tmp2.duty_u16(get_pwm(0)) # middle
        terminal('\n\nStart Functions Complete.')

def data_frequency_return_rate_test(length):
    length = round(1/length,9)
    length_ms = int(round(length*1000,0))
    length_us = int(round(length*1000000,0))

    terminal('\n\nINIT DATA FREQUENCY TEST MILLISECONDS\n')
    t=time.ticks_ms()
    time.sleep_ms(length_ms)
    ta=time.ticks_ms()
    terminal(f'Should be {length_ms} and result is {ta-t}\n')
    ms_fini = (length_ms, ta-t)

    terminal('\n\nINIT DATA FREQUENCY TEST MICROSECONDS\n')
    t=time.ticks_us()
    time.sleep_us(length_us)
    ta=time.ticks_us()
    terminal(f'Should be {length_us} and result is {ta-t}\n')
    us_fini = (length_us, ta-t)

    terminal(f'\nMillisecond %-error is:{round((ms_fini[1]-ms_fini[0])/ms_fini[0],5):10}% |\n')
    terminal(f'\nMicrosecond %-error is:{round((us_fini[1]-us_fini[0])/us_fini[0],5):10}% |\n')

def end_connections():
    for x in active_pins:
        try:
            x.off()
        except AttributeError:
            pass
        
def get_next_state(cur):
    next = list_of_states[1+list_of_states.index(cur)]
    return next

if __name__ == '__main__':
    while True:
        if master_state == 'START':
            start_func()
            master_state=get_next_state('START')
        """
        #Base State example
        if master_state == '99':
            do_stuff()
        """
        if master_state == 'STOP':
            end_connections()
            print('\n---\nEoF\n---\n')
