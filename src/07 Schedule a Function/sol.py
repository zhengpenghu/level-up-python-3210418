# ```console
# >>> schedule_function(time.time() + 1, print, 'Howdy!')
# print() scheduled for Sun Aug 14 20:39:28 2022
# ```
# Then one second later...
# ```console
# Howdy!
# ```
import threading
import time
import sched


def schedule_function(scheduled_time, fun, args):
    print(f"{fun}() scheduled for {scheduled_time}")
    wait_time = scheduled_time - time.time()
    # threading.Timer(wait_time, fun, [args]).run()
    threading.Timer(wait_time, fun, [args]).start()
    print("hello")


def schedule_function2(scheduled_time, fun, args):
    print(f"{fun}() scheduled for {scheduled_time}")
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(scheduled_time, 0, fun, (args,))
    s.run()


if __name__ == '__main__':
    schedule_function(time.time() + 1, print, 'Howdy!')
    print("hello 2")

    schedule_function2(time.time() + 2, print, 'schedule_function2!')
