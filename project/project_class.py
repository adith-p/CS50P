import pathlib


class file_sys():
    def __init__(self) -> None:
        self.folder_path()

    @classmethod
    def folder_path(self, p):
        self.path = pathlib.Path(p)
