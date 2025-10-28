import serial
import time

def open_serial_port(port, baudrate, comtimeout, retries, delay):

    for tries in range(retries):
        try:
            ser = serial.Serial(port, baudrate, timeout= comtimeout)
            if ser.is_open:
                print(f"port {ser.portstr} is opened successfully")
                return ser
        except ser.SerialException as e:
            print(f"Attempt{tries}: Failed to open {port} ({e})")


    
    return None
