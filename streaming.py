import os

os.chdir(os.getcwd() + "/360x240")
# Crear vector con la ip local, que también la pondremos en el VLC.
ip = '192.168.1.195'
# Computar la linea que crea el streaming. (codigo de internet).
os.system("ffmpeg -i video_comparison.mkv -v 0 -vcodec mpeg4 -acodec copy -b:v 64k -f mpegts udp://" + ip + ":1234")
