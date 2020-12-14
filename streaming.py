import os

os.chdir(os.getcwd() + "/360x240")
ip = '192.168.1.195'
os.system("ffmpeg -i video_comparison.mkv -v 0 -vcodec mpeg4 -acodec copy -b:v 64k -f mpegts udp://127.0.0.1:1234")

#CAMBIA EL NOMBRE DEL VIDEO Y CA,BIA OLA DIRECCION DE RED (IFCONFIG PARA VER LA DE TU ORDENARDOR, LA DE RED!!!)