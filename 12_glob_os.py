from glob import glob
import os

fileList = glob('sample/*.png')
for file in fileList:
    print(file, '=>', file[:-3] + 'jpg')
    os.rename(file, file[:-3] + 'jpg')
