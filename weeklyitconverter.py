from __future__ import generators

__author__ = 'Lord'

import os, fnmatch, subprocess

file_list = []
path_for_search = "d:/Weekly-it_video/"
filetype_to_search = ".MOD"

#curpath = os.getcwd()
# assert 0, curpath



def convert(path_for_search=os.getcwd()):
    collect_files(path_for_search)
    run_conversion()


def run_conversion():
    for f in file_list:
        filecounter =+ 1
        #f = '"'+f+'"'
        subprocess.call("ffmpeg -i "+'"'+f+'"'+" -aspect 720:540 -vcodec libx264 -vprofile high -preset slow -b:v 500k -maxrate 500k -bufsize 1000k -vf scale=-1:480 -acodec ac3 -b:a 128k -y -f mp4 "+'"'+f+".mp4"+'"')


def collect_files(path_for_search):
    for f in dirwalk(path_for_search):
        if filetype_to_search in f:
            file_list.append(f)
    print file_list
    return file_list




def dirwalk(dir):
    "walk a directory tree, using a generator"
    for f in os.listdir(dir):
        fullpath = os.path.join(dir,f)
        if os.path.isdir(fullpath) and not os.path.islink(fullpath):
            for x in dirwalk(fullpath):  # recurse into subdir
                yield x
        else:
            yield fullpath


if __name__ == '__main__':
    if path_for_search:
        convert(path_for_search)
    else: convert()



