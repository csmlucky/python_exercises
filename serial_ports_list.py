###########################################################################
# This Script lists the avilble serial port names
############################################################################

import serial
import serial.tools.list_ports


ports = serial.tools.list_ports.comports()
for port in ports:
    print(f"port:{port}")
    print(f"port-name:{port.device}")