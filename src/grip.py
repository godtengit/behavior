from multiprocessing import Process, Manager
from HX711 import AdvancedHX711, Rate
from pynput import keyboard
from utils.prompts import *
from utils.dframe import *

data = []
maxData = Manager().list([0.0, 0.0])
listener = None
# test = "grip"
# experiment = ""
# group = ""
# boxes = 0
# mice = 0
# trials = 0
# initials = ""


# def onPress(key, data, exp, grp, box, mice, trs, inits, test, maxData):
def onPress(key, data, maxData)
    if key == keyboard.Key.esc: 
        return False
    try:
        k = key.char
    except:
        k = key.name
    if k in ['m']:
        showData(maxData)
    if k in ['space']:
        pinData(data, maxData)
        resetForce(maxData)
    if k in ['z']:
        resetForce(maxData)
    # if k in ['enter']:
    #     cleanExit(data, exp, grp, box, mice, trs, inits, test)
    if k in ['w']:
        print("WOW!")


def pinData(data, maxData):
    data.append(maxData)
    print("Test #: ", len(data))
    print("Peak 01 (g): {:.3f} - recorded".format(maxData[0]))
    print("Peak 02 (g): {:.3f} - recorded".format(maxData[1]))
    return data


def showData(maxData):
    print("Peak 01 (g): {:.3f}".format(maxData[0]))
    print("Peak 02 (g): {:.3f}".format(maxData[1]))


def getForce01(maxData):
    # Right Hand orange
    with AdvancedHX711(27, 17, -3435, 117303, Rate.HZ_80) as hx:
        while True:
            m = float(hx.weight(1)) 
            if m < 100.0 and m > maxData[0]:
                maxData[0] = m


def getForce02(maxData):
    # Left Hand blue
    with AdvancedHX711(24, 23, 3191, 141342, Rate.HZ_80) as hx:
        while True:
            m = float(hx.weight(1)) 
            if m < 100.0 and m > maxData[1]:
                maxData[1] = m


def resetForce(maxData):
    # global maxData
    maxData[0] = 0.0
    maxData[1] = 0.0
    print("Force Reset: {}, {}".format(maxData[0], maxData[1]))
    return maxData


def keyboardHooks(data, maxData):
    global listener
    # listener = keyboard.Listener(on_press = 
    #     lambda event:onPress(
    #         event, data, experiment, group, boxes, 
    #         mice, trials, initials, test, maxData))
    listener = keyboard.Listener(on_press = lambda event:onPress(event, data, maxData))
    listener.start()
    print("Listening...")


def main(data, maxData):
    # getInfo(experiment, group, boxes, mice, trials, initials
    keyboardHooks(data, maxData)
    p1 = Process(target=getForce01, args=(maxData,))
    p2 = Process(target=getForce02, args=(maxData,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == "__main__":

    main(data, maxData)