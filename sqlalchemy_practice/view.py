import controller
import logging

logger = logging.getLogger(__name__)


def prepareDB():
    print("DBを準備しています・・・")
    controller.save_random4number()


def prepareCompleteDB():
    print("DBの準備が完了しました!")


def inputUserNumber():
    user_number = input("4桁の数字を入力してください!")
    user_number = int(user_number)
    return user_number


def isInDB(userNumber):
    if controller.checkDB(userNumber):
        correctNumber,tryNumber = controller.getSameNumberDB(userNumber)

        print("you're number is exist!! choose{}, at{}".format(correctNumber, tryNumber))
    else:
        print("you're number does not exist in DB...")
