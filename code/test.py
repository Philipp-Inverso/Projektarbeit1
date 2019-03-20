import RPi.GPIO as GPIO
import time

dataPin  = 11
latchPin = 13
clockPin = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(dataPin,  GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT)
GPIO.setup(clockPin, GPIO.OUT)
GPIO.output(latchPin, GPIO.LOW)
GPIO.output(clockPin, GPIO.LOW)
GPIO.output(dataPin, GPIO.LOW)

#0x00, 0x00,
#0b11111100,
#0b00010010,
#0b00010010,
#0b11111100,
#0x00, 0x00,

for j in range(0,500):
    x = 0xc0 >> 2
    for i in range(0,8):
        GPIO.output(clockPin, GPIO.LOW)
        GPIO.output(dataPin, (1 & 0b11111100 >> i) == 1 and GPIO.HIGH or GPIO. LOW)
        GPIO.output(clockPin, GPIO.HIGH)
    for i in range(0,8):
        GPIO.output(clockPin, GPIO.LOW)
        GPIO.output(dataPin, (1 & ~x >> i) == 1 and GPIO.HIGH or GPIO. LOW)
        GPIO.output(clockPin, GPIO.HIGH)
    GPIO.output(latchPin, GPIO.HIGH)
    time.sleep(0.001)
    x>>=1
    GPIO.output(latchPin, GPIO.LOW)
    time.sleep(0.001)
    for i in range(0,8):
        GPIO.output(clockPin, GPIO.LOW)
        GPIO.output(dataPin, (1 & 0b00010010 >> i) == 1 and GPIO.HIGH or GPIO. LOW)
        GPIO.output(clockPin, GPIO.HIGH)
    for i in range(0,8):
        GPIO.output(clockPin, GPIO.LOW)
        GPIO.output(dataPin, (1 & ~x >> i) == 1 and GPIO.HIGH or GPIO. LOW)
        GPIO.output(clockPin, GPIO.HIGH)
    GPIO.output(latchPin, GPIO.HIGH)
    time.sleep(0.001)
    x>>=1
    GPIO.output(latchPin, GPIO.LOW)
    for i in range(0,8):
        GPIO.output(clockPin, GPIO.LOW)
        GPIO.output(dataPin, (1 & 0b00010010 >> i) == 1 and GPIO.HIGH or GPIO. LOW)
        GPIO.output(clockPin, GPIO.HIGH)
    for i in range(0,8):
        GPIO.output(clockPin, GPIO.LOW)
        GPIO.output(dataPin, (1 & ~x >> i) == 1 and GPIO.HIGH or GPIO. LOW)
        GPIO.output(clockPin, GPIO.HIGH)
    GPIO.output(latchPin, GPIO.HIGH)
    time.sleep(0.001)
    x>>=1
    GPIO.output(latchPin, GPIO.LOW)
    for i in range(0,8):
        GPIO.output(clockPin, GPIO.LOW)
        GPIO.output(dataPin, (1 & 0b11111100 >> i) == 1 and GPIO.HIGH or GPIO. LOW)
        GPIO.output(clockPin, GPIO.HIGH)
    for i in range(0,8):
        GPIO.output(clockPin, GPIO.LOW)
        GPIO.output(dataPin, (1 & ~x >> i) == 1 and GPIO.HIGH or GPIO. LOW)
        GPIO.output(clockPin, GPIO.HIGH)
    GPIO.output(latchPin, GPIO.HIGH)
    time.sleep(0.001)
    x>>=1
    GPIO.output(latchPin, GPIO.LOW)

GPIO.cleanup()