    # # import cv2
# # import mediapipe as mp
# # import pyautogui
# # cam = cv2.VideoCapture(0)
# # face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# # screen_w, screen_h = pyautogui.size()
# # while True:
# #     _, frame = cam.read()
# #     frame = cv2.flip(frame, 1)
# #     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #     output = face_mesh.process(rgb_frame)
# #     landmark_points = output.multi_face_landmarks
# #     frame_h, frame_w, _ = frame.shape
# #     if landmark_points:
# #         landmarks = landmark_points[0].landmark
# #         for id, landmark in enumerate(landmarks[474:478]):
# #             x = int(landmark.x * frame_w)
# #             y = int(landmark.y * frame_h)
# #             cv2.circle(frame, (x, y), 3, (0, 255, 0))
# #             if id == 1:
# #                 screen_x = screen_w * landmark.x
# #                 screen_y = screen_h * landmark.y
# #                 pyautogui.moveTo(screen_x, screen_y)
# #         left = [landmarks[145], landmarks[159]]
# #         for landmark in left:
# #             x = int(landmark.x * frame_w)
# #             y = int(landmark.y * frame_h)
# #             cv2.circle(frame, (x, y), 3, (0, 255, 255))
# #         if (left[0].y - left[1].y) < 0.01:
# #             pyautogui.click()
# #             pyautogui.sleep(1)
# #     cv2.imshow('Eye Controlled Mouse', frame)
# #     cv2.waitKey(1)


# import cv2
# import mediapipe as mp
# import pyautogui
# import time
# import datetime
# import speech_recognition as sr
# import os

# # Initialize Mediapipe and PyAutoGUI
# cam = cv2.VideoCapture(0)
# hands = mp.solutions.hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
# face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# mp_draw = mp.solutions.drawing_utils
# screen_w, screen_h = pyautogui.size()

# # Voice Assistant Function
# def voice_assistant():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         pyautogui.alert("Listening...", title="Voice Assistant")
#         audio = recognizer.listen(source)
#         try:
#             command = recognizer.recognize_google(audio).lower()
#             print(f"Command: {command}")
#             if "youtube" in command:
#                 os.system("start https://www.youtube.com")
#             elif "instagram" in command:
#                 os.system("start https://www.instagram.com")
#             elif "chatgpt" in command:
#                 os.system("start https://chat.openai.com")
#             elif "telegram" in command:
#                 os.system("start https://web.telegram.org")
#             elif "netflix" in command:
#                 os.system("start https://www.netflix.com")
#             elif "whatsapp" in command:
#                 os.system("start https://web.whatsapp.com")
#             elif "google" in command:
#                 os.system("start https://www.google.com")
#             elif "time" in command:
#                 current_time = datetime.datetime.now().strftime("%H:%M:%S")
#                 pyautogui.alert(f"Current Time: {current_time}", title="Time")
#             elif "date" in command:
#                 current_date = datetime.datetime.now().strftime("%Y-%m-%d")
#                 pyautogui.alert(f"Current Date: {current_date}", title="Date")
#             else:
#                 pyautogui.alert("Command not recognized", title="Error")
#         except sr.UnknownValueError:
#             pyautogui.alert("Sorry, I did not understand that.", title="Error")

# while True:
#     _, frame = cam.read()
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Process hands
#     hand_results = hands.process(rgb_frame)

#     # Process face landmarks for mouse control
#     face_results = face_mesh.process(rgb_frame)
#     frame_h, frame_w, _ = frame.shape

#     if face_results.multi_face_landmarks:
#         landmarks = face_results.multi_face_landmarks[0].landmark
#         for id, landmark in enumerate(landmarks[474:478]):
#             x = int(landmark.x * frame_w)
#             y = int(landmark.y * frame_h)
#             cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)
#             if id == 1:
#                 screen_x = screen_w * landmark.x
#                 screen_y = screen_h * landmark.y
#                 pyautogui.moveTo(screen_x, screen_y)

