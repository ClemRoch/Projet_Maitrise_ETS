import serial
import time
from datetime import datetime

def command(ser, command):
    ser.write(str.encode(command)) 
    time.sleep(1)

    while True:
        line = ser.readline()
        print(line)

        if line == b'ok\n':
            break


def serial_open(port="COM3",baud=115200):
    ser = serial.Serial(port, baud)
    time.sleep(2)
    return ser

def serial_close(ser):
    time.sleep(2)
    ser.close()

"""
ser=serial_open()
command(ser, "G28 X0 Y0 Z0\r\n")
time.sleep(1)
command(ser, "G0 X200 Y200\r\n")
command(ser, "G0 X50 Y50\r\n")
serial_close(ser)
"""
#command(ser, "G28 X0 Y0 Z0\r\n")
# command(ser, "G28 X0 Y0\r\n")
# command(ser, "G28 X0\r\n")
# command(ser, "G28 Y0\r\n")
# command(ser, "G28 Z0\r\n")

# Extruder Temp
# command(ser, "M104 S190 T0\r\n") #  start heating T0 to 190 degrees Celsius
# command(ser, "G28\r\n") # Home
# command(ser, "M109 S190 T0\r\n") # wait for T0 to reach 190 degrees before continuing with any other commands

# Bed Temp
# command(ser, "M140 S55\r\n") # heat bed to 50 degrees celsius but do not wait
# command(ser, "G28\r\n") # Home
# command(ser, "M190 S55\r\n") # wait for bed to heat to 50 degrees celsius and wait

# Fan
# command(ser, "M106 S255\r\n") # fan speed full
# command(ser, "M106 S127\r\n") # fan speed about half
# command(ser, "M106 S0\r\n") # turn off fan

# Set Units(does not seem to work on ender 5)
# command(ser, "G20\r\n") # inches
#command(ser, "G21\r\n") # millimeters

# Absolute Mode
#command(ser, "G90\r\n")

# Relative Mode
# command(ser, "G91 X10\r\n")

# Move
# command(ser, "G0 X7 Y18\r\n") # rapid motion but does not extrude material
#command(ser, "G0 X200 Y200\r\n") # rapid motion but does not extrude material ender 5 plus is 350 x 350
#command(ser, "G1 Z0.345 F500\r\n") # change layer
#command(ser, "G0 X50 Y50\r\n") # rapid motion but does not extrude material ender 5 plus is 350 x 350

