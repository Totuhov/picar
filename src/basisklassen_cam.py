# coding=utf-8
#!/usr/bin/env python
'''
    Information: Module mit Basisklasse für Camera für Projekt RPiCar
    File name: basisklassen_cam.py
    Author: Robert Heise (FIDA)
    Date created: 11/10/2021
    Date last modified: 20/06/2022
    Python Version: 3.9
    Usage: Basisklassen U4I/FIDA "Autonomens Fahren" mit Sunfounder PiCar-S Projektphase 2
'''


#import click
#import time
import numpy as np

import cv2

class Camera(object):
    """ Klasse für die Abfrage der Kamera mittels OpenCV

    Args:
        devicenumber int: Identifier for camera (OpenCV VideoCapture)
        buffersize int : Größe des Videobuffers (OpenCV VideoCapture)
        skip_frame int : Anzahl der zu verwerfenden Bilder bei Ausführung von get_frame
        height, width int: Höhe und Breite des Bildes
        flip bool: vertical flip of taken image
        colorspace str: Verwendeter Farbraum ('bgr','rgb', 'gray')
    Methoden: 
        get_frame: Rückgabe eines Bildes als np.array unter Verwendung von skip_frame
        get_jpeg: Rückgabe eines Bildes als jpeg 
        release: Freigabe der Kamera
        get_size (int,int): Rückgabe des Bildgröße
        get_size: Rückgabe der verwendeten Bildgröße
        check bool: Rückgabe von True wenn Kamera erreichbar
        
    """
    def __init__(self,devicenumber : int = 0, buffersize : int = 1, skip_frame : int = 2, 
                 height : int = None, width : int = None,flip : bool = True, colorspace : str = None) -> None:
        self.__skip_frame = skip_frame
        self.__devicenumber = devicenumber
        self.__VideoCapture = cv2.VideoCapture(devicenumber) # wrong devidenumber -> Warning: can't open camera by index
        self.__imgsize = (int(self.__VideoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),int(self.__VideoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        if width:
            self.__VideoCapture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            self.__imgsize = (self.__imgsize[0],width)
        if height:
            self.__VideoCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
            self.__imgsize = (height,self.__imgsize[1])
        self.__VideoCapture.set(cv2.CAP_PROP_BUFFERSIZE,1)
        self.__flip = flip
        self.__colorspace = colorspace or 'bgr'
        
    def get_size(self) -> tuple:
        """
        Return size of image returned be get_frame
        """
        return self.__imgsize
    
    def get_frame(self) -> np.array:
        """
        Reads frame from camera, applies tranformations to it and returns die resulting frame
        """
        if self.__skip_frame:
            for i in range(int(self.__skip_frame)):
                _, frame = self.__VideoCapture.read()
        _, frame = self.__VideoCapture.read()
        if self.__flip:
            frame = cv2.flip(frame, -1)
        if self.__colorspace == 'rgb':
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        elif self.__colorspace == 'gray':
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        else:
            pass
        return frame
    
    def get_jpeg(self) -> np.array:
        """
        Reads frame from camera via get_frame and return the frame in jpg-format
        Primarily used for video-streaming
        """
        frame = self.get_frame()
        _,jpeg = cv2.imencode('.jpeg', frame)
        return jpeg

    def check(self) -> bool:
        """
        Test for accessibility of the camera
        """
        flag = self.__VideoCapture is not None and self.__VideoCapture.isOpened()
        return flag
        
    
    def release(self) -> None:
        """
        Releases camera and allows other processes to access it
        """
        self.__VideoCapture.release()


if __name__ == "__main__":

    cam = Camera()
    while True:
        img = cam.get_frame()
        cv2.imshow('image',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    print(' - camera released')
    cv2.destroyAllWindows()
