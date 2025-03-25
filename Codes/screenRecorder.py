import cv2
import numpy as np
import pyautogui
import datetime as dt
import os
#
# Set the screen size 87
screen_size = pyautogui.size()

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# Get the current time and format it
timestamp = dt.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

# Define the file path for saving the video
save_path = os.path.join("C:\\path\\to\\save\\directory", f"screen_record_{timestamp}.avi")

out = cv2.VideoWriter(f"screen_record_{timestamp}.avi", fourcc, 20.0, (screen_size.width, screen_size.height))

# Flag to control recording state
is_recording = True

try:
    while True:
        # Capture the screen
        img = pyautogui.screenshot()
        
        # Convert the screenshot to a numpy array
        frame = np.array(img)
        
        # Convert it from BGR(Blue, Green, Red) to RGB(Red, Green, Blue)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Get the current time and format it
        timestamp = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Define the font, size, and color for the timestamp
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        color = (255, 255, 255)  # White color
        thickness = 2
        position = (10, screen_size.height - 10)  # Bottom-left corner
        
        
        # Write the frame to the video file if recording is active
        if is_recording:
            out.write(frame)
        
        # Optional: Display the recording screen
        cv2.imshow('Live', frame)
        
        # Check for key presses
        key = cv2.waitKey(1)
        if key == ord('q') or key == ord('Q') and is_recording == False:
            break
        elif key == ord('p') or key == ord('P'):
            # Toggle recording state
            is_recording = not is_recording

finally:
    # Release the VideoWriter object and close all OpenCV windows
    out.release()
    cv2.destroyAllWindows()