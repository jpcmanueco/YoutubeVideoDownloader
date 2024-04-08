import os
from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
from tkinter import messagebox as MessageBox
from tkinter import Tk, Label, Entry, Button, PhotoImage, Menu

def descargar_audio():
    enlace = video.get()
    video_descargar = YouTube(enlace)
    
    # Descargar el audio
    audio_streams = video_descargar.streams.filter(only_audio=True)
    audio_stream = audio_streams[0]
    carpeta_descargas = "AudioDescargado"
    if not os.path.exists(carpeta_descargas):
        os.makedirs(carpeta_descargas)
    ruta_audio = os.path.join(carpeta_descargas, video_descargar.title + ".mp3")
    audio_stream.download(output_path=carpeta_descargas, filename=video_descargar.title + ".mp3")
    
    MessageBox.showinfo("Descarga completada", "El audio se ha descargado en la carpeta AudioDescargado.")

def descargar_video():
    enlace = video.get()
    video_descargar = YouTube(enlace)
    
    # Descargar el video
    video_stream = video_descargar.streams.get_highest_resolution()
    carpeta_descargas = "VideoDescargado"
    if not os.path.exists(carpeta_descargas):
        os.makedirs(carpeta_descargas)
    ruta_video = os.path.join(carpeta_descargas, video_descargar.title + ".mp4")
    video_stream.download(output_path=carpeta_descargas, filename=video_descargar.title + ".mp4")
    
    MessageBox.showinfo("Descarga completada", "El video se ha descargado en la carpeta VideoDescargado.")

def descargar_video_y_audio():
    enlace = video.get()
    video_descargar = YouTube(enlace)
    
    # Descargar el video
    video_stream = video_descargar.streams.get_highest_resolution()
    carpeta_video_descargas = "VideoDescargado"
    if not os.path.exists(carpeta_video_descargas):
        os.makedirs(carpeta_video_descargas)
    ruta_video = os.path.join(carpeta_video_descargas, video_descargar.title + ".mp4")
    video_stream.download(output_path=carpeta_video_descargas, filename=video_descargar.title + ".mp4")
    
    # Descargar el audio
    audio_streams = video_descargar.streams.filter(only_audio=True)
    audio_stream = audio_streams[0]
    carpeta_audio_descargas = "AudioDescargado"
    if not os.path.exists(carpeta_audio_descargas):
        os.makedirs(carpeta_audio_descargas)
    ruta_audio = os.path.join(carpeta_audio_descargas, video_descargar.title + ".mp3")
    audio_stream.download(output_path=carpeta_audio_descargas, filename=video_descargar.title + ".mp3")
    
    # Combinar el video y el audio
    video_clip = VideoFileClip(ruta_video)
    audio_clip = AudioFileClip(ruta_audio)
    video_con_audio = video_clip.set_audio(audio_clip)
    carpeta_video_audio_descargas = "VideoAudioDescargado"
    if not os.path.exists(carpeta_video_audio_descargas):
        os.makedirs(carpeta_video_audio_descargas)
    ruta_video_con_audio = os.path.join(carpeta_video_audio_descargas, video_descargar.title + "_con_audio.mp4")
    video_con_audio.write_videofile(ruta_video_con_audio, codec="libx264")
    
    # Eliminar el archivo de video descargado
    os.remove(ruta_video)
    
    MessageBox.showinfo("Descarga completada", "El video con audio se ha descargado en la carpeta VideoAudioDescargado.")

def popup():
    MessageBox.showinfo("Sobre mí", "Enlace al repositorio de Github: https://github.com/jpcmanueco")

root = Tk()
root.title('YoutubeVideoDownloader')
root.geometry("900x500")
root.resizable(False, False)

# Declaración de menú superior
menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)
# Declaración de elementos del menú superior
menubar.add_cascade(label="Info. Adicional", menu=helpmenu)
helpmenu.add_command(label="Información del creador", command=popup)
menubar.add_command(label="Exit", command=root.destroy)

imagen = PhotoImage(file="Resources/youtube.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0, padx=20, pady=20)

instrucciones = Label(root, text="Programa en Python para la descarga de videos de Youtube")
instrucciones.grid(row=0, column=1, padx=20, pady=20)

video = Entry(root, width=40)
video.grid(row=1, column=1, padx=20, pady=10)

boton_audio = Button(root, text="Descargar solo audio", command=descargar_audio)
boton_audio.grid(row=2, column=0, padx=20, pady=10)

boton_video = Button(root, text="Descargar solo video", command=descargar_video)
boton_video.grid(row=2, column=1, padx=20, pady=10)

boton_audio_video = Button(root, text="Descargar video con audio", command=descargar_video_y_audio)
boton_audio_video.grid(row=2, column=2, padx=20, pady=10)

root.mainloop()
