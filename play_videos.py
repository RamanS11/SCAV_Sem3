import os

def reproduce():
    os.chdir(os.getcwd() + "/360x240")
    # Create aux variables.
    direc = '.'
    allfiles = os.listdir(direc)
    aux = 1
    names = []
    # Plot all the videos in the current directory.
    for f_name in allfiles:
        names.append(f_name)
        print(aux, f_name)
        aux = aux + 1
    # Codigo de internet;
    os.system('ffmpeg -i ' + names[0] + ' -i ' + names[1] + ' -i ' + names[2] + ' -i ' + names[3] +
              ' -filter_complex "nullsrc=size=640x480 [base]; [0:v] setpts=PTS-STARTPTS,'
              ' scale=320x240 [upperleft]; [1:v] setpts=PTS-STARTPTS, scale=320x240 [upperright];'
              ' [2:v] setpts=PTS-STARTPTS, scale=320x240 [lowerleft]; [3:v] setpts=PTS-STARTPTS,'
              ' scale=320x240 [lowerright]; [base][upperleft] overlay=shortest=1 [tmp1];'
              ' [tmp1][upperright] overlay=shortest=1:x=320 [tmp2];'
              ' [tmp2][lowerleft] overlay=shortest=1:y=240 [tmp3];'
              ' [tmp3][lowerright] overlay=shortest=1:x=320:y=240" -c:v libx264 video_comparison.mkv')

def app():
    reproduce()


if __name__ == '__main__':
    app()