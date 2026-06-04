import serial
import time

PORT = "/dev/cu.usbmodem1101"  
BAUD = 115200

ser = serial.Serial(PORT, BAUD)
time.sleep(2)  

with open("data/samples.txt", "w") as f:
    while True:
        try:
            line = ser.readline().decode("utf-8", errors="ignore").strip()
            if line:
                print(line)
                f.write(line + "\n")
        except KeyboardInterrupt:
            print("Stopped.")
            break

ser.close()