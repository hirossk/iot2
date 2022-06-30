import cv2

def main():
    # VideoCapture オブジェクトを取得します
    capture = cv2.VideoCapture(0)

    while(True):
        #カメラから１フレーム読み込みます
        ret, frame = capture.read()
        # 画面サイズを変更します
        window = (800,480)
        frame = cv2.resize(frame,window)

        #画面表示します
        cv2.imshow('capture',frame)

        #キーボードから'q'を押すと終了します
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
