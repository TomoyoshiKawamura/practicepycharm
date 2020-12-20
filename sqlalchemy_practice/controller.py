import random
import model
import logging

logger = logging.getLogger(__name__)


def save_random4number():
    # make random number 0000 ~ 9999
    for i in range(10):
        random_4number = random.randint(0000, 9999)
        # then random number into tuple
        model.save_number(random_4number)


# check match UserInputData And DBnumber
# then return mainKey,matchNumber

def checkDB(userNumber):
    dictDB = model.getDB()
    for i in dictDB:
        if userNumber in dictDB.values():
            getSameNumberDB(userNumber, dictDB)
        else:
            return False


def getSameNumberDB(userNumber, dictDB):
    for i in dictDB.keys():
        if userNumber == dictDB.values():
            correctNumber = dictDB.values()
    return correctNumber