#         # Blink detection for left click
#         left_eye = [landmarks[145], landmarks[159]]
#         for landmark in left_eye:
#             x = int(landmark.x * frame_w)
#             y = int(landmark.y * frame_h)
#             cv2.circle(frame, (x, y), 3, (0, 255, 255), -1)
#         if (left_eye[0].y - left_eye[1].y) < 0.01:
#             pyautogui.click()
#             pyautogui.sleep(1)

#     # Detect hand gestures for additional operations
#     if hand_results.multi_hand_landmarks:
#         for hand_landmarks in hand_results.multi_hand_landmarks:
#             mp_draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
#             fingers = []
#             hand_type = "Right" if hand_landmarks.landmark[0].x > 0.5 else "Left"
            
#             for i, lm in enumerate(hand_landmarks.landmark):
#                 x, y = int(lm.x * frame_w), int(lm.y * frame_h)
#                 if i in [8, 12]:  # Index and middle fingertips
#                     fingers.append((x, y))

#             # Check gestures for the right hand
#             if hand_type == "Right":
#                 if len(fingers) == 2:  # Index and middle finger gesture
#                     if abs(fingers[0][1] - fingers[1][1]) < 10:  # Close distance for right click
#                         pyautogui.rightClick()
#                 elif len(fingers) == 1:  # Only index finger shown
#                     index_x, index_y = fingers[0]
#                     if index_x < frame_w // 2:  # Left side of the screen
#                         pyautogui.scroll(-10)  # Scroll down
#                     else:  # Right side of the screen
#                         pyautogui.scroll(10)  # Scroll up
#                 elif len(fingers) == 0:  # All fingers hidden except index of both hands
#                     voice_assistant()
            
#             # Check gestures for the left hand
#             elif hand_type == "Left":
#                 if len(fingers) == 2:  # Index and middle finger gesture
#                     if abs(fingers[0][1] - fingers[1][1]) < 10:  # Close distance
#                         pyautogui.keyDown("ctrl")
#                         pyautogui.scroll(10)  # Zoom in
#                         pyautogui.keyUp("ctrl")
#                 elif len(fingers) == 1:  # Only index finger shown
#                     index_x, index_y = fingers[0]
#                     if index_x < frame_w // 2:  # Left side of the screen
#                         pyautogui.scroll(10)  # Scroll up
#                     else:  # Right side of the screen
#                         pyautogui.scroll(-10)  # Scroll down
#                 elif len(fingers) == 0:  # All fingers hidden except index of both hands
#                     pyautogui.keyDown("alt")
#                     pyautogui.press("tab")  # Switch application
#                     pyautogui.keyUp("alt")

#     cv2.imshow("Hand and Eye Controlled System", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cam.release()
# cv2.destroyAllWindows()






# import cv2
# import mediapipe as mp
# import pyautogui
# import webbrowser
# import numpy as np
# import time
# import speech_recognition as sr
# from datetime import datetime
# from tkinter import Tk, Label

# cam = cv2.VideoCapture(0)
# hands = mp.solutions.hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
# face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# mp_draw = mp.solutions.drawing_utils
# screen_w, screen_h = pyautogui.size()

# smooth_x, smooth_y = 0, 0
# voice_recognition_active = False


# def activate_voice_recognition():
#     global voice_recognition_active

#     root = Tk()
#     root.title("Voice Recognition")
#     root.geometry("300x100")
#     label = Label(root, text="Voice Recognition Active!", font=("Arial", 14))
#     label.pack(pady=20)
#     root.update()

#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         try:
#             print("Listening...")
#             audio = recognizer.listen(source, timeout=5)
#             command = recognizer.recognize_google(audio).lower()
#             print(f"You said: {command}")

#             if "time" in command:
#                 now = datetime.now()
#                 pyautogui.alert(f"The current time is {now.strftime('%H:%M:%S')}")

#             elif "date" in command:
#                 today = datetime.today()
#                 pyautogui.alert(f"Today's date is {today.strftime('%Y-%m-%d')}")

