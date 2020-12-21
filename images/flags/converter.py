from PIL import Image
from os import listdir, getcwd, remove
from os.path import isfile, join
mypath = getcwd()
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def iter_frames(im):
    try:
        i= 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            if i == 0:
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass

for file in onlyfiles:
    if not file.endswith("gif"):
        continue
    im = Image.open(file)
    new_file = file.replace(".gif", ".png")
    for i, frame in enumerate(iter_frames(im)):
        frame.save(new_file,**frame.info)
    im.close()
    remove(file)


