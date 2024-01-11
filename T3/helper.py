from io import UnsupportedOperation
from pathlib import Path
import os

class File:
    _f = None 
    _path = None
    def __init__(self, name: str, mode="r", content=None) -> None:
        try:
            self._f = open(name, mode)
            self._path = str(Path(__file__).parent.resolve() / self._f.name)
            if content and self._f.writable:
                self._f.write(content)
        except OSError:
            print("OSError occured make sure you have \
                  entered correct file names")   
            raise OSError
        
    def read(self, i=-1):
        return self._f.read(i)
    
    def readlines(self):
        return self._f.readlines()
        
    def write(self, s: str):
        if self._f.writable:
            self._f.write(s)
        else:
            raise UnsupportedOperation
    def writelines(self, l: list):
        self._f.writelines(l)

    def close(self):
        if not self._f.closed:
            self._f.close()
    
    def delete(self):
        self.close()
        os.remove(self._path)
    
    def save_as(self, filename=None):
        if filename and self._f.readable:
            mode = self._f.mode
            self.seek(0)
            lines = self._f.readlines()
            self.close()
            with open(filename, "w") as f:
                f.writelines(lines)
            self._f = open(self._path, mode)

    def seek(self, i):
        return self._f.seek(i)
    
    def __len__(self):
        self.seek(0)
        return len(self._f.readlines())

def inti(msg="Enter a number: "):
    return int(input(msg))

def ip(msg="Enter value: "):
    return input(msg)