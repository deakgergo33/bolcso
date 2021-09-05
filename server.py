from flask import Flask, render_template, url_for
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time
import RPi.GPIO as GPIO
import threading



app = Flask(__name__)

#region [Region] variables
success_response = 'success'
fail_response = 'error'

#led control variables
led_pwm = 0
previous_value = 0
#endregion

#region [Region] View loader endpoints

@app.route('/')
def indexView():
    url_for('static', filename='js/round-slider.js')
    url_for('static', filename='js/index.js')
    return render_template('index.html')

@app.route('/stream')
def streamView():
    return render_template('stream.html')

@app.route('/gallery')
def galleryView():
    return render_template('gallery.html')

#endregion

#region [Region] Controllers

@app.route("/intensity/<percent>")
def setLightIntensity(percent):
    global led_pwm
    global previous_value
    previous_value = int(percent)
    led_pwm = int(percent)
    return success_response

#endregion

#region [Region] LED
GPIO.setmode(GPIO.BCM) #led init
GPIO.setup(16, GPIO.OUT) #16. pin

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

counter = 0
timer_on = False

def led_control():
    #led vezerlese
    while True:
        if led_pwm > 0:
            GPIO.output(16, GPIO.HIGH)
            time.sleep(led_pwm/100000.0) #us pwm
        if led_pwm < 100:
            GPIO.output(16, GPIO.LOW)
            time.sleep((100-led_pwm)/100000.0)

def adc_control():
    global previous_value
    global led_pwm
    global counter
    global timer_on
    while True:
        chan = AnalogIn(ads, ADS.P0)
        value = int(chan.value/325)

        if ((previous_value >= value + 2) or (previous_value <= value - 2) or (value == 1)) and not timer_on:
            print(value)
            led_pwm = value
            previous_value = value
            timer_on = True
        elif timer_on:
            if (previous_value <= value + 1) or (previous_value >= value - 1):
                if previous_value != value:
                    print(value)
                    led_pwm = value
                    previous_value = value
                counter+=1
            else:
                print(value)
                led_pwm = value
                previous_value = value
                counter = 0
            if counter > 40:
                counter = 0
                timer_on = False

        time.sleep(0.05)

thread1 = threading.Thread(target = led_control)
thread2 = threading.Thread(target = adc_control)
thread1.start()
thread2.start()
#endregion
