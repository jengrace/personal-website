from jengrace.mainpage.control import Control
import time

control = Control()


class TwitterDbUpdater():
    def work(self):
        time.sleep(60*10)
        while True:
            control.saveTweetsFromComments()
            print 'Database has been updated.'
            time.sleep(60*60*1)
