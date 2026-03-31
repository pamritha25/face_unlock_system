import cv2
cam = cv2.VideoCapture(0)
print("Press S to save your face")
print("Press Q to quit")
while True:
    ret, frame = cam.read()
    if not ret:
        continue
    cv2.imshow("Register Face", frame)
    key = cv2.waitKey(1)
    if key ==ord("s"):
        cv2.imwrite("Register Face.png",frame)
        print("Face saved successfully")
        break
    if key == ord("q"):
        break
cam.relrease()
cv2.destroyAllwindows()


