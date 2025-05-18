# and
# or
# not
# ==
# !=
# >
# <
# >=
# <=
# is
# is not
# in
# not in

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