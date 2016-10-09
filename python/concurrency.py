"""Concurrency examples python."""

# Author: Daniel Dahlmeier <ddahlmeier@gmail.com>


import time
import threading


class CountdownThread(threading.Thread):

    def __init__(self, count):
        threading.Thread.__init__(self)
        self.count = count

    def run(self):
        while self.count > 0:
            print "Counting down", self. count
            self.count -= 1
            time.sleep(1)
        return


if __name__ == "__main__":
    t1 = CountdownThread(10)
    t1.start()
    t2 = CountdownThread(20)
    t2.start()
