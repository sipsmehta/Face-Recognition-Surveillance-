from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer, QDate, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QPushButton

from qt_material import apply_stylesheet

import cv2
import face_recognition
import numpy as np
import os
import csv
import sys
import datetime as dt
from PIL import Image

format = '%Y-%m-%d %H:%M'

guard_ui = "ui/guard.ui"
main_ui = "ui/login.ui"
student_ui = "ui/student_view.ui"

camera = "1"
