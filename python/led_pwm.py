#parancsok:
#   1) led pwm kitoltesi tenyetojenek allitasa:           led_setpwm:xxx
#       harom szamjegy kiirasa kotelezo xxx -> 000-100
#   2) program leallitasa:                                led_shutdown
#       szabalyos ujrainditas es leallitas eseten erossen ajanlott

import threading
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) #led init
GPIO.setup(16, GPIO.OUT) #16. pin

lock = threading.Lock()

led_active = True #restart, shut down eseten Falsra allitando
led_pwm = 0 #kitoltesi tenyezo

def read_cmd(): #command line input folyamatos olvasasa
    global led_active, led_pwm
    while led_active:
        cmd = input()
        if cmd[0:11] == 'led_setpwm:': #1. parancs
            print(cmd[0:11])
            lock.acquire()
            led_pwm = int(cmd[11:14])
            print('led pwm was set to: ' + str(led_pwm) + '%')
            lock.release()
        if cmd == 'led_shutdown': #2. parancs
            lock.acquire()
            led_active = False
            lock.release()
        

thread = threading.Thread(target=read_cmd)
thread.start()

while led_active: #led vezerlese
    if led_pwm > 0:
        GPIO.output(16, GPIO.HIGH)
        time.sleep(led_pwm/100000.0) #us pwm
    if led_pwm < 100:
        GPIO.output(16, GPIO.LOW)
        time.sleep((100-led_pwm)/100000.0)

thread.join()
GPIO.cleanup()
print('led_pwm program was shouted down.')