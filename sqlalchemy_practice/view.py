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
    return user_number


def isInDB(userNumber):
    if controller.checkDB(userNumber):
        print("you're number is exist. at {},{}".format("mainNum", "number"))
    else:
        print("you're number does not exist in DB...")
