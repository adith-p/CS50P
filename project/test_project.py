
from project_class import file_sys
import project
import os
from pathlib import Path


def main():
    test_get_loc()
    test_folder_exist()
    test_stem()


def test_get_loc():
    assert os.path.exists("/home/adith/Documents") == True


def test_folder_exist():
    test_path = Path("/home/adith/Documents")
    file_sys.path = test_path
    project.folder_exist()
    p = test_path
    for x in p.iterdir():
        flag = False
        if x.is_dir() and x in ["audio", "application",
                                "video", "image", "text"]:

            flag = True

            assert flag == True

    project.stem()


def test_stem():
    test_path = Path("/home/adith/Documents/")
    file_sys.path = test_path
    project.stem()
    flag = False
    for x in test_path.iterdir():

        if x.is_dir() and x in ["audio", "application",
                                "video", "image", "text"]:

            dir = os.listdir(test_path+x)
            if len(dir) != 0:
                flag = True
                continue
            assert flag == True


if __name__ == "__main__":
    main()
