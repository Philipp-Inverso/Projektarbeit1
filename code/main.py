import Characterset
import RPi.GPIO as GPIO
import UserInterface
import traceback
import Factory

#####  Global Variables  #####
def DATAPIN():  return 11
def DATAPIN():  return 11
def LATCHPIN(): return 13
def CLOCKPIN(): return 15


class RadioVars:
    static = Factory.IntVar()
    speed = Factory.IntVar()

    def __init__(self):
        self.speed.set(10)
        self.static.set(0)
##############################


def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DATAPIN(), GPIO.OUT)
    GPIO.setup(LATCHPIN(), GPIO.OUT)
    GPIO.setup(CLOCKPIN(), GPIO.OUT)


def destroy():
    Factory.UI.destroy()
    GPIO.cleanup()


if __name__ == '__main__':
    try:
        init()
        charset = Characterset.Characterset()
        charset.createDictionary()
        UserInterface.createInterface(charset)
        UserInterface.Factory.UI.mainloop()
    except Exception as e:
        traceback.print_exc()
        print(e)
        destroy()
