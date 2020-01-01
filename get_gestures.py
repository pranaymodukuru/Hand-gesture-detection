# -*- coding: utf-8 -*-
import cv2
import os
import sys
import argparse
import numpy as np

parser = argparse.ArgumentParser()

parser.add_argument('--save_path', default = 'data', help='Path to save gesture images')
parser.add_argument('--gesture_name', default = 'default', help='Inner folder name representing gesture name')
parser.add_argument('--number', default=200, type=int, help='Number of images to capture')
parser.add_argument('--test_size', default=0.2, type=float, help='Percentage of images to be marked as Testing')

args = parser.parse_args()

gesture_name = args.gesture_name
num_captures = args.number

SAVE_PATH = args.save_path
CLASS_PATH = os.path.join(SAVE_PATH, gesture_name)

test_size = args.test_size

try:
    os.mkdir(SAVE_PATH)
except FileExistsError:
    pass

try:
    os.mkdir(CLASS_PATH)
except FileExistsError:
    filelist = [ f for f in os.listdir(CLASS_PATH) if f.endswith(".jpg") ]
    for f in filelist:
        os.remove(os.path.join(CLASS_PATH, f))
    print("{} directory already exists. Replacing existing files from this folder".format(CLASS_PATH))

cap = cv2.VideoCapture(0)

start = False
count = 0

while(True):
    ret, frame = cap.read()

    if not ret:
        continue
    if count == num_captures:
        break

    cv2.rectangle(frame, (100, 100), (400, 400), (255, 255, 255), 2)
    if start:
        roi = frame[100:400, 100:400]
        save_path = os.path.join(CLASS_PATH, '{}_{}.jpg'.format(gesture_name, count + 1))
        cv2.imwrite(save_path, roi)
        count += 1

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Collecting {}".format(count),
                (5, 50), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow("Collecting images", frame)

    k = cv2.waitKey(10)
    if k == ord('a'):
        start = not start

    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



images = []
for image_name in os.listdir(CLASS_PATH):
    images.append(image_name)

indices = np.random.permutation(len(images))
train_indices = indices[:int(indices.shape[0] * (1-test_size))]
test_indices = indices[int(indices.shape[0] * (1-test_size)):]

images = np.array(images)
train_images = images[train_indices]
test_images = images[test_indices]

path = CLASS_PATH
for img in train_images:
    os.rename(os.path.join(path, img), os.path.join(path, img.split('.')[0]+'_TR.'+img.split('.')[1]))

for img in test_images:
    os.rename(os.path.join(path, img), os.path.join(path, img.split('.')[0]+'_TE.'+img.split('.')[1]))

print(f"\nGestures for {gesture_name} successfully stored at {CLASS_PATH} with {test_size*100}% of them as test images.")
