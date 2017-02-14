import os
import cv2
import dlib
import asyncio

detector = dlib.get_frontal_face_detector()
MALE = len(os.listdir('male'))
FEMALE = len(os.listdir('female'))
DETECTED_MALE = 0
DETECTED_FEMALE = 0


async def detect_face(folder, f):
    global DETECTED_MALE
    global DETECTED_FEMALE
    print('detecting: ' + f)
    img = cv2.imread(f)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dets = detector(img_rgb)

    if len(dets) > 0:
        print('get the face in: ' + f)
        if folder == './male/':
            DETECTED_MALE += 1
        else:
            DETECTED_FEMALE += 1
    else:
        print('can\'t detect the face in: ' + f)


async def detect_faces(folder):
    print('folder: ' + str(folder))
    for f in folder[1]:
        print('loading: ' + f)
        f = folder[0] + f
        await detect_face(folder[0], f)


def main():
    male = ['./male/']
    female = ['./female/']
    male.append(os.listdir(male[0]))
    female.append(os.listdir(female[0]))
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(detect_faces(male))
    asyncio.ensure_future(detect_faces(female))
    loop.run_forever()


if __name__ == '__main__':
    main()
    print('MALE: ' + str(MALE))
    print('FEMALE: ' + str(FEMALE))
    print('DETECTED_MALE: ' + str(DETECTED_MALE))
    print('DETECTED_FEMALE: ' + str(DETECTED_FEMALE))
