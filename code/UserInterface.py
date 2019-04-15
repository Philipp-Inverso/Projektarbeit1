from tkinter import *
import Display
import Factory
import main

Builder = Factory.UIFactory.factory

matrix1 = Builder('Matrix').build(5, 1)

entryMirror = Factory.Entry(Factory.UI)
entryText = Factory.Entry(Factory.UI)
newCharacter = Factory.Entry(Factory.UI)
entryMirror.insert(12, '0')


def createInterface(charset):
    # Headline#
    Builder('Label').build('LED-Matrix Output', 0, 0, columnspan=4, ipadx=20,
                           font="16", fg='lightgreen', bg='green')
    # Text dynamic/ displayStaticText#
    Builder('Label').build('Text mode: ', 0, 1)
    Builder('Radio').build('Dynamic', 0, main.RadioVars.static, 0, 1, 1)
    Builder('Radio').build('Static', 0, main.RadioVars.static, 1, 1, 2)
    # Raumteiler#
    Builder('Label').build('│\n│\n│\n│\n│\n│\n│\n│\n│', 4, 1, rowspan=10)
    Builder('Label').build('', 2, 3)
    # text speed#
    Builder('Label').build('Text speed: ', 0, 4)
    Builder('Radio').build('fast', 0, main.RadioVars().speed, 5, 1, 4)
    Builder('Radio').build('normal', 0, main.RadioVars().speed, 10, 1, 5)
    Builder('Radio').build('slow', 0, main.RadioVars().speed, 20, 1, 6)
    # item box for text#
    Builder('Label').build('Turn: ', 2, 1)
    Builder('Label').build('Text: ', 2, 2)
    Builder('Entry').build(entryMirror, 3, 1)
    Builder('Entry').build(entryText, 3, 2)

    Builder('Button').build('Help', helper, 3, 5)
    Builder('Button').build('Show', lambda chars=charset: Display.getText(chars.chars), 3, 6, fg='green')
    # Headline 2#
    Builder('Label').build('New character:', 4, 0, columnspan=6, font="16", )
    # Create new charsacter#
    Builder('Label').build('character:', 13, 2)
    Builder('Entry').build(newCharacter, 14, 2, padx=3)
    Builder('Button').build('Create new entry', charset.savenew, 14, 5, padx=2)
    Builder('Button').build('Show', lambda chars=charset: Display.shownew(chars), 14, 6, sticky='wns', ipadx=16, padx=2)
    Builder('Button').build('Quit', main.destroy, 14, 6, sticky='ens', ipadx=15, fg='red', padx=2)


def helper():
    helper = Toplevel()  # create new Window
    helper.wm_title("Help")  # new Windows Title
    label = Label(helper, text="""Eingabe von beliebigem Text in das Feld Text:\n
                 Im Textfeld werden Sonderzeichen mit\n
                 <*NAME*> oder <\\NAME/> aufgerufen.\n\n
                 Der Text kann durch Eingabe von 0-4 oder die Gradzahlen 0,90,180,270 im Feld Turn\n
                 fuer bessere Lesbarkeit um gedreht werden.\n\n
                 Links: Erstellung neuer Symbole\nName kann Buchstabe oder Wort sein.'\n
                 Bitte keine Sonderzeichen!\n""")
    label.grid(row=0, column=0)
    B1 = Button(helper, text="Okay", command=helper.destroy)  # Quitbutton
    B1.grid(column=0, row=1, ipadx=5, ipady=2)
