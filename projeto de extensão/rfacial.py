import cv2
import mediapipe as mp

# inicializar o mediapipe e o openCV

webcan = cv2.VideoCapture(0)
detection_face = mp.solutions.face_detection
reconhecer_rostos = detection_face.FaceDetection()
area = mp.solutions.drawing_utils

while True:
    #Ligar a camera
    Verificador, imagem = webcan.read()
    if not Verificador:
        break
    #Reconhecer rostos
    dados_rostos = reconhecer_rostos.process(imagem)
    for rostos in dados_rostos.detections:
        #Desenhar na tela
        area.draw_detection(imagem, rostos)

    cv2.imshow("Detections", imagem)
    # Apertar Esc para parar o programa
    if cv2.waitKey(5) == 27:
        break

webcan.release()
cv2.destroyAllWindows()