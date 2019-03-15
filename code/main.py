import RPi.GPIO as GPIO
import pyexcel as ods
from tkinter import *
import time
import collections
import math

dataPin  = 11
latchPin = 13
clockPin = 15

UI = Tk()
UI.configure(bg = 'lightgreen')
staticbool = IntVar()
speed = IntVar()
staticbool.set(0)
speed.set(10)
edir  = Entry(UI)
etext = Entry(UI)
echar = Entry(UI)
edir.insert(12,'L')

doc = ods.get_sheet(file_name="characterset.ods")
char = collections.OrderedDict()
eof = 0
newchar = {}

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
    
def dictionary():
    global eof
    row = 0
    while True:
        try:
            char[doc[row, 1]] = [doc[row, 20]]
            row += 9
        except IndexError:
            eof = row
            break
    row = 0
    for key in char:
        try:
            for column in range(21,28):
                char[key].append(doc[row, column])
            row += 9
        except IndexError: break
        for c in range(0,8):
            char[key].insert(0,0)
            char[key].append(0)

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(dataPin,  GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    dictionary()

def shiftout(dPin, cPin, direction, val):
    """Shift data into registers"""
    for i in range(0,8):
        GPIO.output(cPin, GPIO.LOW)
        if (direction == 'R'):
            GPIO.output(dPin, (0x80 & (val<<i) == 0x80) and GPIO.HIGH or GPIO.LOW) ## Scroll Rightwards
        elif (direction == 'L'):
            GPIO.output(dPin, (0x01 & (val>>i) == 0x01) and GPIO.HIGH or GPIO.LOW) ## Scroll Leftwards
        GPIO.output(cPin, GPIO.HIGH)
        
def scroll(direction, data):
    """Animate Text"""
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
    """Display non-animated Text"""
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
    """Combine multiple Data arrays to display animated Text or Cut data to display non-animated Text"""
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
            
def loop(direction, text, *new):
    #start_time = time.time()
    args=[]
    if new: args.append(newchar)
    else:
        for letter in text:
            try:
                args.append(char[letter.upper()])
            except KeyError: print(letter + ' is not included in the characterset')
    #end_time = time.time()
    #print("%.10f seconds" % (end_time - start_time))
    display(direction, args)
    
def show():
    text = etext.get()
    direction = edir.get()
    etext.delete(0,END)
    loop(direction, text)

def shownew():
    getstates()
    loop('L', '1', 1)
    
def destroy():
    doc.save_as("characterset-kaputt.ods")
    UI.destroy()
    GPIO.cleanup()

matrix = [checkbar(UI, ['','','','','','','','']), checkbar(UI, ['','','','','','','','']), checkbar(UI, ['','','','','','','','']), checkbar(UI, ['','','','','','','','']),
          checkbar(UI, ['','','','','','','','']), checkbar(UI, ['','','','','','','','']), checkbar(UI, ['','','','','','','','']), checkbar(UI, ['','','','','','','',''])]
for create in range(0,len(matrix)):
    matrix[create].grid(column = create + 5, row = 1, rowspan = 10)

def getstates():
    global newchar
    key = echar.get()
    newchar[key] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for count in range(0,len(matrix)):
        for i in range(0,8):
            if list(matrix[count].state())[i] == 1: newchar[key][count+8]+=(int(math.pow(2,i)))

def interface():
    Label(UI, text = 'LED-Matrix Output', font = "16", bg = 'green', fg = 'lightgreen').grid(column = 0, row = 0, ipadx = 20, ipady = 5, columnspan = 4)

    Label(UI, text = 'Text mode: ', bg = 'lightgreen').grid(column = 0, row = 1, padx = 7)
    Radiobutton(UI, text = 'Dynamic', indicatoron = 0, variable = staticbool, value = 0).grid(column = 1, row = 1, sticky = W, ipadx = 6, ipady= 3, padx = 5, pady = 3)
    Radiobutton(UI, text = 'Static', indicatoron = 0, variable = staticbool, value = 1).grid(column = 1, row = 2, sticky = W, ipadx = 14, ipady = 3, padx = 5, pady = 3)
    Label(UI, text = '│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│', bg = 'lightgreen').grid(column = 4, row = 1, padx = 10, rowspan=6, pady =3)
    Label(UI, text = '', bg = 'lightgreen').grid(column = 2, row = 3, padx = 10,  pady =3)

    Label(UI, text = 'Text speed: ', bg = 'lightgreen').grid(column = 0, row = 4, sticky = W, padx = 7)
    Radiobutton(UI, text = 'fast', indicatoron = 0, variable = speed, value = 5).grid(column = 1, row = 4, sticky = W, ipadx = 20, ipady = 3, padx = 5, pady = 3)
    Radiobutton(UI, text = 'normal', indicatoron = 0, variable = speed, value = 10).grid(column = 1, row = 5, sticky = W, ipadx = 10, ipady = 3, padx = 5, pady = 3)
    Radiobutton(UI, text = 'slow', indicatoron = 0, variable = speed, value = 20).grid(column = 1, row = 6, sticky = W, ipadx = 18, ipady = 3, padx = 5, pady = 3)
        
    Label(UI, text = 'Richtung: ', bg = 'lightgreen').grid(column = 2, row = 1, sticky = W)
    Label(UI, text = 'Text: ', bg = 'lightgreen').grid(column = 2, row = 2, sticky = W)
    edir.grid(column = 3, row = 1, padx =5)
    etext.grid(column = 3, row = 2, padx = 5)

    Button(UI, text = 'Show', command = show, fg = 'green').grid(column = 3, row = 6, sticky = E, padx = 5, pady = 3)
    
    Label(UI, text = 'Temporary Character:', font = "16", bg = 'lightgreen').grid(column = 4, row = 0, ipadx = 20, ipady = 5, columnspan = 10)    
    
    Label(UI, text = 'Character:', bg = 'lightgreen').grid(column = 13, row = 2)
    echar.grid(column = 14, row = 2, padx = 7)
    Button(UI, text = 'Create new Entry', command = getstates).grid(column = 14, row = 5, sticky = E, ipadx = 1, padx = 5, pady = 3)
    Button(UI, text = 'Quit', command = destroy, fg = 'red').grid(column = 14, row = 6, ipadx = 4, sticky = E, padx = 7, pady = 5)
    

if __name__=='__main__':
    setup()
    try:
        interface()
        UI.mainloop()
    except: destroy()
