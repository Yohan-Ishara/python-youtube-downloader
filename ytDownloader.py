from pytube import YouTube
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


def download_video():
    link= link_field.get()
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        output_path = filedialog.askdirectory()
        youtube_object.download(output_path)

    except:
        print('Cannot found video')
    print('Download Completed')


screen = Tk()
title = screen.title('YouTube Downloader')
canvas = Canvas(screen, width=500, height=300)
canvas.pack()
img = Image.open('images/down.png')
resized_img = img.resize((500, 300), Image.LANCZOS)
new_image = ImageTk.PhotoImage(resized_img)
# logo_img= logo_img.subsample(2,2)
canvas.create_image(0, 0, anchor=NW, image=new_image)


link_field = Entry(screen, width=30)
link_label = Label(screen, text="Put your link here")

canvas.create_window(100, 100, window=link_label)
canvas.create_window(100, 140, window=link_field)

download_button=Button(screen,text="DOWNLOAD",command=download_video)
canvas.create_window(100,200,window=download_button)
screen.mainloop()




