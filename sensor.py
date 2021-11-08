import RPi.GPIO as GPIO
import time
 
buzzer = 16
trig = 11
echo = 12
LED_RED = 29
LED_GREEN = 31

print('start') 
 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
GPIO.setup(buzzer,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.setup(LED_RED, GPIO.OUT, initial = GPIO.LOW) #ㅊㅗㄱㅣㄱㅏㅂㅅ ㅅㅓㄹㅈㅓㅇ
GPIO.setup(LED_GREEN, GPIO.OUT, initial = GPIO.LOW)

try:
    GPIO.output(buzzer, False)
    while(True):
        GPIO.output(trig, False)
        time.sleep(0.5)
        
        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)
        
        while GPIO.input(echo) == 0:
            pulse_start = time.time()
            
        while GPIO.input(echo) == 1:
            pulse_end = time.time()
        
        GPIO.output(buzzer, False)
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)
        print('Distance : ', distance,'cm')
        
        if distance <= 10:
            print('Warning!!!')
            GPIO.output(buzzer, GPIO.HIGH)
            GPIO.output(LED_GREEN,GPIO.HIGH)
            GPIO.output(LED_RED, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(buzzer, GPIO.LOW)
            
        else:                                                               
            GPIO.output(LED_GREEN,GPIO.LOW)
            GPIO.output(LED_RED, GPIO.LOW)
            time.sleep(0.5)
except:
    GPIO.cleanup()