#             elif "joke" in command:
#                 pyautogui.alert("Why don't skeletons fight each other? They don't have the guts!")

#             elif "youtube" in command:
#                 webbrowser.open("https://www.youtube.com")

#             elif "google" in command:
#                 webbrowser.open("https://www.google.com")

#             elif "facebook" in command:
#                 webbrowser.open("https://www.facebook.com")

#             elif "telegram" in command:
#                 webbrowser.open("https://web.telegram.org")

#             elif "whatsapp" in command:
#                 webbrowser.open("https://web.whatsapp.com")

#             elif "snapchat" in command:
#                 webbrowser.open("https://www.snapchat.com")

#             elif "x" in command:
#                 webbrowser.open("https://twitter.com")

#             elif "instagram" in command:
#                 webbrowser.open("https://instagram.com")

#             elif "leetcode" in command:
#                 webbrowser.open("https://leetcode.com")

#             elif "chatgpt" in command:
#                 webbrowser.open("https://chatgpt.com")

#             elif "netflix" in command:
#                 webbrowser.open("https://www.netflix.com")
            

#             else:
#                 pyautogui.alert("Sorry, I didn't understand that command.")

#         except sr.UnknownValueError:
#             pyautogui.alert("Sorry, I couldn't understand what you said.")

#         except sr.RequestError:
#             pyautogui.alert("Voice recognition service is unavailable.")

#     root.destroy()
#     voice_recognition_active = False


# def smooth_coordinates(new_x, new_y, alpha=0.5):
#     global smooth_x, smooth_y
#     smooth_x = alpha * new_x + (1 - alpha) * smooth_x
#     smooth_y = alpha * new_y + (1 - alpha) * smooth_y
#     return int(smooth_x), int(smooth_y)

# def count_fingers(hand_landmarks, hand_type):
#     finger_states = []
#     fingertips = [8, 12, 16, 20]
#     thumb_tip = 4

#     if hand_landmarks:
#         for tip in fingertips:
#             if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
#                 finger_states.append(1)
#             else:
#                 finger_states.append(0)

#         if hand_type == "Right":
#             if hand_landmarks.landmark[thumb_tip].x > hand_landmarks.landmark[thumb_tip - 1].x:
#                 finger_states.append(1)
#             else:
#                 finger_states.append(0)
#         else:
#             if hand_landmarks.landmark[thumb_tip].x < hand_landmarks.landmark[thumb_tip - 1].x:
#                 finger_states.append(1)
#             else:
#                 finger_states.append(0)

#     return finger_states.count(1)


# def track_eyes_and_mouth(frame, landmarks):
#     global voice_recognition_active

#     frame_h, frame_w, _ = frame.shape

#     # Track mouth opening
#     upper_lip = landmarks[13]  # Upper lip landmark
#     lower_lip = landmarks[14]  # Lower lip landmark

#     upper_lip_y = int(upper_lip.y * frame_h)
#     lower_lip_y = int(lower_lip.y * frame_h)

#     mouth_opening = abs(lower_lip_y - upper_lip_y)  # Distance between lips

#     if mouth_opening > 60:  # Check if the mouth opening is wider than 6 cm
#         if not voice_recognition_active:
#             voice_recognition_active = True
#             activate_voice_recognition()


# while True:
#     _, frame = cam.read()
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     hand_output = hands.process(rgb_frame)
#     if hand_output.multi_hand_landmarks:
#         for hand_landmarks, hand_type in zip(hand_output.multi_hand_landmarks, hand_output.multi_handedness):
#             hand_label = hand_type.classification[0].label
#             mp_draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

           
#             finger_count = count_fingers(hand_landmarks, hand_label)

            
#             if hand_label == "Right":
#                 if finger_count == 5:
#                     pyautogui.press("volumeup")
#                 elif finger_count == 4:
#                     pyautogui.scroll(30)
#                 elif finger_count == 3:
#                     pyautogui.rightClick()
#                 elif finger_count == 2:
#                     pyautogui.click()
#             elif hand_label == "Left":
#                 if finger_count == 5:
#                     pyautogui.press("volumedown")
#                 elif finger_count == 4:
#                     pyautogui.scroll(-30)
#                 elif finger_count == 3:
#                     pyautogui.leftClick()
#                 elif finger_count == 2:
#                     pyautogui.doubleClick()
#     face_output = face_mesh.process(rgb_frame)
#     if face_output.multi_face_landmarks:
#         landmarks = face_output.multi_face_landmarks[0].landmark
#         track_eyes_and_mouth(frame, landmarks)

