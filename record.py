import cv2

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')


# Open the default camera
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while cv2.getWindowProperty('Facecam', 0) >= 0:
    cv2.waitKey(50)
    ret, frame = cap.read()
    if not ret:
        break

    # Write the frame into the file 'output.avi'


    # Display the resulting frame
    cv2.imshow('Facecam', frame)

    # Press 'q' on the keyboard to exit the recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
