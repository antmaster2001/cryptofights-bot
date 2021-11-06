from cv2 import cv2
import mss
import numpy as np
import os
import time
from pynput import mouse, keyboard
import random
import pydirectinput


class Game:
    def __init__(self):
        self.stc = mss.mss()

        path = os.path.dirname(os.path.dirname(__file__))
        self.img_path = os.path.join(path, 'img')
        self.mouse = mouse.Controller()
        self.keyboard = keyboard.Controller()

        self.bar_top = 0
        self.bar_left = 0

    
