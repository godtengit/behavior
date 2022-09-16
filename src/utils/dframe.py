import os
import sys
import time
import pandas as pd


def rmWspace(str):
    return str.replace(" ", "")


def makeDF(data, boxes, mice, trials, test):
    rows_label = []
    columns_label = []
    n = 0

    for box in range(1, boxes + 1):
        for mouse in range(1, mice + 1):
            rows_label.append("{}.{}".format(box,mouse))

    if test == "grip":
        for i in range(1, trials + 1):
            for j in range(2):
                hand = 'R' if j == 0 else "L"
                columns_label.append("Trial {}{}".format(i, hand))
    else:
        for k in range(1, trials + 1):
            columns_label.append("Trial {}".format(k))    

    if test == "grip":
        n = trials * 2
    else:
        n = trials

    data = [data[i:i + n] for i in range(0, len(data), n)]
    df = pd.DataFrame(data, columns=columns_label)
    df.index = rows_label

    df.index.name = "Mouse"
    df["Mean"] = df.mean(axis=1)
    df["STDEV"] = df.std(axis=1, ddof=2)

    return df


def makeExcel(df, experiment, test, group, initials):
    rmWspace(experiment)

    today = time.strftime("%Y%m%d")

    filename = './Data/{0}_{1}_{2}_{3}_{4}.xlsx'.format(experiment, test, group, today, initials)
    df.to_excel(filename)


def cleanData(data):
    data = ['{:.3f}'.format(value) for value in data]
    return data


def cleanExit(data, experiment, group, boxes, mice, trials, initials, test):
    df = makeDF(data, boxes, mice, trials)
    makeExcel(df, experiment, test, group, initials)

    if test == "grip":
        print("Total tests: {}".format(int(len(data)/2)))
    else:
        print("Total tests: {}".format(int(len(data))))
    
    sys.exit(os.EX_OK)
