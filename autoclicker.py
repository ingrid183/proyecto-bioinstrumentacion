import serial
import time
import pyautogui

time.sleep(2)
ser = serial.Serial("COM7", 9600, timeout=1)
while ser.is_open:
    valorSerial = str(ser.read())
    numero = 0
    if len(valorSerial) == 4:
        # Valor del serial -> b'2'
        numero = int(valorSerial[2:3])
    
    if numero == 1:
        pyautogui.press('right')
    elif numero == 2:
        pyautogui.press('left')

    print(numero)
    time.sleep(1)