from email.mime import image
from operator import index
from tkinter import *
from os import *
from tkinter.font import Font

from numpy import imag
from idna import valid_contextj


downloader = Tk()
downloader.geometry("1000x600")
downloader.minsize(400, 400)


walph = PhotoImage(file=r"D:\my.png")
wall = Label(downloader, image=walph)
wall.place(x=0, y=0, width=1400, height=900)


dl_frame = Label(wall, bg="white")
dl_frame.place(x=420, y=70, width=530, height=520)
# ==================================== functions ===================================================
clicked = " "


def video_f():
    global clicked
    clicked = "Video"
    video_b.config(value=1)


def audio_f():
    global clicked
    clicked = "Audio"
    audio_b.config(value=1)


def download_f():
    if clicked == " " or path_e.get() == "" or link_e.get() == "":
        msg.set("             * You Should Fill The Form *")

    elif clicked == "Video" and path_e.get() != "" and link_e.get() != "":
        msg.set("")
        system(f"cd {path_e.get()}")
        try:
            system(f"youtube-dl  {link_e.get()}")
        except:
            msg.set("Error , Make Sure The Path Or The Link Is Exist ")

    elif clicked == "Audio":
        for i in range(1, 1000000):
            real_path = fr"{path_e.get()}\audio{i}.mp3"
            try:
                system(f"youtube-dl -o \"{real_path}\"  {path_e.get()}")
            except:
                msg.set("Error , Make Sure The Path Or The Link Is Exist ")


# ==================================== Entrys ======================================================
link_e = Entry(dl_frame, bg="#bdbdbd")
link_e.place(x=120, y=150, width=320, height=30)
path_e = Entry(dl_frame, bg="#bdbdbd")
path_e.place(x=120, y=200, width=320, height=30)

# ==================================== Labels ======================================================
link_l = Label(dl_frame, text="Link : ", bg="white")
link_l.place(x=40, y=150, width=80, height=30)

path_l = Label(dl_frame, text="Path : ", bg="white")
path_l.place(x=40, y=200, width=80, height=30)

msg = StringVar()

message_l = Label(dl_frame, textvariable=msg, bg="white", fg="red",
                  font=Font(size=10, weight="bold"))
message_l.place(x=10, y=20, width=460, height=100)


# ===================================== Buttons ====================================================
video_b = Radiobutton(dl_frame, text="Video", bg="white",
                      fg="black", command=video_f, value=0)
video_b.place(x=150, y=250)

audio_b = Radiobutton(dl_frame, text="Audio", bg="white",
                      fg="black", command=video_f, value=0)
audio_b.place(x=300, y=250)

dl_button = Button(dl_frame, text="Download", fg="white",
                   command=download_f, bg="#19887b")
dl_button.place(x=200, y=400, width=100, height=30)

downloader.mainloop()


# from os import *

# # youtube-dl -o "path" 'youtube file url'
# v_p=input("Video or  Playlist or Audio\n").capitalize()
# path=input("enter the path of the playlist\n").strip()
# url=input("enter the link \n")

# if v_p=="Video":
#     name=input("enter the name of video\n")
#     if name!="":
#         real_path=fr"{path}\{name}.mp4"
#         try:
#             system(f"youtube-dl -o \"{real_path}\" {url}")
#         except:
#             print("make sure the url is working")
#     else:
#         real_path=fr"{path}\unkown.mp4"
#         try:
#             system(f"youtube-dl -o \"{real_path}\"  {url}")
#         except:
#             print("make sure the url is working")
# elif v_p=="Playlist":
#     for i in range(1,1000000):
#         real_path=fr"{path}\video{i}.mp4"
#         try:
#                 system(f"youtube-dl -o \"{real_path}\"  {url}")
#         except:
#                 print("make sure the url is working")
# elif v_p=="Audio":
#     name=input("enter the name of audio\n")
#     if name!="":
#         real_path=fr"{path}\{name}.mp3"
#         try:
#                 system(f"youtube-dl -o \"{real_path}\"  {url}")
#         except:
#                 print("make sure the url is working")
#     else:
#         real_path=fr"{path}\unkown.mp3"
#         try:
#             system(f"youtube-dl -o \"{real_path}\"  {url}")
#         except:
#             print("make sure the url is working")
