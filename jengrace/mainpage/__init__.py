import threading
from twitterDbUpdater import TwitterDbUpdater

def startup():
    # here you should import and instantiate updater and start it in a thread
    updater = TwitterDbUpdater()
    t = threading.Thread(target = updater.work)
    t.start()

startup()