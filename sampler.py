import os

import cv2

names = ['unknown']


def sample():
    users = int(input('Please enter the number of users that you want your model to train'))
    if users < 1:
        print('System failure')

    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # For each person, enter one numeric face id

    for i in range(1, users + 1):

        print("\n [INFO] Initializing face capture. Look the camera and wait ...")
        # Initialize individual sampling face count

        cap = cv2.VideoCapture(0)
        photos_taken = 0

        while True and photos_taken < 30:
            # Read the frame
            _, img = cap.read()
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Detect the faces
            faces = face_detector.detectMultiScale(gray, 1.1, 4)
            # Draw the rectangle around each face
            for (x, y, w, h) in faces:
                photo = img[y: y + h, x: x + w]
                photos_taken = photos_taken + 1
                cv2.imwrite("dataset/User." + str(i) + '.' +
                            str(photos_taken) + ".jpg", photo)

            # Stop if escape key is pressed
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        name = input('Input the name of the user we just scanned ')
        names.append(name)
        if i < users:

            continuation = input('Change users and press n to continue ')
            if continuation != 'n':
                quit()
            else:
                print('\n continuing')

    print("\n [INFO] Exiting Program and cleanup stuff")
    print(names)

    f = open('names.txt', 'a')

    for i in names:
        f.write(i + '\n')

    f.close()

    cam.release()
    cv2.destroyAllWindows()
