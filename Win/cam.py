import cv2

cam = cv2.VideoCapture(0)

while(True):
    ret, frame = cam.read()
    cv2.imshow("camera", frame)

        # キー操作があればwhileループを抜ける
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# 撮影用オブジェクトとウィンドウの解放
cam.release()
cv2.destroyAllWindows()