#     cv2.imshow('Hand and Eye Gesture Control', frame)

#     if cv2.waitKey(1) & 0xFF == 27:  
#         break

# cam.release()
# cv2.destroyAllWindows()

# import cv2
# import mediapipe as mp
# import pyautogui
# import webbrowser
# import numpy as np
# import time
# import speech_recognition as sr
# from datetime import datetime
# from tkinter import Tk, Label

# cam = cv2.VideoCapture(0)
# hands = mp.solutions.hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
# face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# mp_draw = mp.solutions.drawing_utils
# screen_w, screen_h = pyautogui.size()

# smooth_x, smooth_y = 0, 0
# eye_closed_start_time = None
# voice_recognition_active = False


# def activate_voice_recognition():
#     global voice_recognition_active

  
#     root = Tk()
#     root.title("Voice Recognition")
#     root.title("Voice Recognition")
#     root.geometry("300x100") 
#     label = Label(root, text="Voice Recognition Active!", font=("Arial", 14))
#     label.pack(pady=20)
#     root.update()

#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         try:
#             print("Listening...")
#             audio = recognizer.listen(source, timeout=5)
#             command = recognizer.recognize_google(audio).lower()
#             print(f"You said: {command}")

#             if "time" in command:
#                 now = datetime.now()
#                 pyautogui.alert(f"The current time is {now.strftime('%H:%M:%S')}")

#             elif "date" in command:
#                 today = datetime.today()
#                 pyautogui.alert(f"Today's date is {today.strftime('%Y-%m-%d')}")

#             elif "joke" in command:
#                 pyautogui.alert("Why don't skeletons fight each other? They don't have the guts!")

#             elif "youtube" in command:
#                 webbrowser.open("https://www.youtube.com")

#             elif "google" in command:
#                 webbrowser.open("https://www.google.com")

#             elif "facebook" in command:
#                 webbrowser.open("https://www.facebook.com")

#             elif "telegram" in command:
#                 webbrowser.open("https://web.telegram.org")

#             elif "whatsapp" in command:
#                 webbrowser.open("https://web.whatsapp.com")

#             elif "snapchat" in command:
#                 webbrowser.open("https://www.snapchat.com")

#             elif "x" in command:
#                 webbrowser.open("https://twitter.com")

#             elif "instagram" in command:
#                 webbrowser.open("https://instagram.com")

#             elif "coder" in command:
#                 webbrowser.open("https://leetcode.com")

#             elif "chat gpt" in command:
#                 webbrowser.open("https://chatgpt.com")

#             elif "netflix" in command:
#                 webbrowser.open("https://www.netflix.com")
#             elif "w3schools" in command:
#                 webbrowser.open("https://w3schools.com")

#             else:
#                 pyautogui.alert("Sorry, I didn't understand that command.")

#         except sr.UnknownValueError:
#             pyautogui.alert("Sorry, I couldn't understand what you said.")

#         except sr.RequestError:
#             pyautogui.alert("Voice recognition service is unavailable.")

#     root.destroy()
#     voice_recognition_active = False
# def smooth_coordinates(new_x, new_y, alpha=0.5):
#     global smooth_x, smooth_y
#     smooth_x = alpha * new_x + (1 - alpha) * smooth_x
#     smooth_y = alpha * new_y + (1 - alpha) * smooth_y
#     return int(smooth_x), int(smooth_y)

# def count_fingers(hand_landmarks, hand_type):
#     finger_states = []
#     fingertips = [8, 12, 16, 20]
#     thumb_tip = 4

