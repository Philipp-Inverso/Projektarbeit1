from tkinter import messagebox
import RPi.GPIO as GPIO
import UserInterface
import main
import time


def shiftout(dPin, cPin, direction, val):
#Shift data into registers#
    
    for i in range(0,8):
        GPIO.output(cPin, GPIO.LOW)
        if (direction == 'N'):
            GPIO.output(dPin, (0x80 & (val<<i) == 0x80) and GPIO.HIGH or GPIO.LOW) ## displayRunningText Rightwards
        elif (direction == 'J'):
            GPIO.output(dPin, (0x01 & (val>>i) == 0x01) and GPIO.HIGH or GPIO.LOW) ## displayRunningText Leftwards
        GPIO.output(cPin, GPIO.HIGH)
        
def mirror(x):
    mirror = UserInterface.entryMirror.get().upper()
    if x:
        if mirror == 'J': return('N')
        else: return('J')
    else:
        if mirror == 'J': return('J')
        else: return('N')
        
def displayText(static, data):
    
    if not static: #display running text
        for k in range(0,len(data)-8):
            for j in range(0,main.RadioVars.speed.get()):
                x=0x80
                for i in range(k,k+8):
                    GPIO.output(main.LATCHPIN(),GPIO.LOW)
                    shiftout(main.DATAPIN(),main.CLOCKPIN(),mirror(0),data[i])
                    shiftout(main.DATAPIN(),main.CLOCKPIN(),mirror(1),~x)
                    GPIO.output(main.LATCHPIN(),GPIO.HIGH)
                    time.sleep(0.001)
                    x>>=1
    else: #display static text
        for j in range(0,500):
            x=0x80
            for i in range(0,8):
                GPIO.output(main.LATCHPIN(),GPIO.LOW)
                shiftout(main.DATAPIN(),main.CLOCKPIN(),mirror(0),data[i])
                shiftout(main.DATAPIN(),main.CLOCKPIN(),mirror(1),~x)
                GPIO.output(main.LATCHPIN(),GPIO.HIGH)
                time.sleep(0.001)
                x>>=1  
            
def getText(charset):
    data = []
    args = []
    letters = []
    text = UserInterface.entryText.get()
    UserInterface.entryText.delete(0,'end')
    for letter in text:
        try:
            args.append(charset[letter][1])
        except KeyError:
            messagebox.showwarning("Warning",letter+" is not included in the charsacterset")
            args = []
            break
    index = len(args)

    if main.RadioVars.static.get():
        data=args[0][8:16]
        #cut off leading and last 8 zeros
        displayText(1, data)
    else:
        if (len(args) == 1):
            data=(args[0])
            #don't cut
            displayText(0, data)
            
        elif(len(args) >= 2):
            data=(args[0][0:14])
            #cut last 10 zeros
            for i in range(1,index-1):
                data.extend(args[i][8:14])
                #cut leading 8 and last 10 zeros
            data.extend(args[index-1][8:])
            #cut leading 8 zeros
            displayText(0, data)