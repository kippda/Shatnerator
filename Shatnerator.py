import time
import random

def toBoldlyGo(listOfStrings):
    ct = 0
    for word in listOfStrings:
        if ct == 3: #3 is an arbitrary number, it just can't be 0
            time.sleep(1.5)
            print('\n', word, end=" ")
            ct = random.randint(0,10)
            #I want lower odds of two newlines in a row
        else:
            time.sleep(.25)
            print(word, end=" ")
            ct = random.randint(0,6)

tmpStr = '''What you do not know and must be told is that my
    command orders on this subject are precise and inviolable.
    No act, no provocation'''

tmpList = tmpStr.split(" ")

toBoldlyGo(tmpList)
