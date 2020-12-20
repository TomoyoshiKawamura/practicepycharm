import random
import model
import logging

logger = logging.getLogger(__name__)


def save_random4number():
    # make random number 0000 ~ 9999
    for i in range(9999):
        random_4number = random.randint(0, 9999)
        # then random number into tuple
        model.save_number(random_4number)


# check match UserInputData And DBnumber
# then return mainKey,matchNumber

def checkDB(userNumber):
    dictDB = model.getDB()
    listValuesDB = list(dictDB.values())
    for value in listValuesDB:
        if userNumber == value:
            return True
    return False


def getSameNumberDB(userNumber):
    correctNumber = 0000
    dictDB = model.getDB()
    for value in dictDB.items():
        if userNumber == value[0]:
            correctNumber = value[0]
            try_number = value[1]
    return correctNumber,try_number
