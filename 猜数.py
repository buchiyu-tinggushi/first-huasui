""" 用python设计第一个游戏 """
import random


counts = 3
a = random.randint(1, 10)

while counts > 0:
    temp = input("不妨猜一下不吃鱼在心里想的是哪个数字：")
    guess = int(temp)

    if guess == a:
        print("你是不吃鱼心里的蛔虫嘛？！")
        print("哼，猜中了也没奖励")
        break
    else:
        if guess > a:
            print("大了")
        else:
            print('小了')
        counts = counts - 1
print("游戏结束，不玩了哈哈")
