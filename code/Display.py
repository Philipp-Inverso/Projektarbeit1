from tkinter import messagebox
import RPi.GPIO as GPIO
import UserInterface
import main
import time


def shiftout(dPin, cPin, direction, val):
    for i in range(0, 8):
        GPIO.output(cPin, GPIO.LOW)
        if (direction == 'R'):
            GPIO.output(dPin, (0x80 & (val << i) == 0x80) and GPIO.HIGH or GPIO.LOW)  ## displayRunningText Rightwards
        elif (direction == 'L'):
            GPIO.output(dPin, (0x01 & (val >> i) == 0x01) and GPIO.HIGH or GPIO.LOW)  ## displayRunningText Leftwards
        GPIO.output(cPin, GPIO.HIGH)


def displayText(static, data):
    speed = main.RadioVars.speed.get()
    mirror = UserInterface.entryMirror.get()
    if mirror == '0' or mirror == '360':
        if not static:
            for k in range(0, len(data) - 8):
                for j in range(0, speed):
                    x = 0x80
                    for i in range(k, k + 8):
                        GPIO.output(main.LATCHPIN(), GPIO.LOW)
                        shiftout(main.DATAPIN(), main.CLOCKPIN(), 'R', data[i])
                        shiftout(main.DATAPIN(), main.CLOCKPIN(), 'L', ~x)
                        GPIO.output(main.LATCHPIN(), GPIO.HIGH)
                        time.sleep(0.001)
                        x >>= 1
        else:  # display static text
            for j in range(0, 500):
                x = 0x80
                for i in range(0, 8):
                    GPIO.output(main.LATCHPIN(), GPIO.LOW)
                    shiftout(main.DATAPIN(), main.CLOCKPIN(), 'R', data[i])
                    shiftout(main.DATAPIN(), main.CLOCKPIN(), 'L', ~x)
                    GPIO.output(main.LATCHPIN(), GPIO.HIGH)
                    time.sleep(0.001)
                    x >>= 1
    elif mirror == '90' or mirror == '1':
        if not static:
            for k in range(0, len(data) - 8):
                for j in range(0, speed):
                    x = 0x80
                    for i in range(k, k + 8):
                        GPIO.output(main.LATCHPIN(), GPIO.LOW)
                        shiftout(main.DATAPIN(), main.CLOCKPIN(), 'L', x)
                        shiftout(main.DATAPIN(), main.CLOCKPIN(), 'L', ~data[i])
                        GPIO.output(main.LATCHPIN(), GPIO.HIGH)
                        time.sleep(0.001)
                        x >>= 1
        else:  # display static text
            for j in range(0, 500):
                x = 0x80
                for i in range(0, 8):
                    GPIO.output(main.LATCHPIN(), GPIO.LOW)
                    shiftout(main.DATAPIN(), main.CLOCKPIN(), 'L', x)
                    shiftout(main.DATAPIN(), main.CLOCKPIN(), 'L', ~data[i])
                    GPIO.output(main.LATCHPIN(), GPIO.HIGH)
                    time.sleep(0.001)
                    x >>= 1
    elif mirror == '180' or mirror == '2':
        if not static:
            for k in range(0, len(data) - 8):
                for j in range(0, speed):
                    x = 0x80
                    for i in range(k, k + 8):
                        GPIO.output(main.LATCHPIN(), GPIO.LOW)
                        shiftout(main.DATAPIN(), main.CLOCKPIN(), 'L', data[i])
                        shiftout(main.DATAPIN(), main.CLOCKPIN(), 'R', ~x)
                        GPIO.output(main.LATCHPIN(), GPIO.HIGH)
                        time.sleep(0.001)
                        x >>= 1
        else:  # display static text
            for j in range(0, 500):
                x = 0x80
                for i in range(0, 8):
                    GPIO.output(main.LATCHPIN(), GPIO.LOW)
                    shiftout(main.DATAPIN(), main.CLOCKPIN(), 'L', data[i])
                    shiftout(main.DATAPIN(), main.CLOCKPIN(), 'R', ~x)
                    GPIO.output(main.LATCHPIN(), GPIO.HIGH)
                    time.sleep(0.001)
                    x >>= 1
    elif mirror == '270' or mirror == '3':
        if not static:
            for k in range(0, len(data) - 8):
                for j in range(0, speed):
                    x = 0x80
                    for i in range(k, k + 8):
                        GPIO.output(main.LATCHPIN(), GPIO.LOW)
                        shiftout(main.DATAPIN(), main.CLOCKPIN(), 'R', x)
                        shiftout(main.DATAPIN(), main.CLOCKPIN(), 'R', ~data[i])
                        GPIO.output(main.LATCHPIN(), GPIO.HIGH)
                        time.sleep(0.001)
                        x >>= 1
        else:  # display static text
            for j in range(0, 500):
                x = 0x80
                for i in range(0, 8):
                    GPIO.output(main.LATCHPIN(), GPIO.LOW)
                    shiftout(main.DATAPIN(), main.CLOCKPIN(), 'R', x)
                    shiftout(main.DATAPIN(), main.CLOCKPIN(), 'R', ~data[i])
                    GPIO.output(main.LATCHPIN(), GPIO.HIGH)
                    time.sleep(0.001)
                    x >>= 1
    else:
        messagebox.showwarning('InputError', mirror + ' is an invalid Input for turn.')
    UserInterface.entryText.delete(0, 'end')


def getText(charset):
    args = []
    letters = ''
    caution = False
    string = False
    text = UserInterface.entryText.get()
    for letter in text:
        try:
            if not caution and not string:
                if letter == '<':
                    caution = True
                else:
                    args.append(charset[letter][1])
            elif caution and not string:
                if letter == '*' or letter == '\\':
                    caution = False
                    string = True
                else:
                    args.append(charset[letter][1])
                    caution = False

            elif not caution and string:
                if letter == text[-1]:
                    messagebox.showwarning("InputError", "Please check your Input!\nEOL but not End of String")
                    args = []
                    break
                if letter == '*' or letter == '/':
                    caution = True
                else:
                    letters += letter
            elif caution and string:
                if letter == '>':
                    caution = False
                    string = False
                    try:
                        args.append(charset[letters][1])
                        letters = ''
                    except KeyError:
                        messagebox.showwarning("Warning", letters + " is not included in the charsacterset")
                        args = []
                        break
                else:
                    letters += '*'
                    letters += letter
                    caution = False

        except KeyError:
            messagebox.showwarning("Warning", letter + " is not included in the charsacterset")
            args = []
            break

    index = len(args)
    if main.RadioVars.static.get():
        try:
            data = args[0][8:16]
            # cut off leading and last 8 zeros
            displayText(1, data)
        except IndexError:
            messagebox.showwarning("Warning", "There is no text to display.")
    else:
        if (index == 1):
            data = (args[0])
            # don't cut
            displayText(0, data)

        elif (index >= 2):
            data = (args[0][0:14])
            # cut last 10 zeros
            for i in range(1, index - 1):
                data.extend(args[i][8:15])
                # cut leading 8 and last 10 zeros
            data.extend(args[index - 1][8:])
            # cut leading 8 zeros
            displayText(0, data)
        else:
            messagebox.showwarning("Warning", "There is no text to display.")


def shownew(charset):
    key = UserInterface.newCharacter.get()
    charset.getstates(key)
    main.RadioVars.static.set(1)
    displayText(1, charset.chars[key][1][8:16])
    main.RadioVars.static.set(0)
