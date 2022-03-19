import cv2
import mediapipe as mp
import dlib


def get_face_landmarks(image_filename,method='mediapipe',predict_model_file='shape_predictor_68_face_landmarks.dat'):
    preds = []
    image = cv2.imread(image_filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    if method == 'mediapipe':
        mp_face_mesh = mp.solutions.face_mesh

        with mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=3,
            min_detection_confidence=0.5) as face_mesh:

            results = face_mesh.process(image)

            if not results.multi_face_landmarks:
                preds =[]
            else:
                face_land = []
                for face in results.multi_face_landmarks:
                    face_land = []
                    for landmark in face.landmark:
                        x = landmark.x
                        y = landmark.y

                        shape = image.shape 
                        relative_x = int(x * shape[1])
                        relative_y = int(y * shape[0])
                        face_land.append([relative_x, relative_y])
                    preds.append(face_land)
    elif method == 'dlib':
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(predict_model_file)
        face_rects = detector(image, 1)

        for face in face_rects:
            face_landmarks = [(land.x, land.y) for land in predictor(image,face).parts()]
            preds.append(face_landmarks)

    return preds
