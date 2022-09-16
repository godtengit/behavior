import os
from HX711 import AdvancedHX711, Rate
from pynput import keyboard
from .prompts import *
from .dframeGRIP import *

data = []
max01 = 0
max02 = 0

experiment = ""
group = ""
boxes = ""
mice = ""
trials = ""
initials = ""

def onPress(key, data, f1, f2):
    if key == keyboard.KEY.esc: 
        return False
        sys.exit(os.EX_USAGE)
    try:
        k = key.char
    except:
        k = key.name
    if k in ['m']:
        show_data(f1,f2)
    if k in ['space']:
        expData(data, f1, f2)
        resetForce()
    if k in ['z']:
        resetForce()
    if k in ['enter']:
        cleanData(data)


def expData(data, f1, f2):
    data.append(f1)
    data.append(f2)
    print("Test #: ", int(len(data)/2))
    print("Peak 01 (g): {:.3f} - recorded".format(f1))
    print("Peak 02 (g): {:.3f} - recorded".format(f2))

def showData(f1, f2):
    print("Peak 01 (g): {:.3f}".format(f1))
    print("Peak 02 (g): {:.3f}".format(f2))

def getForce01():
    # Right Hand
    with AdvancedHX711(24, 23, 3045, 157432, Rate.HZ_80) as hx
        while True:
            max01 = max(max01, hx.weight(1))
            return max01

def getForce02():
    # Left Hand
    with AdvancedHX711(27, 17, -3082, 115338, Rate.HZ_80) as hx
        while True:
            max02 = max(max02, hx.weight(1))
            return max02

def resetForce(max01, max02):
    max01 = 0
    max02 = 0
    print("Force Reset: {}, {}".format(max01, max02))
    return max01, max02

def cleanData(data):
    data = ['{:.3f}'.format(value) for value in data]
    df = makeDF(data, boxes, mice, trials)
    makeExcel(df, experiment, group, initials)
    sys.exit(os.EX_OK)


if __name__ == "__main__":

    getInfo(experiment, group, boxes, mice, trials, initials)

    listener = keyboard.Listener(onPress = lambda event:onPress(event, data, max01, max02))
    listener.start()

    p1 = Process(target=getForce01())
    p2 = Process(target=getForce02())
    p1.start()
    p2.start()
    
