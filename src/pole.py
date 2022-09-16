import os
import sys
import time
from HX711 import AdvancedHX711, Rate
from pynput import keyboard
from utils.prompts import *
from utils.dframe import *

data = []
minWeight = 10
minTime = 3.0
maxTime = 20.0

test = "pole"
experiment = ""
group = ""
boxes = ""
mice = ""
trials = ""
initials = ""


def onPress(key, data, exp, grp, box, mice, trs, inits, test):
    if key == keyboard.KEY.esc: 
        return False
        sys.exit(os.EX_USAGE)
    try:
        k = key.char
    except:
        k = key.name
    if k in ['space']:
        r = data.pop()
        print("Removed: {:.3f}".format(r))
    if k in ['enter']:
        cleanExit(data, exp, grp, box, mice, trs, inits, test)


def poleTest(wmin, tmin, tmax, data): # minweight, mintime, maxtime
    loaded = 0
    tStart = 0.0
    tEnd = 0.0
    tElapsed = 0.0
    
    with AdvancedHX711(15, 14, 1, 0, Rate.HZ_80) as hx:
        while True:
            mass = hx.weight(1)

            if mass > wmin and loaded % 2 == 0:
                tStart = time.perf_counter()
                loaded += 1

            if mass < wmin and loaded % 2 != 0:
                tEnd = time.perf_counter()
                loaded += 1
                tElapsed = tEnd - tStart

            if tElapsed < tmin or tElapsed > tmax:
                loaded -= 2
                print("Time outside range: {:.3f}".format(tElapsed))
            else:
                data.append(tElapsed)
                print("Test#: {} - Time(s): {:.3f}".format(int(len(data)), tElapsed))


if __name__ == "__main__":

    getInfo(experiment, group, boxes, mice, trials, initials)

    listener = keyboard.Listener(onPress = lambda event:onPress(event, data, experiment, group, boxes, mice, trials, initials, test))
    listener.start()

    poleTest(minWeight, minTime, maxTime, data)
    