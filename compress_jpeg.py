import os
import glob
from PIL import Image


path_dir = input('Введите путь к папке \n')
os.chdir(path_dir)
list_of_jpeg = glob.glob('*.jpg')
new_folder = 'compressed'
if not os.path.exists(new_folder):
    os.mkdir(new_folder)
size = 1200, 1200

for infile in list_of_jpeg:
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        im.thumbnail(size)
        os.chdir(new_folder)
        im.save(file + "_compressed.jpg", "JPEG")
    os.chdir('..')
print('DONE!!!')