#     if hand_landmarks:
#         for tip in fingertips:
#             if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
#                 finger_states.append(1)
#             else:
#                 finger_states.append(0)

#         if hand_type == "Right":
#             if hand_landmarks.landmark[thumb_tip].x > hand_landmarks.landmark[thumb_tip - 1].x:
#                 finger_states.append(1)
#             else:
#                 finger_states.append(0)
#         else:
#             if hand_landmarks.landmark[thumb_tip].x < hand_landmarks.landmark[thumb_tip - 1].x:
#                 finger_states.append(1)
#             else:
#                 finger_states.append(0)

#     return finger_states.count(1)


# def track_eyes_and_control_cursor(frame, landmarks):
#     global eye_closed_start_time, voice_recognition_active

#     frame_h, frame_w, _ = frame.shape
#     for id, landmark in enumerate(landmarks[474:478]):
#         x = int(landmark.x * frame_w)
#         y = int(landmark.y * frame_h)
#         cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)
#         if id == 1:
#             screen_x, screen_y = smooth_coordinates(landmark.x * screen_w, landmark.y * screen_h)
#             pyautogui.moveTo(screen_x, screen_y)

#     left_eye = [landmarks[145], landmarks[159]]
#     for landmark in left_eye:
#         x = int(landmark.x * frame_w)
#         y = int(landmark.y * frame_h)
#         cv2.circle(frame, (x, y), 3, (0, 255, 255), -1)


# def track_eyes_and_mouth(frame, landmarks):
#     global voice_recognition_active

#     frame_h, frame_w, _ = frame.shape

#     # Track mouth opening
#     upper_lip = landmarks[13]  # Upper lip landmark
#     lower_lip = landmarks[14]  # Lower lip landmark

#     upper_lip_y = int(upper_lip.y * frame_h)
#     lower_lip_y = int(lower_lip.y * frame_h)

#     mouth_opening = abs(lower_lip_y - upper_lip_y)  # Distance between lips

#     if mouth_opening > 30:  # Check if the mouth opening is wider than 2 cm
#         if not voice_recognition_active:
#             voice_recognition_active = True
#             activate_voice_recognition()


# while True:
#     _, frame = cam.read()
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     hand_output = hands.process(rgb_frame)
#     if hand_output.multi_hand_landmarks:
#         for hand_landmarks, hand_type in zip(hand_output.multi_hand_landmarks, hand_output.multi_handedness):
#             hand_label = hand_type.classification[0].label
#             mp_draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

           
#             finger_count = count_fingers(hand_landmarks, hand_label)

            
#             if hand_label == "Right":
#                 if finger_count == 5:
#                     pyautogui.press("volumeup")
#                 elif finger_count == 4:
#                     pyautogui.scroll(30)
#                 elif finger_count == 3:
#                     pyautogui.rightClick()
#                 elif finger_count == 2:
#                     pyautogui.click()
#             elif hand_label == "Left":
#                 if finger_count == 5:
#                     pyautogui.press("volumedown")
#                 elif finger_count == 4:
#                     pyautogui.scroll(-30)
#                 elif finger_count == 3:
#                     pyautogui.leftClick()
#                 elif finger_count == 2:
#                     pyautogui.doubleClick()
#     face_output = face_mesh.process(rgb_frame)
#     if face_output.multi_face_landmarks:
#         landmarks = face_output.multi_face_landmarks[0].landmark
#         track_eyes_and_mouth(frame, landmarks)
#         track_eyes_and_control_cursor(frame, landmarks)
#     cv2.imshow('Hand and Eye Gesture Control', frame)

#     if cv2.waitKey(1) & 0xFF == 27:  
#         break

# cam.release()
# cv2.destroyAllWindows()




















# import cv2 #used for captuiring the video
# import mediapipe as mp#used for detecting the landmarks and tracking face mesh
# import pyautogui#used for performing the operations related to keyboard and mouse
# import webbrowser#enhance acessibility to open websites
# import numpy as np#array used for storing landmarks
# import time#inorder to provide the time
# import speech_recognition as sr#for voice recognition
# from datetime import datetime
# from tkinter import Tk, Label#To get the popup window 

