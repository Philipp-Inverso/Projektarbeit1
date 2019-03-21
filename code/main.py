import RPi.GPIO as GPIO
from tkinter import *
from tkinter import messagebox
import PIL.Image
import PIL.ImageDraw
import time
import math
import os

###__global Variables__###
dataPin  = 11
latchPin = 13
clockPin = 15

UI = Tk()
static = IntVar()
speed = IntVar()

path = os.getcwd()
chars = {} #TypeDictionary = {'Key': Value}
##########################

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(dataPin,  GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    static.set(0)
    speed.set(10)
    createDictionary()
    
def createDictionary():
    
    for item in os.listdir(path):
        if item[2:] == 'png':
            
            chars[item[0]] = [PIL.Image.open(item), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
            """initialize dictionary with Key = 1st letter of item
               value = [TypePicture, values of columns]
               initialize columns value with 0"""
            
            for ix in range(0,8):
                x = ix * 100 + 100
                for iy in range(9,1,-1):
                    y = iy * 100 - 100
            #iterate coordinates
                    r,g,b = chars[item[0]][0].getpixel((x,y))
                    if (r == 0 and g == 0 and b == 0):
                        chars[item[0]][1][ix+8] += (int(math.pow(2,(iy-2))))
                    #else: print ('weiss')
def destroy():
    UI.destroy()
    GPIO.cleanup()
    

def shiftout(dPin, cPin, direction, val):
#Shift data into registers#
    
    for i in range(0,8):
        GPIO.output(cPin, GPIO.LOW)
        if (direction == 'R'):
            GPIO.output(dPin, (0x80 & (val<<i) == 0x80) and GPIO.HIGH or GPIO.LOW) ## displayRunningText Rightwards
        elif (direction == 'L'):
            GPIO.output(dPin, (0x01 & (val>>i) == 0x01) and GPIO.HIGH or GPIO.LOW) ## displayRunningText Leftwards
        GPIO.output(cPin, GPIO.HIGH)
        
def displayText(static, data):
    direction = entryDirection.get()
    if not static: #display running text
        for k in range(0,len(data)-8):
            for j in range(0,speed.get()):
                x=0x80
                for i in range(k,k+8):
                    GPIO.output(latchPin,GPIO.LOW)
                    shiftout(dataPin,clockPin,'R',data[i])
                    shiftout(dataPin,clockPin,direction,~x)
                    GPIO.output(latchPin,GPIO.HIGH)
                    time.sleep(0.001)
                    x>>=1
    else: #display static text
        for j in range(0,500):
            x=0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                shiftout(dataPin,clockPin,'R',data[i])
                shiftout(dataPin,clockPin,'L',~x)
                GPIO.output(latchPin,GPIO.HIGH)
                time.sleep(0.001)
                x>>=1  
            
def getText():
    data=[]
    args=[]
    text = entryText.get()
    entryText.delete(0,END)
    for letter in text:
        try:
            args.append(chars[letter][1])
        except KeyError:
            messagebox.showwarning("Warning",letter+" is not included in the charsacterset")
            args = []
            break
    index = len(args)

    if static.get():
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
    

#############################__Interface__#############################
#variables#
UI.configure(bg = 'lightgreen')

entryDirection  = Entry(UI)
entryText = Entry(UI)
newCharacter = Entry(UI)
entryDirection.insert(12,'L')

class Checkbar(Frame):
    def __init__(self,parent=None, picks = []):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            check = Checkbutton(self, text = pick, variable = var)
            check.configure(bg = 'lightgreen', bd = 1)
            check.pack(anchor= W,expand = YES)
            self.vars.append(var)
    
    def state(self):
        return map((lambda var: var.get()), self.vars)
    
#Create Checkbox Matrix#   
matrix = [Checkbar(UI, ['','','','','','','','']), Checkbar(UI, ['','','','','','','','']), Checkbar(UI, ['','','','','','','','']), Checkbar(UI, ['','','','','','','','']),
          Checkbar(UI, ['','','','','','','','']), Checkbar(UI, ['','','','','','','','']), Checkbar(UI, ['','','','','','','','']), Checkbar(UI, ['','','','','','','',''])]
for create in range(0,len(matrix)):
    matrix[create].grid(column = create + 5, row = 1, rowspan = 10)



def getstates(key):
    chars[key] = [PIL.Image.new('RGB', (900,900), (255,255,255)), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    for count in range(0,len(matrix)):
        for i in range(0,8):
            if list(matrix[count].state())[i] == 1: chars[key][1][count+8]+=(int(math.pow(2,i)))

def shownew():
    key = newCharacter.get()
    getstates(key)
    static.set(1)
    getTextData('L', chars[key][1])
    static.set(0)
    
#save new charsacter as png#    
def savenew():
    key = newCharacter.get()
    getstates(key)
    draw = PIL.ImageDraw.Draw(chars[key][0])
    for i in range(0,9):
        x = i*100+50
        y = i*100+50
        draw.polygon([(x,50),(x,850)],fill = 'black',outline=None)
        draw.polygon([(50,y),(850,y)],fill = 'black',outline=None)
    for xi in range(0,8):
        x = xi * 100 + 50
        for yi in range(0,8):
            y = yi * 100 + 50
            if (1 & chars[key][1][xi+8] >> yi) == 1 : color = 'black'
            else: color = 'white'
            draw.rectangle([(x,y),(x+100, y+100)], fill = color, outline = 'black')
    chars[key][0].save(key+".png")

def createInterface():
#Headline#
    Label(UI, text = 'LED-Matrix Output', font = "16", bg = 'green', fg = 'lightgreen').grid(column = 0, row = 0, ipadx = 20, ipady = 5, columnspan = 4)
#Text dynamic/ displayStaticText#
    Label(UI, text = 'Text mode: ', bg = 'lightgreen').grid(column = 0, row = 1, padx = 7)
    Radiobutton(UI, text = 'Dynamic', indicatoron = 0, variable = static, value = 0).grid(column = 1, row = 1, sticky = W, ipadx = 6, ipady= 3, padx = 5, pady = 3)
    Radiobutton(UI, text = 'Static', indicatoron = 0, variable = static, value = 1).grid(column = 1, row = 2, sticky = W, ipadx = 14, ipady = 3, padx = 5, pady = 3)
#Raumteiler#
    Label(UI, text = '│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│', bg = 'lightgreen').grid(column = 4, row = 1, padx = 10, rowspan=6, pady =3)
    Label(UI, text = '', bg = 'lightgreen').grid(column = 2, row = 3, padx = 10,  pady =3)
#text speed#
    Label(UI, text = 'Text speed: ', bg = 'lightgreen').grid(column = 0, row = 4, sticky = W, padx = 7)
    Radiobutton(UI, text = 'fast', indicatoron = 0, variable = speed, value = 5).grid(column = 1, row = 4, sticky = W, ipadx = 20, ipady = 3, padx = 5, pady = 3)
    Radiobutton(UI, text = 'normal', indicatoron = 0, variable = speed, value = 10).grid(column = 1, row = 5, sticky = W, ipadx = 10, ipady = 3, padx = 5, pady = 3)
    Radiobutton(UI, text = 'slow', indicatoron = 0, variable = speed, value = 20).grid(column = 1, row = 6, sticky = W, ipadx = 18, ipady = 3, padx = 5, pady = 3)
#item box for text#
    Label(UI, text = 'Richtung: ', bg = 'lightgreen').grid(column = 2, row = 1, sticky = W)
    Label(UI, text = 'Text: ', bg = 'lightgreen').grid(column = 2, row = 2, sticky = W)
    entryDirection.grid(column = 3, row = 1, padx =5)
    entryText.grid(column = 3, row = 2, padx = 5)

    Button(UI, text = 'Show', command = getText, fg = 'green').grid(column = 3, row = 6, sticky = E, padx = 5, pady = 3)
#Headline 2#
    Label(UI, text = 'New character:', font = "16", bg = 'lightgreen').grid(column = 4, row = 0, ipadx = 20, ipady = 5, columnspan = 10)    
#Create new charsacter#
    Label(UI, text = 'character:', bg = 'lightgreen').grid(column = 13, row = 2)
    newCharacter.grid(column = 14, row = 2, padx = 7)
    Button(UI, text = 'Create new entry', command = savenew).grid(column = 14, row = 5, sticky = E, ipadx = 17, padx = 5, pady = 3)
    Button(UI, text = 'Show', command = shownew).grid(column = 14, row = 6, ipadx = 4, sticky = W, padx = 7, pady = 5)
    Button(UI, text = 'Quit', command = destroy, fg = 'red').grid(column = 14, row = 6, ipadx = 4, sticky = E, padx = 7, pady = 5)
#############################__привет__#############################     



if __name__=='__main__':
    init()
    try:
        createInterface()
        UI.mainloop()
    except: destroy()
