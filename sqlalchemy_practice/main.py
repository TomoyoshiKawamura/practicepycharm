"""
logging使いたい

メモリ上にDBを作成
1000回のランダム4桁をデータベースに保存する

ユーザーインプットを求める
そのデータベースの中から　ユーザーインプット数値があれば値を返す
（メインキーの情報もかえす）
"""

import view
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    view.prepareDB()
    view.prepareCompleteDB()
    userNumber = view.inputUserNumber()
    view.isInDB(userNumber)