# cam = cv2.VideoCapture(0)#default video capturing
# hands = mp.solutions.hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)#confidence value for get the accuracy
# face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)#facemesh for tracking the facial features and voice recognition
# mp_draw = mp.solutions.drawing_utils#draw the necessary util diagram
# screen_w, screen_h = pyautogui.size()

# rsmooth_x, smooth_y = 0, 0 #used for smooth processing of the cursor
# eye_closed_start_time = None
# voice_recognition_active = False

# def activate_voice_recognition():
#     global voice_recognition_active
#     root = Tk()
#     root.title("Voice Recognition")
#     root.geometry("300x100") 
#     label = Label(root, text="Voice Recognition Active!", font=("Arial", 14))
#     label.pack(pady=20)
#     root.update()

#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         try:
#             print("Listening...")
#             audio = recognizer.listen(source, timeout=5)
#             command = recognizer.recognize_google(audio).lower()
#             print(f"You said: {command}")

#             websites = {
#                 "youtube": "https://www.youtube.com",
#                 "google": "https://www.google.com",
#                 "facebook": "https://www.facebook.com",
#                 "telegram": "https://web.telegram.org",
#                 "whatsapp": "https://web.whatsapp.com",
#                 "snapchat": "https://www.snapchat.com",
#                 "x": "https://twitter.com",
#                 "instagram": "https://instagram.com",
#                 "coder": "https://leetcode.com",
#                 "chat gpt": "https://chatgpt.com",
#                 "netflix": "https://www.netflix.com",
#                 "w3schools": "https://w3schools.com"
#             }

#             if "time" in command:
#                 now = datetime.now()
#                 pyautogui.alert(f"The current time is {now.strftime('%H:%M:%S')}")
#             elif "date" in command:
#                 today = datetime.today()
#                 pyautogui.alert(f"Today's date is {today.strftime('%Y-%m-%d')}")
#             elif "joke" in command:
#                 pyautogui.alert("Why don't skeletons fight each other? They don't have the guts!")
#             elif command in websites:
#                 webbrowser.open(websites[command])
#             else:
#                 pyautogui.alert("Sorry, I didn't understand that command.")

#         except sr.UnknownValueError:
#             pyautogui.alert("Sorry, I couldn't understand what you said.")
#         except sr.RequestError:
#             pyautogui.alert("Voice recognition service is unavailable.")

#     root.destroy()
#     voice_recognition_active = False

# def smooth_coordinates(new_x, new_y, alpha=0.5):
#     global smooth_x, smooth_y
#     smooth_x = alpha * new_x + (1 - alpha) * smooth_x
#     smooth_y = alpha * new_y + (1 - alpha) * smooth_y
#     return int(smooth_x), int(smooth_y)

# def count_fingers(hand_landmarks, hand_type):
#     finger_states = []
#     fingertips = [8, 12, 16, 20]
#     thumb_tip = 4

#     if hand_landmarks:
#         for tip in fingertips:
#             finger_states.append(1 if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y else 0)
#         if hand_type == "Right":
#             finger_states.append(1 if hand_landmarks.landmark[thumb_tip].x > hand_landmarks.landmark[thumb_tip - 1].x else 0)
#         else:
#             finger_states.append(1 if hand_landmarks.landmark[thumb_tip].x < hand_landmarks.landmark[thumb_tip - 1].x else 0)
#     return finger_states.count(1)

# def track_eyes_and_control_cursor(frame, landmarks):
#     global eye_closed_start_time
#     frame_h, frame_w, _ = frame.shape
#     for id, landmark in enumerate(landmarks[474:478]):
#         x, y = int(landmark.x * frame_w), int(landmark.y * frame_h)
#         cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)
#         if id == 1:
#             screen_x, screen_y = smooth_coordinates(landmark.x * screen_w, landmark.y * screen_h)
#             pyautogui.moveTo(screen_x, screen_y)

