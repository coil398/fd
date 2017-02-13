import cv2
import dlib
import copy
import time


detector = dlib.get_frontal_face_detector()
video_input = cv2.VideoCapture(1)


while(video_input.isOpened()):
    ret, frame = video_input.read()
    temp_frame = cv2.cvtColor(copy.deepcopy(frame), cv2.COLOR_BGR2RGB)

    start = time.time()
    dets = detector(temp_frame, 1)
    elapsed_time = time.time() - start

    for k, d in enumerate(dets):
        cv2.putText(frame, 'Dlib', (d.left(), d.top()),
                    cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255))
        cv2.rectangle(frame, (d.left(), d.top()),
                      (d.right(), d.bottom()), (255, 0, 0), 2)

    print('face detection(dlib) processing time: {0}'.format(elapsed_time))

    cv2.imshow('face detection', frame)

    c = cv2.waitKey(50) & 0xFF

    if c == 27:
        break

video_input.release()
cv2.destroyAllWindows()
