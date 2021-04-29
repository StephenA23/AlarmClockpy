# Alarm clock in python
# Allows user to input a time
# Alerts user when time has reached.

from datetime import datetime
from playsound import playsound
def setAlarmTime():
    # prompt user to set a time
    hourTime = input("Set an hour time (24 hour system): ")
    minuteTime = input("Set an minute time: ")

    alarmTime = hourTime + minuteTime

    if(len(alarmTime) != 4):
        print("Alarm Time should be 4 digits")
        print("Ensure the Hour and Minute have 2 digits each")
        setAlarmTime()
    else:
        print(alarmTime)
        return alarmTime
    

def isAlarmTime(alarmTime):
    # Check if Alarm time is equal to current time
    # if it is alert user
    
    # get current time
    # string it to hour and minute
    # make it the same format as alarmTime 
    while True:
        current = datetime.now()
        currTime = current.strftime("%H:%M")
        splcurrTime = currTime.split(":")
        hour = splcurrTime[0]
        minute = splcurrTime[1]
        curTime = hour+minute
        
        print(curTime)
        if curTime == alarmTime:
            print("Alarm Target Hit")
            playsound('/Users/stephenagberien/Desktop/songs/Buju.mp3')
            break
    return

if __name__ == "__main__":
    alarmTime = setAlarmTime()
    isAlarmTime(alarmTime)