#     left_eye = [landmarks[145], landmarks[159]]
#     left_eye_closed = abs(int(left_eye[0].y * frame_h) - int(left_eye[1].y * frame_h)) < 10

#     if left_eye_closed:
#         if eye_closed_start_time is None:
#             eye_closed_start_time = time.time()
#         elif time.time() - eye_closed_start_time > 1:
#             pyautogui.click()
#             eye_closed_start_time = None
#     else:
#         eye_closed_start_time = None

# def track_eyes_and_mouth(frame, landmarks):
#     global voice_recognition_active
#     frame_h, frame_w, _ = frame.shape
#     mouth_opening = abs(int(landmarks[13].y * frame_h) - int(landmarks[14].y * frame_h))
#     if mouth_opening > 30 and not voice_recognition_active:
#         voice_recognition_active = True
#         activate_voice_recognition()

# while True:
#     _, frame = cam.read()
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
#     hand_output = hands.process(rgb_frame)
#     if hand_output.multi_hand_landmarks:
#         for hand_landmarks, hand_type in zip(hand_output.multi_hand_landmarks, hand_output.multi_handedness):
#             hand_label = hand_type.classification[0].label
#             mp_draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
#             finger_count = count_fingers(hand_landmarks, hand_label)
            
#             if hand_label == "Right":
#                 if finger_count == 5:
#                     pyautogui.press("volumeup")
#                 elif finger_count == 4:
#                     pyautogui.scroll(30)
#                 elif finger_count == 3:
#                     pyautogui.rightClick()
#                 elif finger_count == 2:
#                     pyautogui.click()
#             elif hand_label == "Left":
#                 if finger_count == 5:
#                     pyautogui.press("volumedown")
#                 elif finger_count == 4:
#                     pyautogui.scroll(-30)
#                 elif finger_count == 3:
#                     pyautogui.leftClick()
#                 elif finger_count == 2:
#                     pyautogui.doubleClick()
    
#     face_output = face_mesh.process(rgb_frame)
#     if face_output.multi_face_landmarks:
#         landmarks = face_output.multi_face_landmarks[0].landmark
#         track_eyes_and_mouth(frame, landmarks)
#         track_eyes_and_control_cursor(frame, landmarks)
    
#     cv2.imshow('Hand and Eye Gesture Control', frame)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break

# cam.release()
# cv2.destroyAllWindows()


import cv2
import mediapipe as mp
import pyautogui
import webbrowser
import numpy as np
import time
import speech_recognition as sr
from datetime import datetime
from tkinter import Tk, Label

cam = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
mp_draw = mp.solutions.drawing_utils
screen_w, screen_h = pyautogui.size()

smooth_x, smooth_y = 0, 0
eye_closed_start_time = None
voice_recognition_active = False

def activate_voice_recognition():
    global voice_recognition_active
    root = Tk()
    root.title("Voice Recognition")
    root.geometry("300x100") 
    label = Label(root, text="Voice Recognition Active!", font=("Arial", 14))
    label.pack(pady=20)
    root.update()

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=50)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")

            websites = {
                "youtube": "https://www.youtube.com",
                "google": "https://www.google.com",
                "facebook": "https://www.facebook.com",
                "telegram": "https://web.telegram.org",
                "whatsapp": "https://web.whatsapp.com",
                "snapchat": "https://www.snapchat.com",
                "x": "https://twitter.com",
                "instagram": "https://instagram.com",
                "coder": "https://leetcode.com",
                "chat gpt": "https://chatgpt.com",
                "netflix": "https://www.netflix.com",
                "w3schools": "https://w3schools.com"
            }

            if "time" in command:
                now = datetime.now()
                pyautogui.alert(f"The current time is {now.strftime('%H:%M:%S')}")
            elif "date" in command:
                today = datetime.today()
                pyautogui.alert(f"Today's date is {today.strftime('%Y-%m-%d')}")
            elif "joke" in command:
                pyautogui.alert("Why don't skeletons fight each other? They don't have the guts!")
            elif command in websites:
                webbrowser.open(websites[command])
            else:
                pyautogui.alert("Sorry, I didn't understand that command.")

        except sr.UnknownValueError:
            pyautogui.alert("Sorry, I couldn't understand what you said.")
        except sr.RequestError:
            pyautogui.alert("Voice recognition service is unavailable.")

    root.destroy()
    voice_recognition_active = False

