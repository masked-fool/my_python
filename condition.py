# and 与
# or 或
# not 非
# == 等于
# != 不等于
# > 大于
# < 小于
# >= 大于等于
# <= 小于等于
# is 是
# is not 不是
# in 在
# not in 不在

mood_index = int(input("对象今晚心情指数："))

if mood_index > 5 and mood_index < 10:
    print("今晚可以约对象出去玩")
    if mood_index > 7:
        print("今晚可以看电影")
    else:
        print("今晚可以逛街")
elif mood_index > 10:
    print("今晚可以约对象玩点别的")
else:
    print("今晚还是在家学习吧")