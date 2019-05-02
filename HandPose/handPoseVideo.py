import cv2
import numpy as np

# Preparação do dataset
# https://drive.google.com/open?id=1MjZqA3VscsVxMpmEbc300EwZLb87NqK_
protoFile = None
weightsFile = None
nPoints = None
POSE_PAIRS = [ [0,1],[1,2],[2,3],[3,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[10,11],[11,12],[0,13],[13,14],[14,15],[15,16],[0,17],[17,18],[18,19],[19,20] ]

threshold = 0.1

input_source = None
cap = None
hasFrame, frame = None

frameWidth = None
frameHeight = None

aspect_ratio = None

# Entada das dimenções da imagem na CNN
inHeight = None
inWidth = None
print('Tamanho da entrada:',inWidth)

vid_writer = None

net = None
k = 0
while 1:
    k+=1
    hasFrame, frame = cap.read()
    frameCopy = np.copy(frame)
    if not hasFrame:
        cv2.waitKey()
        break
    # Setando a Rede
    inpBlob = None

    # Rodando a Rede
    output = None

    points = []

    for i in range(nPoints):
        # Mapa de correspondencia das partes do corpo
        probMap = output[0, i, :, :]
        probMap = None

        # Find global maxima of the probMap.
        minVal, prob, minLoc, point = None

        if prob > threshold :
            # Desenhando o pontos

            # Add the point to the list if the probability is greater than the threshold
            # Adicione o ponto à lista se a probabilidade for maior que o limite
            points.append( )
        else :
            points.append(None)

    # Draw Skeleton
    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]

        if points[partA] and points[partB]:

    # cv2.putText(frame, "time taken = {:.2f} sec".format(time.time() - t), (50, 50), cv2.FONT_HERSHEY_COMPLEX, .8, (255, 50, 0), 2, lineType=cv2.LINE_AA)
    # cv2.putText(frame, "Hand Pose using OpenCV", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 0), 2, lineType=cv2.LINE_AA)
    cv2.imshow('Output-Skeleton', frame)
    # cv2.imwrite("video_output/{:03d}.jpg".format(k), frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

    vid_writer.write(frame)

vid_writer.release()
