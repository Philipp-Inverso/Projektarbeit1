import RPi.GPIO as GPIO
from tkinter import *
from tkinter import messagebox
import PIL.Image
import PIL.ImageDraw
import time
import math
import os

dataPin  = 11
latchPin = 13
clockPin = 15

UI = Tk()
UI.configure(bg = 'lightgreen')
staticbool = IntVar()
speed = IntVar()
staticbool.set(0)
speed.set(10)

path = os.getcwd()
char = {}
pics = {}
    
def dictionary():
    for entry in os.listdir(path):
        if entry[2:] == 'png':
            char[entry[0]] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for key in char:
        pics[key] = PIL.Image.open(key+'.png')
        for ix in range(0,8):
            x = ix * 100 + 100
            for iy in range(9,1,-1):
                y = iy * 100 - 100
                r,g,b = pics[key].getpixel((x,y))
                if (r == 0 and g == 0 and b == 0):
                    char[key][ix+8]+=(int(math.pow(2,(iy-2))))
                #else: print ('weiss')
    
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(dataPin,  GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    dictionary()

def shiftout(dPin, cPin, direction, val):
#Shift data into registers#
    for i in range(0,8):
        GPIO.output(cPin, GPIO.LOW)
        if (direction == 'R'):
            GPIO.output(dPin, (0x80 & (val<<i) == 0x80) and GPIO.HIGH or GPIO.LOW) ## Scroll Rightwards
        elif (direction == 'L'):
            GPIO.output(dPin, (0x01 & (val>>i) == 0x01) and GPIO.HIGH or GPIO.LOW) ## Scroll Leftwards
        GPIO.output(cPin, GPIO.HIGH)
        
def scroll(direction, data):
#Animate Text#
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
                
def static(data):
#Display non-animated Text#
    for j in range(0,500):
        x=0x80
        for i in range(0,8):
            GPIO.output(latchPin,GPIO.LOW)
            shiftout(dataPin,clockPin,'R',data[i])
            shiftout(dataPin,clockPin,'L',~x)
            GPIO.output(latchPin,GPIO.HIGH)
            time.sleep(0.001)
            x>>=1
            
def display(direction, args):
#Combine multiple Data arrays to display animated Text or Cut data to display non-animated Text#
    data=[]
    index = len(args)
    if staticbool.get():
        data=args[0][8:16]
        static(data)
    else:
        if (len(args) == 1):
            data=(args[0])
            scroll(direction, data)
        elif(len(args) >= 2):
            data=(args[0][0:14])
            for i in range(1,index-1):
                data.extend(args[i][8:14])
            data.extend(args[index-1][8:])
            scroll(direction, data)
            
def loop(direction, text):
    args=[]
    for letter in text:
        try:
            args.append(char[letter])#letter.upper()
        except KeyError:
            messagebox.showwarning("Warning",letter+" is not included in the Characterset")
            args = []
            break
    display(direction, args)
    
def show():
    text = etext.get()
    direction = edir.get()
    etext.delete(0,END)
    loop(direction, text)
    
def destroy():
    UI.destroy()
    GPIO.cleanup()

###################__INTERFACE__###################
#variables#
edir  = Entry(UI)
etext = Entry(UI)
echar = Entry(UI)
edir.insert(12,'L')

class checkbar(Frame):
    def __init__(self,parent=None,choices = []):
        Frame.__init__(self, parent)
        self.vars = []
        for choice in choices:
            var = IntVar()
            check = Checkbutton(self, text = choice, variable = var)
            check.configure(bg = 'lightgreen', bd = 1)
            check.pack(anchor= W,expand = YES)
            self.vars.append(var)
    
    def state(self):
        return map((lambda var: var.get()), self.vars)
    
#Create Checkbox Matrix#   
matrix = [checkbar(UI, ['','','','','','','','']), checkbar(UI, ['','','','','','','','']), checkbar(UI, ['','','','','','','','']), checkbar(UI, ['','','','','','','','']),
          checkbar(UI, ['','','','','','','','']), checkbar(UI, ['','','','','','','','']), checkbar(UI, ['','','','','','','','']), checkbar(UI, ['','','','','','','',''])]
for create in range(0,len(matrix)):
    matrix[create].grid(column = create + 5, row = 1, rowspan = 10)

def getstates():
    key = echar.get()
    char[key] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for count in range(0,len(matrix)):
        for i in range(0,8):
            if list(matrix[count].state())[i] == 1: char[key][count+8]+=(int(math.pow(2,i)))

def shownew():
    getstates()
    loop('L', echar.get())
    
#save new Character as png#    
def savenew():
    getstates()
    newkey = str(echar.get())
    pics[newkey] = PIL.Image.new('RGB', (900,900), (255,255,255))
    pics[newkey+'draw'] = PIL.ImageDraw.Draw(pics[newkey])
    for i in range(0,9):
        x = i*100+50
        y = i*100+50
        pics[newkey+'draw'].polygon([(x,50),(x,850)],fill = 'black',outline=None)
        pics[newkey+'draw'].polygon([(50,y),(850,y)],fill = 'black',outline=None)
    for xi in range(0,8):
        x = xi * 100 + 50
        for yi in range(0,8):
            y = yi * 100 + 50
            if (1 & char[newkey][xi+8] >> yi) == 1 : color = 'black'
            else: color = 'white'
            pics[newkey+'draw'].rectangle([(x,y),(x+100, y+100)], fill = color, outline = 'black')
    pics[newkey].save(newkey+".png")

def interface():
#Headline#
    Label(UI, text = 'LED-Matrix Output', font = "16", bg = 'green', fg = 'lightgreen').grid(column = 0, row = 0, ipadx = 20, ipady = 5, columnspan = 4)
#Text dynamic/ static#
    Label(UI, text = 'Text mode: ', bg = 'lightgreen').grid(column = 0, row = 1, padx = 7)
    Radiobutton(UI, text = 'Dynamic', indicatoron = 0, variable = staticbool, value = 0).grid(column = 1, row = 1, sticky = W, ipadx = 6, ipady= 3, padx = 5, pady = 3)
    Radiobutton(UI, text = 'Static', indicatoron = 0, variable = staticbool, value = 1).grid(column = 1, row = 2, sticky = W, ipadx = 14, ipady = 3, padx = 5, pady = 3)
#Raumteiler#
    Label(UI, text = '│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│', bg = 'lightgreen').grid(column = 4, row = 1, padx = 10, rowspan=6, pady =3)
    Label(UI, text = '', bg = 'lightgreen').grid(column = 2, row = 3, padx = 10,  pady =3)
#text speed#
    Label(UI, text = 'Text speed: ', bg = 'lightgreen').grid(column = 0, row = 4, sticky = W, padx = 7)
    Radiobutton(UI, text = 'fast', indicatoron = 0, variable = speed, value = 5).grid(column = 1, row = 4, sticky = W, ipadx = 20, ipady = 3, padx = 5, pady = 3)
    Radiobutton(UI, text = 'normal', indicatoron = 0, variable = speed, value = 10).grid(column = 1, row = 5, sticky = W, ipadx = 10, ipady = 3, padx = 5, pady = 3)
    Radiobutton(UI, text = 'slow', indicatoron = 0, variable = speed, value = 20).grid(column = 1, row = 6, sticky = W, ipadx = 18, ipady = 3, padx = 5, pady = 3)
#entry box for text#
    Label(UI, text = 'Richtung: ', bg = 'lightgreen').grid(column = 2, row = 1, sticky = W)
    Label(UI, text = 'Text: ', bg = 'lightgreen').grid(column = 2, row = 2, sticky = W)
    edir.grid(column = 3, row = 1, padx =5)
    etext.grid(column = 3, row = 2, padx = 5)

    Button(UI, text = 'Show', command = show, fg = 'green').grid(column = 3, row = 6, sticky = E, padx = 5, pady = 3)
#Headline 2#
    Label(UI, text = 'New Character:', font = "16", bg = 'lightgreen').grid(column = 4, row = 0, ipadx = 20, ipady = 5, columnspan = 10)    
#Create new Character#
    Label(UI, text = 'Character:', bg = 'lightgreen').grid(column = 13, row = 2)
    echar.grid(column = 14, row = 2, padx = 7)
    Button(UI, text = 'Create new Entry', command = savenew).grid(column = 14, row = 5, sticky = E, ipadx = 15, padx = 5, pady = 3)
    Button(UI, text = 'Show', command = shownew).grid(column = 14, row = 6, ipadx = 4, sticky = W, padx = 7, pady = 5)
    Button(UI, text = 'Quit', command = destroy, fg = 'red').grid(column = 14, row = 6, ipadx = 4, sticky = E, padx = 7, pady = 5)
###################__привет__###################     



if __name__=='__main__':
    setup()
    try:
        interface()
        UI.mainloop()
    except: destroy()
