

# agents = Agents()
# _viewport_ = Viewport()
# user_agent = agents.get_random_mobile()
# view = _viewport_.get_random_mobile()
# print(user_agent, view.landscapeWidth)


from os import kill
import signal
import subprocess
import sys
import threading
from time import sleep
from driver.driver import Driver
from appium.webdriver.common.appiumby import AppiumBy

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

def open_device(event):
    id = subprocess.call('sh', './new_device.sh')
def signal_handler(signal, frame, thread0:StoppableThread, thread1:StoppableThread):
    if thread0.is_alive():
        thread0.stop()
    if thread1.is_alive():
        thread1.stop()
    print('You pressed Ctrl+C!')
    sys.exit(0)
def main_testing(event=None):
    client = Driver().get_appium_driver()
    
    # Wait for app to load / **REPLACE WITH FUNCTION TO DETECT WHEN APP LOADS** /
    sleep(2)
    # Tap on the searchbar (the possible tappable things are found in the CLI option "list Clickable Nodes")
    client.tapNode("Wait")
    client.closeApp("com.android.settings")
    client.launchApp("com.android.settings")
    # client.tapNode("Search settings")
    # # client.tapNode("Google")
    # # input text to the search bar:
    # client.inputText("account")
    # client.keycodeEvent(keycode=84)
    client.pressHome()
    
    # swipe up a couple times
    # Demonstrate swipe options
    # client.inputSwipe(500, 800, 500, 400, 1000) # This represents a swipe up but slow
    # client.inputSwipe(50, 80, 50, 20, percent=True) # This represents a
    sleep(10)
if __name__ == '__main__':
   main_testing()