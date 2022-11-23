import serial
import time
import pyautogui

time.sleep(2)
ser = serial.Serial("COM6", 9600, timeout=1)
while ser.is_open:
    valorSerial = str(ser.readline())
    numero = 0

    if not(len(valorSerial) < 4):
        numero = float(valorSerial[2:6])

        if numero >= 0.1 and numero <= 0.2:
            pyautogui.press('right')
        elif numero > 0.2 and numero <= 0.3:
            pyautogui.press('left')
        if numero > 0.3 and numero <= 0.4:
            pyautogui.press('up')
        elif numero > 0.4 and numero <= 0.5:
            pyautogui.press('down')
    else:
        print(valorSerial)    

        print('Señal recibida: ' + str(numero) + ' mV')
        time.sleep(1)
