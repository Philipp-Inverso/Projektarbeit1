from tkinter import messagebox
from functools import reduce
import UserInterface
import PIL.ImageDraw
import PIL.Image
import math
import os

def PATH(): return os.getcwd()


class Characterset:
    chars = {}

    def __init__(self):
        self.chars = {}  # TypeDictionary = {'Key': Value}

    def createDictionary(self):

        for item in os.listdir(PATH()):
            if (item[-3:]).lower() == 'png':
                self.chars[item.split('.')[0]] = [PIL.Image.open(item),
                                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                   0]]
                # initialize dictionary with Key = 1st letter of item
                # value = [TypePicture, values of columns]
                # initialize columns value with 0

                for ix in range(0, 8):
                    x = ix * 100 + 100
                    for iy in range(0, 8, 1):
                        y = iy * 100 + 100
                        # iterate coordinates
                        r, g, b = self.chars[item.split('.')[0]][0].getpixel((x, y))
                        if (r == 0 and g == 0 and b == 0):
                            self.chars[item.split('.')[0]][1][ix + 8] += int(math.pow(2, iy))
                        # else: print ('weiss')
        return self

    def savenew(self):
        key = UserInterface.newCharacter.get()
        try:
            if any(s in key for s in '<>*?|.^"!@#$% ^&*()_+=-[]\\{};:/') or any(s in key for s in "'"):
                raise NameError
            self.getstates(key)
            draw = PIL.ImageDraw.Draw(self.chars[key][0])
            for i in range(0, 9):
                x = i * 100 + 50
                y = i * 100 + 50
                draw.polygon([(x, 50), (x, 850)], fill='black', outline=None)
                draw.polygon([(50, y), (850, y)], fill='black', outline=None)
            for xi in range(0, 8):
                x = xi * 100 + 50
                for yi in range(0, 8):
                    y = yi * 100 + 50
                    if (1 & self.chars[key][1][xi + 8] >> yi) == 1:
                        color = 'black'
                    else:
                        color = 'white'
                    draw.rectangle([(x, y), (x + 100, y + 100)], fill=color, outline='black')
            self.chars[key][0].save(key + ".png")
        except ValueError:
            messagebox.showerror('ERROR', 'Please type in a shortage of the characters name!')
        except NameError:
            messagebox.showerror('NameError', "Please check your Input: it shouldn't contain any Symbols")

    def getstates(self, key):
        self.chars[key] = [PIL.Image.new('RGB', (900, 900), (255, 255, 255)),
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        UserInterface.matrix1.getstates()
        matrix = UserInterface.matrix1.data
        for c, lists in enumerate(matrix):
            self.chars[key][1][c + 8] += reduce((lambda x, y: y + x), (
                list(int(math.pow(2, i)) if x == 1 else 0 for i, x in enumerate(lists))))
