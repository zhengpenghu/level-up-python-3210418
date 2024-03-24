from random import randrange
from datetime import datetime


def waiting_game():
    target = randrange(2, 4)
    print("Your target time is %s seconds" % target)
    enter_time = None
    cmd = input("---Press Enter to Begin---") # any cmd input always end with newline
    enter_time = datetime.now()

    input("...Press Enter again after %s seconds..." % target)
    delta = datetime.now() - enter_time
    print("Elapsed time: %s seconds" % delta.total_seconds())
    if delta.total_seconds() == target:
        print("right on target")
    elif delta.total_seconds() > target:
        print("(%s seconds too slow)" % (delta.total_seconds() - target))
    else:
        print("(%s seconds too fast)" % (target-delta.total_seconds()))


# commands used in solution video for reference
if __name__ == '__main__':
    waiting_game()
