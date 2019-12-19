#main file for anything
import time
import random
from multiprocessing import Process
from threading import Thread, Event
from sys import exit

# import the files
from christmasTree import treeFunction
from christmasStar import starFunction
from christmasSanta import santaFunction
from christmasText import hohohoFunction

import unicornhathd

#rotate
unicornhathd.rotation(-90);

# get size
width, height = unicornhathd.get_shape()

#lets loop this forever
try:
    while True:
        # Christmas tree
        action_thread = Process(target=treeFunction, args=(width, height, unicornhathd))
        action_thread.start()
        action_thread.join(timeout=600)
        action_thread.terminate()
        # Christmas Star
        action_thread = Process(target=starFunction, args=(width, height, unicornhathd))
        action_thread.start()
        action_thread.join(timeout=600)
        action_thread.terminate()
        # Christmas Santa
        action_thread = Process(target=santaFunction, args=(width, height, unicornhathd))
        action_thread.start()
        action_thread.join(timeout=600)
        action_thread.terminate()
        # Christmas Text
        action_thread = Process(target=hohohoFunction, args=(width, height, unicornhathd))
        action_thread.start()
        action_thread.join(timeout=600)
        action_thread.terminate()
        
except KeyboardInterrupt:
    unicornhathd.off()
    exit
