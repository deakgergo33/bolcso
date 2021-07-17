#import RPi.GPIO as GPIO
#import lgpio
import time
from gpiozero.output_devices import LED
import keyboard

#h = lgpio.gpiochip_open(0)
#lgpio.gpio_claim_output(h, 16)

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(16, GPIO.OUT)
led = LED(16)

x = False
y = False
pwm_kitoltes = 0

def PWM(kitoltesi_ido):
    if kitoltesi_ido > 0:
        #GPIO.output(16, GPIO.HIGH)
        #lgpio.gpio_write(h, 16, 1)
        led.on()
        time.sleep(kitoltesi_ido/100000.0)
    if kitoltesi_ido < 100:
        #GPIO.output(16, GPIO.LOW)
        #lgpio.gpio_write(h, 16, 0)
        led.off()
        time.sleep((100-kitoltesi_ido)/100000.0)

def Novel():
    global x
    global pwm_kitoltes
    if x == False and keyboard.is_pressed('o'):
        if pwm_kitoltes < 100:
            pwm_kitoltes += 5
            print(pwm_kitoltes)
        x = True
    if not(keyboard.is_pressed('o')):
        x = False

def Csokkent():
    global y
    global pwm_kitoltes
    if y == False and keyboard.is_pressed('l'):
        if pwm_kitoltes > 0:
            pwm_kitoltes -= 5
            print(pwm_kitoltes)
        y = True
    if not(keyboard.is_pressed('l')):
        y = False

while not(keyboard.is_pressed('e')):
    Csokkent()
    Novel()
    PWM(pwm_kitoltes)

#GPIO.cleanup()
#lgpio.gpiochip_close(h)
    
        