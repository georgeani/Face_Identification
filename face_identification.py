import cv2


def face_identification(names):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    font = cv2.FONT_HERSHEY_SIMPLEX
    cap = cv2.VideoCapture(0)


    while True:
        # Read the frame
        _, img = cap.read()
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        confidence = 0
        res = ''

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            if 100 >= confidence:
                res = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                res = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            cv2.putText(
                img,
                res,
                (x + 5, y - 5),
                font,
                1,
                (255, 255, 255),
                2
            )
            cv2.putText(
                img,
                str(confidence),
                (x + 5, y + h - 5),
                font,
                1,
                (255, 255, 0),
                1
            )

        # Display
        cv2.imshow('img', img)
        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    # Release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()
    quit()
