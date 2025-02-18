
import os
import os.path

import sys
import errno

import zipfile

import tqdm

import shutil

BEAMNG_PATH = "/home/x7k3e21/.games/BeamNG.drive Linux/game/content/vehicles/"

BEAMNG_CONTENT_PATH = BEAMNG_PATH + "content/"

BEAMNG_LEVELS_PATH = BEAMNG_CONTENT_PATH + "levels/"
BEAMNG_VEHICLES_PATH = BEAMNG_CONTENT_PATH + "vehicles/"

BEAMNG_COMPRESSION_LIST = [BEAMNG_LEVELS_PATH, BEAMNG_VEHICLES_PATH]

BEAMNG_REQUIRED_SPACE = 15 * (2 ** 20)

def validateDirectory(targetDir):
    if not os.path.isdir(targetDir):
        raise NotADirectoryError("The specified path must point to a directory")
    else:
        return True

def checkAvailableSpace(targetDir, freeSpaceThreshold):
    diskFreeSpace = shutil.disk_usage(targetDir)["free"]

    if diskFreeSpace < freeSpaceThreshold:
        raise OSError(os.strerror(errno.ENOSPC))
    else:
        return True

def compress(folderPath):
    os.chdir(folderPath)

    folderContents = list()

    for filename in sorted(os.listdir(os.getcwd())):
        if filename.endswith(".zip"):
            folderContents.append(filename)
    
    for filename in (pbar:=tqdm.tqdm(folderContents)):
        pbar.set_postfix_str(filename)

        with zipfile.ZipFile(filename, mode="r") as zipFile:
            zipFile.extractall(filename[:-4])

        os.remove(filename)

        with zipfile.ZipFile(filename, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipFile:
            for root, subdirs, files in os.walk(filename[:-4]):
                for nextFile in files:
                    zipFile.write(os.path.join(root, nextFile))

        shutil.rmtree(filename[:-4])

if __name__ == "__main__":
    validateDirectory(BEAMNG_PATH)
        
    #for folderPath in BEAMNG_COMPRESSION_LIST:
    #    compress(folderPath)

