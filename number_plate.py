import cv2

harcascade = "model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640) # width
cap.set(4, 480) #height

min_area = 500
count = 0

