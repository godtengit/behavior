def getInfo(experiment, group, boxes, mice, trials, initials):
    experiment = input("Name of experiment: ").strip()
    while not experiment:
        experiment = input("Name of experiment: ").strip()

    group = input("Name of group: ").strip()
    while not group:
        group = input("Name of group: ").strip()

    boxes = input("Number of boxes: ").strip()
    while not boxes or not boxes.isdigit():
        boxes = input("Number of boxes: ").strip()
    boxes = int(boxes)

    mice = input("Number of mice per box: ").strip()
    while not mice or not mice.isdigit():
        mice = input("Number of mice per box: ").strip()
    mice = int(mice)

    trials = input("Number of trials per mouse: ").strip()
    while not trials or not trials.isdigit():
        trials = input("Number of trials per mouse: ").strip()
    trials = int(trials)

    initials = input("Initials: ").strip().upper()
    while not initials:
        initials = input("Initials: ").strip().upper()

    return experiment, group, boxes, mice, trials, initials
