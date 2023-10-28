import cv2
import time
import pygame

def play_audio(audio_file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    time.sleep(5)


with open('ip.txt', 'r') as file:
    ip = file.readline()    

droidcam_url = f"http://{ip}:4747/video"
audio_file = "assets/audio.wav"

video_stream = cv2.VideoCapture(droidcam_url)

cap = cv2.VideoCapture(0)   

background = None
motion_threshold = 100

# Define the coordinates for the ROI (Region of Interest)
x, y, width, height =   0, 240, 40, 40

# Create a window for the ROI
cv2.namedWindow("ROI", cv2.WINDOW_NORMAL)

# Read the initial frame to define the ROI
ret, initial_frame = video_stream.read()
roi = initial_frame[y:y + height, x:x + width]

while True:
    ret, frame = video_stream.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if background is None:
        background = gray
        continue

    frame_delta = cv2.absdiff(background, gray)
    thresh = cv2.threshold(frame_delta, 30, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    contours, _ = cv2.findContours(thresh[y:y + height, x:x + width].copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > motion_threshold:
            play_audio(audio_file)
            print("Ting Tong!")

    background = gray

    # Display the ROI in its own window
    # cv2.imshow("ROI", roi)
    cv2.imshow("Frame",frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

video_stream.release()
cv2.destroyAllWindows()
