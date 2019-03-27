import UserInterface
import RPi.GPIO as GPIO
import PIL.ImageDraw
import PIL.Image
import Factory
import math
import os

def DATAPIN():  return 11
def LATCHPIN(): return 13
def CLOCKPIN(): return 15
def PATH(): return os.getcwd()

class RadioVars:
    static = Factory.IntVar()
    speed = Factory.IntVar()
        

#class Characterset(object):
chars = {} #TypeDictionary = {'Key': Value}

def createDictionary():
    
    for item in os.listdir(PATH()):
        if (item[-3:]).lower() == 'png':
            
            chars[item.split('.')[0]] = [PIL.Image.open(item), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
            """initialize dictionary with Key = 1st letter of item
               value = [TypePicture, values of columns]
               initialize columns value with 0"""
            
            for ix in range(0,8):
                x = ix * 100 + 100
                for iy in range(9,1,-1):
                    y = iy * 100 - 100
            #iterate coordinates
                    r,g,b = chars[item.split('.')[0]][0].getpixel((x,y))
                    if (r == 0 and g == 0 and b == 0):
                        chars[item.split('.')[0]][1][ix+8] += int(math.pow(2,(iy-2)))
                    #else: print ('weiss')
    #return chars

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DATAPIN(),  GPIO.OUT)
    GPIO.setup(LATCHPIN(), GPIO.OUT)
    GPIO.setup(CLOCKPIN(), GPIO.OUT)
    RadioVars.static.set(0)
    RadioVars.speed.set(10)
    createDictionary()
    
def destroy():
    Factory.UI.destroy()
    GPIO.cleanup()

if __name__=='__main__':
    #try:
        init()
        #print(chars['a'][1])
        UserInterface.createInterface(chars)
        UserInterface.Factory.UI.mainloop()
    #except: destroy()
