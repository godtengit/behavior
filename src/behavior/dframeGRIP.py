import pandas as pd
import time
from src.behavior.

def rmWhitespace(str):
    return str.replace(" ", "")

def makeDF(data, boxes, mice, trials):
    rows_label = []
    colums_label = []
    n = 0

    for box in range(1, boxes + 1):
        for mouse in range(1, mice + 1):
            rows_label.append("{}.{}".format(box,mouse))

    for i in range(1, trials + 1):
        for j in range(2):
            hand = 'R' if j == 0 else "L"
            colums_label.append("Trial {}{}".format(i, hand))

    n = trials * 2

    data = [data[i:i + n] for i in range(0, len(data), n)]
    df = pd.DataFrame(data, columns=columns_label)
    df.index = rows_label

    df.index.name = "Mouse"
    df["Mean"] = df.mean(axis=1)
    df["STDEV"] = df.std(axis=1, ddof=2)

    return df

def makeExcel(df, experiment, group, initials):
    rmWhitespace(experiment)

    today = time.strftime("%Y%m%d")

    filename = './Data/{0}_{1}_{2}_{3}_{4}.xlsx'.format("Grip", experiment, group, today, initials)
    df.to_excel(filename)

if __name__ == "__main__":
    