def smooth_coordinates(new_x, new_y, alpha=0.5):
    global smooth_x, smooth_y
    smooth_x = alpha * new_x + (1 - alpha) * smooth_x
    smooth_y = alpha * new_y + (1 - alpha) * smooth_y
    return int(smooth_x), int(smooth_y)

def count_fingers(hand_landmarks, hand_type):
    finger_states = []
    fingertips = [8, 12, 16, 20]
    thumb_tip = 4

    if hand_landmarks:
        for tip in fingertips:
            finger_states.append(1 if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y else 0)
        if hand_type == "Right":
            finger_states.append(1 if hand_landmarks.landmark[thumb_tip].x > hand_landmarks.landmark[thumb_tip - 1].x else 0)
        else:
            finger_states.append(1 if hand_landmarks.landmark[thumb_tip].x < hand_landmarks.landmark[thumb_tip - 1].x else 0)
    return finger_states.count(1)

def track_eyes_and_control_cursor(frame, landmarks):
    global eye_closed_start_time
    frame_h, frame_w, _ = frame.shape
    for id, landmark in enumerate(landmarks[474:478]):
        x, y = int(landmark.x * frame_w), int(landmark.y * frame_h)
        cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)
        if id == 1:
            screen_x, screen_y = smooth_coordinates(landmark.x * screen_w, landmark.y * screen_h)
            pyautogui.moveTo(screen_x, screen_y)

    left_eye = [landmarks[145], landmarks[159]]
    left_eye_closed = abs(int(left_eye[0].y * frame_h) - int(left_eye[1].y * frame_h)) < 10

    if left_eye_closed:
        if eye_closed_start_time is None:
            eye_closed_start_time = time.time()
        elif time.time() - eye_closed_start_time > 1:
            pyautogui.click()
            eye_closed_start_time = None
    else:
        eye_closed_start_time = None

def track_eyes_and_mouth(frame, landmarks):
    global voice_recognition_active
    frame_h, frame_w, _ = frame.shape
    mouth_opening = abs(int(landmarks[13].y * frame_h) - int(landmarks[14].y * frame_h))
    if mouth_opening > 10 and not voice_recognition_active:
        voice_recognition_active = True
        # activate_voice_recognition()

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    hand_output = hands.process(rgb_frame)
    if hand_output.multi_hand_landmarks:
        for hand_landmarks, hand_type in zip(hand_output.multi_hand_landmarks, hand_output.multi_handedness):
            hand_label = hand_type.classification[0].label
            mp_draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
            finger_count = count_fingers(hand_landmarks, hand_label)
            
            if hand_label == "Right":
                if finger_count == 5:
                    pyautogui.press("volumeup")
                elif finger_count == 4:
                    pyautogui.scroll(30)
                elif finger_count == 3:
                    pyautogui.rightClick()
                elif finger_count == 2:
                    pyautogui.click()
            elif hand_label == "Left":
                if finger_count == 5:
                    pyautogui.press("volumedown")
                elif finger_count == 4:
                    pyautogui.scroll(-30)
                elif finger_count == 3:
                    pyautogui.leftClick()
                elif finger_count == 2:
                    pyautogui.doubleClick()
    
    face_output = face_mesh.process(rgb_frame)
    if face_output.multi_face_landmarks:
        landmarks = face_output.multi_face_landmarks[0].landmark
        track_eyes_and_mouth(frame, landmarks)
        track_eyes_and_control_cursor(frame, landmarks)
    
    cv2.imshow('Hand and Eye Gesture Control', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()