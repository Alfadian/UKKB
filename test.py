import face_recognition
from PIL import Image, ImageDraw

image_of_c = face_recognition.load_image_file('./img/known/Chandra.jpeg')
c_face_encoding = face_recognition.face_encodings(image_of_c)[0]


known_face_encodings = [
    c_face_encoding,

]

known_face_names = [
    "Chandra"
]

test_image = face_recognition.load_image_file('./img/groups/d.jpeg')

face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

pil_image = Image.fromarray(test_image)

draw = ImageDraw.Draw(pil_image)

for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(
        known_face_encodings, face_encoding)

    name = "Unknown Person"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0))

    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)),
                   fill=(255, 255, 0), outline=(255, 255, 0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(0, 0, 0))

del draw

pil_image.show()

pil_image.save('identifys.jpg')