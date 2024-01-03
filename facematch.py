import face_recognition

images_of_bill = face_recognition.load_image_file('./img/known/billgates.jpeg')
bill_face_encoding = face_recognition.face_encodings(images_of_bill)[0]

unknow_image = face_recognition.load_image_file('./img/unknown/obama.jpeg')
unknown_face_encoding = face_recognition.face_encodings(unknow_image)[0]

#compare faces
results = face_recognition.compare_faces([bill_face_encoding],unknown_face_encoding)

if results[0]:
    print("This is Bill Mowa")
else:
    print("This is NOT Bill Mowa")