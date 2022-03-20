import os
import face_recognition
import cv2
import numpy as np

path = 'TrainingData'
if not os.path.exists(path):
    os.mkdir(path)
images = []
class_names = []
encode_list = []
TimeList1 = []
TimeList2 = []
attendance_list = os.listdir(path)

for cl in attendance_list:
    cur_img = cv2.imread(f'{path}/{cl}')
    images.append(cur_img)
    class_names.append(os.path.splitext(cl)[0])
for img in images:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(img)
    encodes_cur_frame = face_recognition.face_encodings(img, boxes)[0]
    encode_list.append(encodes_cur_frame)


np.save("main/img_metrix", encode_list)
np.save("main/classes", class_names)

print("Trained")
