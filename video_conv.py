import os
import shutil


def convertor(in_name, codec, out_name):
    os.system("ffmpeg -i " + in_name + " -c:v " + codec + "  -c:a copy " + out_name)

def app():
    # Crear las variables de nombres, codecs y extensiones a usar;
    names = ["1280x720_cut.mp4", "640x480_cut.mp4", "360x240_cut.mp4", "160x120_cut.mp4"]
    new_codecs = ["libvpx", "libvpx-vp9", "libx265", "av1"]
    extensions = [".webm", ".webm", ".mp4", ".mkv"]

    for i in range(len(names)):
        # Crear carpeta para poder guardar los diferentes videos.
        os.mkdir(os.getcwd() + "/" + names[i].split("_")[0])
        print(os.getcwd() + "/" + names[i])
        # Crear los diferentes videos con diferentes codecs;
        for j in range(len(new_codecs)):
            convertor(names[i], new_codecs[j], new_codecs[j] + "_" + names[i].split(".")[0] + extensions[j])

            source_dir = os.getcwd()
            target_dir = os.path.join(os.getcwd(), names[i].split("_")[0])
            # mover el video a la carpeta corespondiente.
            shutil.move(os.path.join(source_dir, new_codecs[j] + "_" + names[i].split(".")[0] + extensions[j]),
                        target_dir)

            print("Video: " + names[i], "Converted to: " + new_codecs[j],
                  "New video: " + new_codecs[j] + "_" + names[i].split(".")[0] + extensions[j])


if __name__ == '__main__':
    app()