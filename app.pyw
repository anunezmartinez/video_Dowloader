from tkinter import filedialog
from tkinter import *
import os
from pytube import YouTube


window = Tk()

window.title("Youtube Video Dowloader")

window.geometry('350x30')

lbl = Label(window, text="Insert URL")
lbl.grid(column=0, row=0)
var1 = IntVar()
ck = Checkbutton(window, text="Only Sound?", variable=var1, onvalue=1, offvalue=0)
ck.grid(column=4, row=0)


txt = Entry(window, width=10)
txt.grid(column=1, row=0)


def getString():

    res = txt.get()
    yt = YouTube(res)
    if var1.get() == 1:
        stream =  yt.streams.filter(only_audio=True).first()
        try:  
            # os.mkdir('mp3')
            window.filename =  filedialog.askdirectory()
        except OSError as error:  
            print(error)  
        stream.download(window.filename)
    elif var1.get() == 0:
        stream = yt.streams.filter(adaptive=True).first()
        try:  
            window.filename =  filedialog.askdirectory()
        except OSError as error:  
            print(error)  
        stream.download(window.filename)
    

btn = Button(window, text="Download", command=getString)
btn.grid(column=2, row=0)

window.mainloop()
