Dependencies
OpenCV (cv2): Used for capturing video from the webcam and for face and eye detection using Haar cascades.
Multiprocessing (multiprocessing): Utilized to run the webcam capture and logging processes concurrently.
Matplotlib (matplotlib): Used for visualization purposes, including plotting the analysis results.

###Usage###
Run the script.
Ensure that a webcam is connected and functioning properly.
The script will display the webcam feed with detected faces and eyes.
Analysis results will be printed in the console.
Log files containing analysis data will be generated for further analysis.

Notes
Haar cascade classifiers (haarcascade_frontalface_default.xml and haarcascade_eye_tree_eyeglasses.xml) are used for face and eye detection. Make sure these files are present in the working directory or provide correct paths to them.
Modify the code to adjust parameters such as the scale factor and minimum neighbors for better face and eye detection based on your requirements.

###Author###
This script was created by an anonymous author for educational and research purposes.
