import cv2

# Load pre-trained model for object detection (e.g., face detection)
# Here, we'll use the pre-trained Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Main function to capture webcam feed and count bounding boxes
def main():
    # Open webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detect faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        
        # Count the number of bounding boxes
        num_boxes = len(faces)
        
        # Draw bounding boxes and display count above each box
        for i, (x, y, w, h) in enumerate(faces, start=1):
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            text = f"Box {i}"
            cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2, cv2.LINE_AA)
        
        # Display the frame with bounding boxes
        cv2.imshow('Frame', frame)
        
        # Print the number of bounding boxes
        print("Number of bounding boxes:", num_boxes)
        
        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the webcam and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
