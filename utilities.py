import numpy as np
import random
from sklearn import preprocessing
import csv
#import torch
import time
import cv2
import mss
import numpy
import pyautogui
from time import sleep


class DataGrabber():
    """gets data and processes ready to use"""

    def __init__(self):
        
        self.love = 14


    def toarray(self, x):
        x = np.array(x, dtype=np.float32)
        return x


    def get_screen(self):
        with mss.mss() as sct:
            # Part of the screen to capture
            monitor = {"top": 40, "left": 0, "width": 800, "height": 640}

            while "Screen capturing":
                last_time = time.time()

                # Get raw pixels from the screen, save it to a Numpy array
                img = numpy.array(sct.grab(monitor))

                # Display the picture
                cv2.imshow("OpenCV/Numpy normal", img)

                # Display the picture in grayscale
                # cv2.imshow('OpenCV/Numpy grayscale',
                #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

                print("fps: {}".format(1 / (time.time() - last_time)))

                # Press "q" to quit
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()
                    break

    def get_screen_array(self, top, left, width, height):
            sct = mss.mss()
            monitor = {"top": top, "left": left, "width": width, "height": height}

            img = numpy.array(sct.grab(monitor))
            #cv2.imshow("OpenCV/Numpy normal", img)
            #cv2.imshow('image',img)
            #sleep(0.1)
            #cv2.waitKey(25)
            #cv2.destroyAllWindows()
            return img

    def get_screen_img_show(self, grey):
        with mss.mss() as sct:
            monitor = {"top": 40, "left": 0, "width": 800, "height": 640}
            img = numpy.array(sct.grab(monitor))
            if grey == False:
                cv2.imshow("OpenCV/Numpy normal", img)
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()

            else:
                cv2.imshow('OpenCV/Numpy grayscale', cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()
            return img
