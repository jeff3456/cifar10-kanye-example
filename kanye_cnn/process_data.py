import os
# Preprocess files in both kanye pics and non kanye pics;

pathtodata = (os.path.dirname(os.path.realpath(__file__))+
              '/../kanye_west_data/')

def get_kanye_f_names():
    i = 1
    basejpg = pathtodata+'kanye_pics/Kanye{}.jpg'
    basejpeg = pathtodata+'kanye_pics/Kanye{}.jpeg'
    fnames = []
    while(os.path.isfile(basejpg.format(i)) or os.path.isfile(basejpeg.format(i))):
        if(os.path.isfile(basejpg.format(i))):
            fnames.append(basejpg.format(i))
        else:
            fnames.append(basejpeg.format(i))

        i += 1
    return fnames

def get_not_kanye_f_names():
    i = 1
    basepng = pathtodata+'not_kanye_pics/File{}.png'
    basejpg = pathtodata+'not_kanye_pics/File{}.jpg'
    fnames = []
    while(os.path.isfile(basepng.format(i)) or
          os.path.isfile(basejpg.format(i))):
        if(os.path.isfile(basepng.format(i))):
            fnames.append(basepng.format(i))
        else:
            fnames.append(basejpg.format(i))
        i += 1
    return fnames

namelist = get_not_kanye_f_names()
print(len(namelist))


