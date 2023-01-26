#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import struct
import random


# Create your objects here.
ev3 = EV3Brick()
height_motor = Motor(Port.C)
syringe_motor = Motor(Port.B)
rotate_motor = Motor(Port.A)
mix_motor = Motor(Port.D)
ev3.speaker.set_volume(100, which='_all_')

syringe = Syringe()
robot = Killswitch()
rotate_arm = RotateArm()
sound = Sound()
mixer = Mixer()
height_arm = HeightArm()


#PS4 connection
infile_path = "/dev/input/event4"
in_file = open(infile_path, "rb")


# Define the format the event data will be read
# See https://docs.python.org/3/library/struct.html#format-characters for more details
FORMAT = 'llHHi'
EVENT_SIZE = struct.calcsize(FORMAT)
event = in_file.read(EVENT_SIZE)

        

# Create a loop to react to events
while event:

    # Place event data into variables
    # In C (the programming language), a struct is a data type which takes different variables 
    # and places them under one name and one memory block. 
    # The input from the PS4 controller is sent as structs, compact groups of information. Therefore, 
    # in order to use the data from the input, it has to be converted to Python. The unpack method takes the struct from
    # event, which is the controller input, and uses the compact data to define the variables given: (tv_sec, tv_usec, ev_type, code, value).
    (tv_sec, tv_usec, ev_type, code, value) = struct.unpack(FORMAT, event)

    # If a button was pressed or released
    if ev_type == 1:
        
        syringe.move(code)
        height_arm.move(code)
        rotate_arm.move(code)
        mixer.mix(code)
        sound.play(code)
        robot.turn_off(code)
    
    
        

        #elif code == 318:
         #   if value == 1:
          #      mix_motor.run(0)
           #     rotate = ev3.get_motor_encoder(ev3.rotate_motor) # reads rotate_motor position
            #    height = ev3.get_motor_encoder(ev3.height_motor) # reads height_motor position       
        
        #elif code == 317:
         #   if value == 1:
          #      ev3.set_motor_position(ev3.rotate_motor, rotate)
           #     ev3.set_motor_position(ev3.height_motor, height)


    # Read the next event
    event = in_file.read(EVENT_SIZE)

in_file.close()



