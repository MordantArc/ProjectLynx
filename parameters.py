#--- ONLY FOR PARAMETERS AND VARIABLES. NO FUNCTIONS ---
#
#
#
#

recordData = {
    'state':False,
    'dir':None,
    'set_points':{
        'standard_tickrate_hz':75,
        'hotel':'trivago'
    }
}

onboard_LED = 25

buzzer = 22

silent = True

Output_Servo_vIn_one = 28
Output_Servo_PWM_one = 27 # 5B PWM channel

servoList=[(Output_Servo_vIn_one,Output_Servo_PWM_one)]

u16 = 65535

servo_throw = 4000
servo_max_lims = 8000

list_of_states=[
    'START',
    #'PASSTHROUGH',
    'STOP'
]
