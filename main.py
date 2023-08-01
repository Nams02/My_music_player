import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer


def browse_music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = [song for song in os.listdir(path) if song.endswith(".mp3")]
        Playlist.delete(0, END)
        for song in songs:
            Playlist.insert(END, song)


def play_music():
    global paused
    if paused:
        mixer.music.unpause()
        status_var.set("Music Resumed")
        paused = False
    else:
        current_song = Playlist.get(ACTIVE)
        mixer.music.load(current_song)
        mixer.music.play()
        status_var.set("Now Playing: " + os.path.basename(current_song))


def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    status_var.set("Music Paused")


def stop_music():
    mixer.music.stop()
    status_var.set("Music Stopped")


def set_volume(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)


mixer.init()
paused = False  # to keep track of whether the music is paused or not

root = Tk()
root.title("Music player project by Naman Agarwal")
root.geometry("485x700+290+10")
root.configure(bg="lightgray")
root.resizable(False, False)

# Add a logo
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="lightgray").pack(pady=10)

# Icon
lower_frame = Frame(root, bg="#FFFFFF", width=485, height=180)
lower_frame.place(x=0, y=400)

# Animation
frameCnt = 30
frames = [PhotoImage(file='aa1.gif', format='gif -index %i' % (i))
          for i in range(frameCnt)]


def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)


label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)

# Button
play_icon = PhotoImage(file="play1.png")
Button(root, image=play_icon, bg="#FFFFFF", bd=0, height=60, width=60,
       command=play_music).place(x=215, y=487)

stop_icon = PhotoImage(file="stop1.png")
Button(root, image=stop_icon, bg="#FFFFFF", bd=0, height=60, width=60,
       command=stop_music).place(x=130, y=487)

pause_icon = PhotoImage(file="pause1.png")
Button(root, image=pause_icon, bg="#FFFFFF", bd=0, height=60, width=60,
       command=pause_music).place(x=300, y=487)

# Label
menu_icon = PhotoImage(file="menu.png")
Label(root, image=menu_icon, bg="lightgray").place(
    x=0, y=580, width=485, height=120)

frame_music = Frame(root, bd=2, relief=RIDGE)
frame_music.place(x=0, y=585, width=485, height=100)

Button(root, text="Browse Music", width=59, height=1, font=("calibri", 12, "bold"),
       fg="Black", bg="#FFFFFF", command=browse_music).place(x=0, y=550)

scroll = Scrollbar(frame_music)
Playlist = Listbox(frame_music, width=100, font=("Times new roman", 10),
                   bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)

scroll.config(command=Playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH, expand=True)

# Volume Scale
volume_scale = Scale(root, from_=0, to=100,
                     orient=HORIZONTAL, command=set_volume, bg="red", troughcolor="white")
volume_scale.set(70)
volume_scale.place(x=20, y=497)

# Status bar
status_var = StringVar()
status_var.set("Echosphere: Immerse in the Melodic Universe")
status_label = Label(root, textvariable=status_var,
                     bg="lightgray", fg="black", font=("Arial", 10, "italic"))
status_label.pack(side=BOTTOM, fill=X)

root.mainloop()
