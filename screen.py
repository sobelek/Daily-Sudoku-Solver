import cv2
import numpy as np
import tensorflow._api.v1.keras as tf
from solver import *
import pyscreenshot as ImageGrab
import time
import pyautogui

pyautogui.hotkey('alt', 'tab')
time.sleep(2)
scrren = ImageGrab.grab(backend='pyqt5')

img_np = np.array(scrren)

img = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

font = cv2.FONT_HERSHEY_COMPLEX
cropped = img[650:1600, 1000:2000]
sudoku = ''
_, threshold = cv2.threshold(cropped, 127, 255, cv2.THRESH_BINARY)
contours,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
model = tf.models.load_model('number_model.model')
position = 0
boxes = []
offset = 40
for cnt in contours:

    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)

    if len(approx) == 4:
        x, y, width, height = cv2.boundingRect(cnt)
        if 150 > width > 50:
            boxes.append([x + 1000, y + 650])
            roi = cropped[y:y + height, x:x + width]
            roi = cv2.resize(roi, (30, 30))
            roi = roi.reshape(-1, 30, 30, 1)

            prediction = model.predict(roi)
            prediction = prediction[0]
            for pred in prediction:
                if pred == 1.0:
                    sudoku = sudoku + str(position)
                position = position + 1
            position = 0


sudoku = " ".join(sudoku)
sudoku = sudoku[::-1]
boxes = boxes[::-1]
problem = Sudoku(sudoku)
result = Sudoku(solve(problem))
result = str(result).replace(' ', '').replace('\n', '').lstrip()
pyautogui.click(x=boxes[0][0], y=boxes[0][1] - 50)
for solution, position in zip(result, boxes):
    pyautogui.press(solution)
    pyautogui.click(x=position[0] + offset, y=position[1] + offset)
    print(solution)
cv2.destroyAllWindows()