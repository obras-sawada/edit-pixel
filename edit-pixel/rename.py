import os
import glob

files = glob.glob('./edit/*')

for i, f in enumerate(files):
    ftitle, fext = os.path.splitext(f)
    os.rename(f, './edit/pic' + '{0:d}'.format(i) + fext)
