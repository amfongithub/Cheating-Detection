import cv2
import multiprocessing
from multiprocessing import Process
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
matplotlib.use('TkAgg')  # or any other backend that works for you
from matplotlib.animation import FuncAnimation
from itertools import count
    
import time
import csv

import sys
from logger import log, initlogger


def exam():
    cap = cv2.VideoCapture(0)  # Use index 0 for the default webcam
    faces, eyes = [], []

    frame_no = 0
    look_screen = 0
    look_away = 0
    suspicious_behavior = 0
    
    frame_no_array = []
    status_array = []
    elapsed_time_array = []

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
            nilai = status_array
            
            
            # count_0 = nilai.count(0)
            # count_1 = nilai.count(1)
            # count_2 = nilai.count(2)
            # # hasil_perhitungan = len(elapsed_time_array)
            
            # # data = [10, 20, 30, 40, 50]

            # # Menghitung jumlah data
            # # jumlah_data = len(nilai)

            # # Menghitung total nilai dari semua data
            # total_nilai = sum(nilai)

            # # Menghitung persentase setiap data terhadap total nilai
            # # persentase_data = [(nilai / total_nilai) * 100 for nilai in nilai]
            
            # persentase_data_0 = []
            # persentase_data_1 = []
            # persentase_data_2 = []
            
            # if total_nilai != 0:
            #     persentase_data_0 = [(count_0 / total_nilai) * 100  for nilai in nilai]
            #     persentase_data_1 = [(count_1 / total_nilai) * 100  for nilai in nilai]
            #     persentase_data_2 = [(count_2 / total_nilai) * 100  for nilai in nilai]
            #      # Menampilkan hasil
            #     # print("Jumlah data:", jumlah_data)
            #     # print("Total nilai:", total_nilai)
            #     # print("Persentase setiap data terhadap total nilai:")
            #     for i, persentase_data_0 in enumerate(persentase_data_0):
            #         ctk0 = (f"Fokus:{persentase_data_0:.2f}%")
            #     for i, persentase_data_1 in enumerate(persentase_data_1):
            #         ctk1 = (f"Menoleh:{persentase_data_1:.2f}%")
            #     for i, persentase_data_2 in enumerate(persentase_data_2):
            #         ctk2 = (f"Curang:{persentase_data_2:.2f}%")
            
            
            count_0 = nilai.count(0)
            count_1 = nilai.count(1)
            count_2 = nilai.count(2)

            total_nilai = sum(nilai)

            # Calculate percentages
            persentase_data_0 = (count_0 / len(nilai)) * 100 if total_nilai != 0 else 0
            persentase_data_1 = (count_1 / len(nilai)) * 100 if total_nilai != 0 else 0
            persentase_data_2 = (count_2 / len(nilai)) * 100 if total_nilai != 0 else 0

            # Normalize percentages to 100%
            total_persentase = persentase_data_0 + persentase_data_1 + persentase_data_2
            if total_persentase > 100:
                normalization_factor = 100 / total_persentase
                persentase_data_0 *= normalization_factor
                persentase_data_1 *= normalization_factor
                persentase_data_2 *= normalization_factor

            # Prepare texts
            ctk0 = f"Fokus: {persentase_data_0:.2f}%" if total_nilai != 0 else "Fokus: 0.00%"
            ctk1 = f"Menoleh: {persentase_data_1:.2f}%" if total_nilai != 0 else "Menoleh: 0.00%"
            ctk2 = f"Curang: {persentase_data_2:.2f}%" if total_nilai != 0 else "Curang: 0.00%"
                    
                    
            image = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
                # text = "Fokus : 33% \n Menoleh: 33% \n Curang: 33%"
                # y0, dy = 80, 20
                # cv2.putText(image, text,  (x-4, y-1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)
                
            var_fcs = "{}".format(ctk0) # nilai mau dicek berkala lalu di cetak
            var_look_away = "{}".format(ctk1) # nilai mau dicek berkala lalu di cetak
            var_ind_spcs = "{}".format(ctk2) # nilai mau dicek berkala lalu di cetak 
                
            fontFace = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)  # Blue color
            thickness = 2
            org = (50, 50)  # Bottom-left corner of the text
                
                
                
                # cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(image, var_fcs, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2, cv2.LINE_AA)
                # You can add more objects and their corresponding labels here
                # For example, you can add eyes, mouth, etc.
            cv2.putText(image, var_look_away, (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.putText(image, var_ind_spcs, (x, y-50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2, cv2.LINE_AA)

            #     # Put the text on the image
            #     # cv2.putText(image, text, org, fontFace, fontScale, color, thickness)
            # else:
            #     # Handle the case where total_nilai is zero, for example:
            #     print("Total nilai is zero. Unable to calculate percentages.")

               
            
            
                
            
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

            # data_array = [[1, 'John', 'New York'],[2, 'Jane', 'Los Angeles'],[3, 'Doe', 'Chicago']]
            # def simpan_ke_csv(nama_file, data):
            # # Tulis data ke dalam file CSV
            #     with open(nama_file, 'a', newline='') as file:  # Mode 'a' untuk menambahkan data ke file yang sudah ada
            #         writer = csv.writer(file)
            #         for row in data:
            #             writer.writerow(row)
            #             print("Data berhasil ditambahkan ke", nama_file)
            # # Panggil fungsi untuk menyimpan data ke dalam file CSV
            # simpan_ke_csv('data.csv', data_array)

            # frame_no_array = []
            # status_array = []
            # elapsed_time_array = []
            for (x, y, w, h) in faces:
                # Calculate face center
                face_center_x = x + w // 2
                face_center_y = y + h // 2

                lihat_kertas = '';
                menoleh = '';
                dicurigai = '';

                look_paper = 0
                away_look = 1
                chatting_indc = 2



                # Check if the face is looking down
                if face_center_y > frame.shape[0] * 2 // 3:
                    # print("STATUS ", frame_no, " : fokus di lembar jawaban")
                    look_screen += 1
                    while look_screen < 10000:
                        look_screen += 1
                    end_time = time.time()  # Membuat timestamp akhir
                    elapsed_time = end_time - start_time  # Menghitung selisih waktu
                    lihat_kertas = frame_no, look_paper,elapsed_time
                    frame_no_array.append(frame_no)
                    status_array.append(look_paper)
                    elapsed_time_array.append(elapsed_time)
                    
                else:
                    # print("STATUS ", frame_no, " : siswa melihat diluar lembar jawaban (tidak fokus)")
                    look_away += 1
                    while look_away < 10000:
                        look_away += 1
                    end_time = time.time()  # Membuat timestamp akhir
                    elapsed_time = end_time - start_time  # Menghitung selisih waktu
                    menoleh = frame_no,away_look,elapsed_time
                    frame_no_array.append(frame_no)
                    status_array.append(away_look)
                    elapsed_time_array.append(elapsed_time)

                # Check if the face is shifted left or right
                if face_center_x < frame.shape[1] // 3 or face_center_x > frame.shape[1] * 2 // 3:
                    # print("STATUS ", frame_no, " : Pergerakan mencurigakan (Dicurigai menyontek)")
                    suspicious_behavior += 1
                    while suspicious_behavior < 10000:
                        suspicious_behavior += 1
                    end_time = time.time()  # Membuat timestamp akhir
                    elapsed_time = end_time - start_time  # Menghitung selisih waktu
                    dicurigai = frame_no,chatting_indc,elapsed_time
                    frame_no_array.append(frame_no)
                    status_array.append(chatting_indc)
                    elapsed_time_array.append(elapsed_time)
            
                print([status_array],[elapsed_time_array],'\n')
        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
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
    # log_process = Process(target=p2)

    print("Sistem dipersiapkan...")
    sys.stdout.flush()
    time.sleep(1)

    exam_process.start()
    time.sleep(2)

    initlogger()

    # log_process.start()

    exam_process.join()

    # if not exam_process.is_alive():
    #     log_process.terminate()

    # print("\nBlue line = frame number\nGreen line = number of time screen look")
    # print("Orange line = number of time away look")