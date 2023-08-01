import time
import gcode_serial
import serial
import scipy.io as sio
from pylibftdi import BitBangDevice

device_address = 'ftdi://ftdi:232h/1'
device = BitBangDevice(device_address)
device.port = BitBangDevice.SPI

def main():
    vitesse = 1
    pas_horizontal = 0.5
    pas_vertical = 2
    com_port = input("Entrez le nom du port COM USB: ")
    radar_port = input("Entrez le nom du port COM radar: ")
    radar_file = input("Entrez le chemin du fichier contenant les commandes du radar: ")
    movment(vitesse, pas_horizontal, pas_vertical, com_port, radar_port, radar_file)

def movment(v, p_horizontal, p_vertical, com_port, radar_port, radar_file):
    ser=gcode_serial.serial_open() #Port COM3 Par defaut
    gcode_serial.command(ser,"G28 X0 Y0 Z0\r\n")
    h = 0

    while True:  
        for i in range(0, 200, p_horizontal):
            gcode_serial.command(ser,f"G01 X{i} Y0 Z{h} F{v}\r\n")
            config_radar(radar_port, radar_file)

            # Récupérer les données du radar
            spi_data = []
            while device.in_waiting:  # tant qu'il y a des données disponibles
                bytes_data = device.read(4)
                num = int.from_bytes(bytes_data, byteorder='big')
                spi_data.append(num)
                
            # Écrire les données dans un fichier .mat
            sio.savemat(f"data_{i}_{h}.mat", {'data': spi_data})

            time.sleep(1)
            stop_sensor(radar_port)

        h += p_vertical
        gcode_serial.command(ser,f"G01 X200 Y0 Z{h} F{v}\r\n")
        time.sleep(1) 

        for i in range(200, 0, -p_horizontal):
            gcode_serial.command(ser,f"G01 X{i} Y0 Z{h} F{v}\r\n")
            config_radar(radar_port, radar_file)

            # Récupérer les données du radar
            spi_data = []
            while device.in_waiting:  # tant qu'il y a des données disponibles
                bytes_data = device.read(4)
                num = int.from_bytes(bytes_data, byteorder='big')
                spi_data.append(num)
                
            # Écrire les données dans un fichier .mat
            sio.savemat(f"data_{i}_{h}.mat", {'data': spi_data})

            time.sleep(1)
            stop_sensor(radar_port)

        h += p_vertical
        gcode_serial.command(ser,f"G01 X0 Y0 Z{h} F{v}\r\n")
        time.sleep(1)  

        if h<=198:
            break

    gcode_serial.serial_close(ser)

def config_radar(radar_port, radar_file):
    with serial.Serial(radar_port, 115200, timeout=1) as ser_radar, open(radar_file, 'r') as f:
        for line in f:
            command = line.strip()
            ser_radar.write(command.encode() + b"\r\n")

def stop_sensor(radar_port):
    with serial.Serial(radar_port, 115200, timeout=1) as ser_radar:
        command="sensorStop"
        ser_radar.write(command.encode() + b"\r\n")

main()