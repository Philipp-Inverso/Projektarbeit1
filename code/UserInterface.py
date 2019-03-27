from functools import reduce
import PIL.ImageDraw
import PIL.Image
import Display
import Factory
import math
import main

Builder = Factory.UIFactory.factory

matrix1 = Builder('Matrix').build(5, 1)

entryMirror = Factory.Entry(Factory.UI)
entryText = Factory.Entry(Factory.UI)
newCharacter = Factory.Entry(Factory.UI)
entryMirror.insert(12,'N')

def getstates(key):
    main.chars[key] = [PIL.Image.new('RGB', (900,900), (255,255,255)), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    matrix1.getstates()
    matrix = matrix1.data
    for c, lists in enumerate(matrix):
        main.chars[key][1][c+8] += reduce((lambda x,y: y+x), (list(int(math.pow(2,i)) if x == 1 else 0 for i, x in enumerate(lists))))

def shownew():
    key = newCharacter.get()
    getstates(key)
    main.RadioVars.static.set(1)
    Display.displayText(1, main.chars[key][1][8:16])
    main.RadioVars.static.set(0)
    
#save new charsacter as png#    
def savenew():
    key = newCharacter.get()
    if not key in main.chars:
        getstates(key)
    draw = PIL.ImageDraw.Draw(main.chars[key][0])
    for i in range(0,9):
        x = i*100+50
        y = i*100+50
        draw.polygon([(x,50),(x,850)],fill = 'black',outline=None)
        draw.polygon([(50,y),(850,y)],fill = 'black',outline=None)
    for xi in range(0,8):
        x = xi * 100 + 50
        for yi in range(0,8):
            y = yi * 100 + 50
            if (1 & main.chars[key][1][xi+8] >> yi) == 1 : color = 'black'
            else: color = 'white'
            draw.rectangle([(x,y),(x+100, y+100)], fill = color, outline = 'black')
    main.chars[key][0].save(key+".png")

def createInterface(charset):
#Headline#
    Builder('Label').build('LED-Matrix Output', 0, 0, columnspan = 4, ipadx = 20,
                           font = "16", fg = 'lightgreen', bg = 'green')
#Text dynamic/ displayStaticText#
    Builder('Label').build('Text mode: ', 0, 1)
    Builder('Radio').build('Dynamic', 0, main.RadioVars.static, 0, 1, 1)
    Builder('Radio').build('Static', 0, main.RadioVars.static, 1, 1, 2)
#Raumteiler#
    Builder('Label').build('│\n│\n│\n│\n│\n│\n│\n│\n│', 4, 1, rowspan = 10)
    Builder('Label').build('', 2, 3)
#text speed#
    Builder('Label').build('Text speed: ', 0, 4)
    Builder('Radio').build('fast', 0, main.RadioVars.speed, 5, 1, 4)
    Builder('Radio').build('normal', 0, main.RadioVars.speed, 10, 1, 5)
    Builder('Radio').build('slow', 0, main.RadioVars.speed, 20, 1, 6)
#item box for text#
    Builder('Label').build('Mirror: ', 2, 1)
    Builder('Label').build('Text: ', 2, 2)
    Builder('Entry').build(entryMirror, 3, 1)
    Builder('Entry').build(entryText, 3, 2)

    Builder('Button').build('Show', Display.getText(charset), 3, 6, fg = 'green')
#Headline 2#
    Builder('Label').build('New character:',  4, 0, columnspan = 6, font = "16",)    
#Create new charsacter#
    Builder('Label').build('character:', 13, 2)
    Builder('Entry').build(newCharacter, 14, 2)
    Builder('Button').build('Create new entry', savenew, 14, 5)
    Builder('Button').build('Show', shownew, 14, 6, sticky = 'wns', ipadx = 15)
    Builder('Button').build('Quit', main.destroy, 14, 6, sticky = 'ens', ipadx = 15, fg = 'red')
    
#createInterface()