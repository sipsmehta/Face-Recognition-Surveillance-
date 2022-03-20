from PIL import Image
import datetime as dt
import sys
import csv
import os
import numpy as np
import face_recognition
import cv2
from copyreg import pickle
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer, QDate, Qt, QDateTime
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QPushButton

# from qt_material import apply_stylesheet
import pickle

import mysql.connector as sq

format = '%Y-%m-%d %H:%M'

guard_ui = "ui/guard.ui"
main_ui = "ui/login.ui"
student_ui = "ui/student_view.ui"
warden_ui = "ui/warden_view.ui"

camera = "1"

cn = sq.connect(username="admin", password="sih",
                host="localhost", database='sih_main')
if cn.is_connected() == False:
    print("not connected")
else:
    print("Connection successful")
mc = cn.cursor()
