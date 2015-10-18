def getMinPos(min):
    return (min/60) * 360

def getHourPos(hour):
    return (hour/12) * 360

def getHMPos(time):
    hPos = getHourPos(time / 60)
    mPos = getMinPos(time % 60)
    return (hPos, mPos)