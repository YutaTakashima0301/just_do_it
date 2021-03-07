import pynput
from pynput import mouse 
from pynput import keyboard
import time
import threading
import webbrowser
import sys
import signal


class JustDoIt():
    def __init__(self):
        self.WAIT_TIME = 60
        self.behavor_flag = False

    def _move(self, x, y):
        self.behavor_flag = True

    def _click(self, x, y, button, pressed):
        self.behavor_flag = True

    def _scroll(self, x, y, dx, dy):
        self.behavor_flag = True

    def _press(self, key):
        self.behavor_flag = True

    def _release(self, key):
        self.behavor_flag = True

    def main(self):
        while True:
            time.sleep(self.WAIT_TIME)
            if self.behavor_flag == True:
                self.behavor_flag = False
                continue
                
            if self.behavor_flag == False:
                webbrowser.open("https://www.youtube.com/watch?v=nwW4CDGucVs")
                continue


    def keyboard_listener_func(self):
        keyboard_listener = keyboard.Listener(
        on_press=self._press,
        on_release=self._release)
        keyboard_listener.start()

    def mouse_listener_func(self):
        mouse_listener = mouse.Listener(
        on_move=self._move,
        on_click=self._click,
        on_scroll=self._scroll)
        mouse_listener.start()

if __name__=='__main__':
    just_do_it = JustDoIt()
    thread_1 = threading.Thread(target=just_do_it.main)
    thread_2 = threading.Thread(target=just_do_it.keyboard_listener_func)
    thread_3 = threading.Thread(target=just_do_it.mouse_listener_func)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    thread_1.start()
    thread_2.start()
    thread_3.start()