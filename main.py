import cv2
import tkinter as tk
from PIL import Image, ImageTk
import os
import tkinter.filedialog

beta = 0
gray = False
inverse = False
recording = False
out = None
video_path = None

capture = cv2.VideoCapture(0)

def Fmain():
    global beta, gray, out, recording

    ret, frame = capture.read()
    if ret:
        if gray == True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if inverse == True:
            frame = cv2.bitwise_not(frame)

        if not gray and not inverse:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        frame = cv2.flip(frame, 1)

        frame = cv2.convertScaleAbs(frame, alpha=1, beta=beta)

        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        Label1.imgtk = imgtk
        Label1.configure(image=imgtk)

    if recording and out is not None:
        out.write(frame)

    Label1.after(10, Fmain)

def F1():
    global beta, gray, inverse
    beta = 0
    gray = False
    inverse = False


def F2():
    global beta

    frame4 = tk.Frame(Wmain, bg="#5C5C5C", width=160, height=80)
    frame4.place(x=170, y=520)

    entry1 = tk.Entry(frame4)
    entry1.place(x=17.5, y=30)

    Label2 = tk.Label(frame4, text="enter the value (0-100)")
    Label2.place(x=18, y=5)

    def F6():
        global beta
        try:
            beta = int(entry1.get())
            beta = (beta - 50) * 5.1
            print(f"value beta: {beta}")
        except ValueError:
            beta = 0
            print("Value for beta is not correct!")
        frame4.destroy()

    button6 = tk.Button(frame4, text="Apply", bg="black", fg="white", bd=5, command=F6)
    button6.place(x=37.5, y=55, width=80, height=20)

def F3():
    global gray
    gray = True

def F4():
    global inverse
    inverse = True


def F5():
    global recording, out

    if not recording:
        video_path = tkinter.filedialog.asksaveasfilename(defaultextension=".avi", filetypes=[("AVI files", "*.avi")])

        if video_path:
            os.makedirs(os.path.dirname(video_path), exist_ok=True)

            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(video_path, fourcc, 20.0, (640, 480), isColor=(not gray))
            recording = True
            button5.config(text="Stop Recording", bg="darkred")
    else:
        recording = False
        if out:
            out.release()
            out = None
        button5.config(text="Record Video", bg="red")


Wmain = tk.Tk()
Wmain.geometry('700x610')
Wmain.configure(bg='#1F1F1F')

frame1 = tk.Frame(Wmain, bg="#2B2B2B", width=660, height=500)
frame1.pack()
frame1.place(x=20, y=20)

Label1 = tk.Label(Wmain, bg="#3D3D3D")
Label1.pack()
Label1.place(x=30, y=30, width=640, height=480)

frame2 = tk.Frame(Wmain, bg="#2B2B2B", width=560, height=60)
frame2.pack()
frame2.place(x=75, y=530)

button1 = tk.Button(Wmain, text="Original", bg="black", fg="white", bd=5, command=F1)
button1.pack()
button1.place(x=85, y=540, width=100, height=40)

button2 = tk.Button(Wmain, text="Brightness", bg="#55D7FF", fg="black", bd=5, command=F2)
button2.pack()
button2.place(x=195, y=540, width=100, height=40)

button3 = tk.Button(Wmain, text="Black & White", bg="#8F8F8F", fg="white", bd=5, command=F3)
button3.place(x=305, y=540, width=100, height=40)

button4 = tk.Button(Wmain, text="Inversion", bg="white", fg="black", bd=5, command=F4)
button4.pack()
button4.place(x=415, y=540, width=100, height=40)

button5 = tk.Button(Wmain, text="Record Vide", bg="red", fg="white", bd=5, command=F5)
button5.pack()
button5.place(x=525, y=540, width=100, height=40)

Fmain()

Wmain.mainloop()

capture.release()
cv2.destroyAllWindows()
