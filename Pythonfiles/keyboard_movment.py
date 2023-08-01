import matplotlib as mp
import keyboard
import gcode_serial
import generator_gcode
import time

def main():
    ser=gcode_serial.serial_open()
    gcode_serial.command(ser,"G28 X0 Y0 Z0\r\n")
    x=[0]
    y=[0]
    z=[0]
    print("is ok")
    while True:
        # Wait for the next event.
        print("Deplacez vous avec les fleches (Esc pour sortir)")
        event = keyboard.read_event()
        
        try:
            if event.event_type == keyboard.KEY_DOWN and event.name in ["up","down","left","right"]:
                match event.name:
                    case "up":
                        if z[-1]<241:
                            z.append(z[-1]+5)
                            x.append(x[-1])
                            y.append(y[-1])
                            move(x,y,z,ser)
                    case "down":
                        if z[-1]>9:
                            z.append(z[-1]-5)
                            x.append(x[-1])
                            y.append(y[-1])
                            move(x,y,z,ser)
                    case "right":
                        if x[-1]<241:
                            x.append(x[-1]+5)
                            y.append(y[-1])
                            z.append(z[-1])
                            move(x,y,z,ser)
                    case "left":
                        if x[-1]>9:
                            x.append(x[-1]-5)
                            y.append(y[-1])
                            z.append(z[-1])
                            move(x,y,z,ser)
            elif event.event_type == keyboard.KEY_DOWN and event.name=="esc":
                print("fin de l'entree de commande")
                gcode_serial.serial_close(ser)
                break
            else:
                raise ValueError
        except ValueError:
            print("Wrong key on keyboard")
            continue

def move(x,y,z,ser):
    #time.sleep(1)
    print(x,y,z)
    gcode_serial.command(ser,generator_gcode.write_gcode(00,x,y,z))

if __name__=="__main__":
    main()