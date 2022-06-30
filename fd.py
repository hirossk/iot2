import cv2
import os

def main():
    # VideoCapture オブジェクトを取得します
    capture = cv2.VideoCapture(0)
    #casceade_path = os.path.join(
    #    cv2.data.haarcascades, "haarcascade_frontalface_alt.xml"
    #)
    #cascade = cv2.CascadeClassifier(casceade_path)

    while(True):
        ret, frame = capture.read()
        # resize the window
        window = (800,480)
        frame = cv2.resize(frame,window)
        #顔検出します
        #face_list = cascade.detectMultiScale(frame)
        #color=(255, 0, 255)
        #if len(face_list) > 0 :
            #顔検出ができたとき
            #for face in face_list :
                #x, y, w, h = face
                #検出された顔に枠をつける
                #cv2.rectangle(frame, (int(x),int(y)), (int(x+w), int(y+h)), color, thickness=2) 

        cv2.imshow('capture',frame)

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
