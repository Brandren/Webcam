import cv2
cap=cv2.VideoCapture(0)
count = 0
print("Open Webcam")
while True:
    ret,img=cap.read()
    cv2.imshow("Webcam",img)
    k=cv2.waitKey(30)
    if k == 27:
        print("Close Webcam")
        break
    elif k == 13:
        print("Image " + str(count) + " saved...")
        file = "C:/Users/Ng Jing Ping/OneDrive/Desktop/Image"+str(count)+".jpg"
        cv2.imwrite(file,img)
        count+=1
cap.release()
cv2.destroyAllWindows()
