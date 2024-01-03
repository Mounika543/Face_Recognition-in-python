import face_recognition

image = face_recognition.load_image_file('./img/groups/nrml.jpeg')
face_locations = face_recognition.face_locations(image)

#Array of coords in each face
#print(face_locations)

print(f'There are{len(face_locations)} people in this image')
