import cv2
from tkinter import *
from tkinter import messagebox

def handsome_cam():
    cam = cv2.VideoCapture(0)

    while True:
        _, frame = cam.read()
        cv2.imshow("DateWithMe:  some name", frame)
        if cv2.waitKey(10) == ord('q'):
            break
    

date = Tk()

date.title("DateWithMe")

date.geometry("500x500")

cam_On_btn = Button(text="Show my handsomeness" ,command=handsome_cam)
cam_On_btn.pack()

date.mainloop()
