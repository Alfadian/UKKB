import face_recognition
import os
import cv2

KNOWN_FACES_DIR = "known_faces"
UNKNOWN_FACES_DIR = "unknown_faces"
TOL = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn"

known_faces = []
known_names = []

for name in os.listdir(KNOWN_FACES_DIR):
    for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        image = face_recognition.load_file_image(f"{KNOWN_FACES_DIR}/{name}")
        encoding = face_recognition.face_encoding(image)
        known_faces.append(encoding)
        known_names.append(name)

print("data sedang di proses")
for filename in os.listdir(UNKNOWN_FACES_DIR):
    print(filename)
    image = face_recognition.load_file_image(f"{KNOWN_FACES_DIR}/{name}")
    locations = face_recognition.face_locations(image, model=MODEL)
    encodings = face_recognition.face_encodings(image, locations)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    for face_encoding, face_location in zip(encodings, locations):
        result = face_recognition.compare_faces(
            known_faces, face_encoding, TOL)
        match = None
        if True in result:
            match = known_names[result.index(True)]
            print(f"match found : {match}")

            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])

            color = [0, 255, 0]

            cv2.rectangle(image, top_left, bottom_right,
                          color, FRAME_THICKNESS)

            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1], face_location[2]+22)
            cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
            cv2.putText(image, match, (face_location[3]+10, face_location[2]+15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), FONT_THICKNESS)

    cv2.imshow(filename, image)
    cv2.waitKey(10000)
    # cv2.destroyWindow(filename)
