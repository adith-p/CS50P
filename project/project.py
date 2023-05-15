import sys
import os
import magic
import shutil
from project_class import file_sys


def main():
    get_loc()
    folder_exist()
    stem()


def get_loc():
    try:
        # get the folder locations through command line argument
        file_loc = sys.argv[1]
    except:
        # if not provided the program goes to the default locations [home/{user}/Downloads]
        file_loc = '/home/adith/Downloads'
    file_sys.folder_path(file_loc)
    p = file_sys.path

    if p.exists() == False:
        sys.exit("File not found")


def folder_exist():
    # scan through the folder and create folder named- [audio,application,video,image,text]
    p = file_sys.path
    q = p/"audio"
    if not q.exists():
        os.mkdir(p/"audio")
    q = p/"application"
    if not q.exists():
        os.mkdir(p/"application")
    q = p/"video"
    if not q.exists():
        os.mkdir(p/"video")
    q = p/"image"
    if not q.exists():
        os.mkdir(p/"image")
    q = p/"text"
    if not q.exists():
        os.mkdir(p/"text")


def stem():
    p = file_sys.path
    # file are then transfered into respective type of folders

    for x in p.iterdir():
        if not x.is_dir():
            type = magic.from_file(x, mime=True).split("/")[0]
            if type in ["audio"]:
                shutil.move(x, p/"audio")
                continue
            if type in ["application"]:
                shutil.move(x, p/"application")
                continue
            if type in ["video"]:
                shutil.move(x, p/"video")
                continue
            if type in ["image"]:
                shutil.move(x, p/"image")
                continue
            if type in ["text"]:
                shutil.move(x, p/"text")
                continue
    print("Done, This Was CS50!")


if __name__ == "__main__":
    main()
