import cv2
import face_recognition
import os

if not os.path.exists("Register Face.png"):
    print("No registered face found")
    exit()

known_image = face_recognition.load_image_file("Register Face.png")
known_encoding = face_recognition.face_encodings(known_image)[0]

cam = cv2.VideoCapture(0)

print("Show your face to unlock")

while True:
    ret, frame = cam.read()
    if not ret:
        continue

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    for face_encoding in face_encodings:
        match = face_recognition.compare_faces(
            [known_encoding],
            face_encoding,
            tolerance=0.5
        )

        if match[0]:
            print("Face matched. Access granted")
            cam.release()
            cv2.destroyAllWindows()
            exit()

    cv2.imshow("Face Unlock", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()