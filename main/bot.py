from cv2 import cv2
import mss
import numpy as np
import os
import time
from pynput import mouse, keyboard
import random
import pydirectinput


class Fighter:
    def __init__(self):
        self.stc = mss.mss()

        path = os.path.dirname(os.path.dirname(__file__))
        self.img_path = os.path.join(path, 'img')
        self.mouse = mouse.Controller()
        self.keyboard = keyboard.Controller()
        self.bar_top = 0
        self.bar_left = 0

        # Increase this limit if you have a larger basket
        self.fish_count = 0
        self.fish_limit = 6
        self.keep_fishing = True
		
        # Adding spot to update sell thresholds!
        self.sell_threshold = .8

