import numpy as np
import face_recognition as fr
import cv2

video_capture = cv2.VideoCapture(0)

bruno_image = fr.load_image_file("Elon Musk Royal.jpg")
bruno_face_encoding = fr.face_encoding(Elon_image)[0]

know_faces_encodings = [Elon_face_encoding]
known_face_names = ["Elon"]

while True:
    ret, frame = video_capture.read()
    
    rgb_frame = grame [:, :, ::-1]
    
    face_locations = fr.face_locations(rgb_frame)
    face_encodings = fr.face_encodings(rgb_frame, face_locations)
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        
        matches = fr.compae_faces(known_encosings, face_encosings)
        
        name = "Unknown"
        
        face_distance = fr.face_distance(known_face_encoding, face_encoding)
     
        best_match_index =np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        
        cv2.rectangle(frame, (left,top),(right,bottom),(0,0,255),2)
        
        cv2.rectangle(frame, (left,bottom -35), (right,bottom), (0,0,255), cv2.FILLED)
        
        font =cv2.FONT_HERSHEY_SIMPLE
        cv2.putText(frame, name, (left + 6,bottom -6), font, 1.0,(255,255,255),1)
        
    cv2.imshow('WebCam_Face_Recognition',frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
video_capture.release()
cv2.destroyAllWindow()