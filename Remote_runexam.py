import cv2
import multiprocessing
from multiprocessing import Process
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
matplotlib.use('TkAgg')  # or any other backend that works for you

import time
import csv

import sys
from logger import log, initlogger
from line import liner
from analysis import analysisCSV

def exam():
    cap = cv2.VideoCapture(0)  # Use index 0 for the default webcam
    faces, eyes = [], []

    frame_no = 0
    look_screen = 0
    look_away = 0
    suspicious_behavior = 0

    start_time = time.time()

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    eyesCascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Couldn't read frame")
            break

        frame_no += 1
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.25,
            minNeighbors=9,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            # Detect eyes within the face region
            eyes = eyesCascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.22,
                minNeighbors=7,
                minSize=(30, 30)
            )

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(frame, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (138,43,226), 2)

        # Analyze face direction for suspicious behavior
        if len(faces) >= 1:
            for (x, y, w, h) in faces:
                # Calculate face center
                face_center_x = x + w // 2
                face_center_y = y + h // 2

                # Check if the face is looking down
                if face_center_y > frame.shape[0] * 2 // 3:
                    print("STATUS ", frame_no, " : fokus di lembar jawaban")
                    look_screen += 1
                    
                else:
                    # print("STATUS ", frame_no, " : siswa melihat diluar lembar jawaban (tidak fokus)")
                    look_away += 1
                    while look_away < 1000000:
                        look_away += 1
                    end_time = time.time()  # Membuat timestamp akhir
                    elapsed_time = end_time - start_time  # Menghitung selisih waktu
                    print("STATUS ", frame_no, " : siswa melihat diluar lembar jawaban (tidak fokus)","dengan durasi", elapsed_time,"detik")

                # Check if the face is shifted left or right
                if face_center_x < frame.shape[1] // 3 or face_center_x > frame.shape[1] * 2 // 3:
                    # print("STATUS ", frame_no, " : Pergerakan mencurigakan (Dicurigai menyontek)")
                    suspicious_behavior += 1
                    while suspicious_behavior < 1000000:
                        suspicious_behavior += 1
                    end_time = time.time()  # Membuat timestamp akhir
                    elapsed_time = end_time - start_time  # Menghitung selisih waktu
                    print("STATUS ", frame_no, " : Pergerakan mencurigakan (Dicurigai menyontek)", "dengan durasi", elapsed_time,"detik")


        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    # Print analysis results
    print("Total frames analyzed:", frame_no)
    print("Number of times focused on exam:", look_screen)
    print("Number of times looking away:", look_away)
    print("Number of instances of suspicious behavior:", suspicious_behavior)

def p2():
    '''Creating a Log files about student analysis'''
    while True:
        log(glob[0], glob[1], glob[2])
        time.sleep(0.05)

if __name__ == '__main__':
    glob = multiprocessing.Array('i', 4)
    # 0th location contains frame_no 1st-> look_away 2nd -> look_screen

    exam_process = Process(target=exam)
    log_process = Process(target=p2)

    print("Preparing...")
    sys.stdout.flush()
    time.sleep(1)

    exam_process.start()
    time.sleep(2)

    initlogger()

    log_process.start()

    exam_process.join()

    if not exam_process.is_alive():
        log_process.terminate()

    print("\nBlue line = frame number\nGreen line = number of time screen look")
    print("Orange line = number of time away look")
    analysisCSV()
    liner('stdlog.csv')