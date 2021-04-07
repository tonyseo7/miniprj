import tkinter
import cv2
from PIL import ImageTk, Image


window=tkinter.Tk()
frame = tkinter.Frame(window, width=700, height=480)
lbl1 = tkinter.Label(frame, width=700, height=480)
cap = cv2.VideoCapture(0) # VideoCapture 객체 정의

btnPosX = 70
btnPosY = 520

position_lblPosX = 25
position_lblPosY = 20

orientation_lblPosX = 800
orientation_lblPosY = 20

def Button_1():
    pass

def Button_2():
    pass

def Button_3():
    pass

def Button_4():
    pass

def ButtonStartPoint():
    pass

def InitWindow():
###################################################################################
    window.title("Cafe Robot Test")
    window.geometry("900x700+100+100")
    window.resizable(False, False)
###################################################################################
    frame.place(x=100, y=10)
###################################################################################

    lbl1.pack()
###################################################################################
    button1 = tkinter.Button(window, text="Table 1", width=20, height=3, command=Button_1)
    button1.place(x=btnPosX, y=btnPosY)

    button2 = tkinter.Button(window, text="Table 2", width=20, height=3, command=Button_2)
    button2.place(x=btnPosX+200, y=btnPosY)

    button3 = tkinter.Button(window, text="Table 3", width=20, height=3, command=Button_3)
    button3.place(x=btnPosX+400, y=btnPosY)

    button4 = tkinter.Button(window, text="Table 4", width=20, height=3, command=Button_4)
    button4.place(x=btnPosX+600, y=btnPosY)

    btnStart = tkinter.Button(window, text="Start Point", width=40, height=3, command=ButtonStartPoint)
    btnStart.place(x=btnPosX + 220, y=btnPosY + 100)
###################################################################################
    position_lbl=tkinter.Label(window, text="Position", width=10, height=2, fg="black", relief="solid")
    position_lbl.place(x=position_lblPosX, y=position_lblPosY)


    posX_lbl = tkinter.Label(window, text="X", width=10, height=2, fg="black")
    posX_lbl.place(x=position_lblPosX, y=position_lblPosY+40)

    posX_entry = tkinter.Entry(window, width=10)
    posX_entry.place(x=position_lblPosX, y=position_lblPosY + 70)


    posY_lbl = tkinter.Label(window, text="Y", width=10, height=2, fg="black")
    posY_lbl.place(x=position_lblPosX, y=position_lblPosY + 110)

    posX_entry = tkinter.Entry(window, width=10)
    posX_entry.place(x=position_lblPosX, y=position_lblPosY + 140)

    posZ_lbl = tkinter.Label(window, text="Z", width=10, height=2, fg="black")
    posZ_lbl.place(x=position_lblPosX, y=position_lblPosY + 180)

    posX_entry = tkinter.Entry(window, width=10)
    posX_entry.place(x=position_lblPosX, y=position_lblPosY + 210)


###################################################################################
    orientation_lbl = tkinter.Label(window, text="Orientation", width=10, height=2, fg="red", relief="solid")
    orientation_lbl.place(x=orientation_lblPosX, y=orientation_lblPosY)

    orienX_lbl = tkinter.Label(window, text="X", width=10, height=2, fg="black")
    orienX_lbl.place(x=orientation_lblPosX, y=position_lblPosY+40)

    orienX_entry = tkinter.Entry(window, width=10)
    orienX_entry.place(x=orientation_lblPosX, y=position_lblPosY + 70)

    orienY_lbl = tkinter.Label(window, text="Y", width=10, height=2, fg="black")
    orienY_lbl.place(x=orientation_lblPosX, y=position_lblPosY+110)

    orienY_entry = tkinter.Entry(window, width=10)
    orienY_entry.place(x=orientation_lblPosX, y=position_lblPosY + 140)

    orienZ_lbl = tkinter.Label(window, text="Z", width=10, height=2, fg="black")
    orienZ_lbl.place(x=orientation_lblPosX, y=position_lblPosY+180)

    orienZ_entry = tkinter.Entry(window, width=10)
    orienZ_entry.place(x=orientation_lblPosX, y=position_lblPosY + 210)


    orienW_lbl = tkinter.Label(window, text="W", width=10, height=2, fg="black")
    orienW_lbl.place(x=orientation_lblPosX, y=position_lblPosY + 250)

    orienW_entry = tkinter.Entry(window, width=10)
    orienW_entry.place(x=orientation_lblPosX, y=position_lblPosY + 280)

###################################################################################
xml_path = "haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(xml_path)

def detectBody(img):
    # Detect faces in the image
    detectFlag = False

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    body = faceCascade.detectMultiScale(grayImg)

    if not body is None:
        detectFlag = True

    # 검출된 얼굴 주변에 사각형 그리기
    for (x, y, w, h) in body:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return detectFlag, img


def playVideo():
    ret, frame = cap.read() # 프레임이 올바르게 읽히면 ret은 True
    if not ret:
        cap.release() # 작업 완료 후 해제
        return
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    detectFlag, detectFrame = detectBody(frame)

    img = Image.fromarray(detectFrame) # Image 객체로 변환

    imgtk = ImageTk.PhotoImage(image=img) # ImageTk 객체로 변환
    # OpenCV 동영상
    lbl1.imgtk = imgtk
    lbl1.configure(image=imgtk)
    lbl1.after(10, playVideo)


def main():
    InitWindow()
    playVideo()
    window.mainloop()

if __name__ == "__main__":
    main()


