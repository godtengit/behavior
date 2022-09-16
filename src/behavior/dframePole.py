import pandas as pd
import time

def rmWhitespace(str):
    return str.replace(" ", "")

def makeDF(data, boxes, mice, trials, test):
    rows_label = []
    colums_label = []
    n = 0

    for box in range(1, boxes + 1):
        for mouse in range(1, mice + 1):
            rows_label.append("{}.{}".format(box,mouse))

    for k in range(1, trials + 1):
        columns_label.append("Trial {}".format(k))

    n = trials

    data = [data[i:i + n] for i in range(0, len(data), n)]
    df = pd.DataFrame(data, columns=columns_label)
    df.index = rows_label

    df.index.name = "Mouse"
    df["Mean"] = df.mean(axis=1)
    df["STDEV"] = df.std(axis=1, ddof=2)

    return df

def make_excel(df, experiment, group, initials):
    rmWhitespace(experiment)

    today = time.strftime("%Y%m%d")

    filename = './Data/{0}_{1}_{2}_{3}_{4}.xlsx'.format('Pole', experiment, group, today, initials)
    df.to_excel(filename)

if __name__ == "__main__":
    