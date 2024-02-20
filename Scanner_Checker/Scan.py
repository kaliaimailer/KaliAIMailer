import os

def scan_files_and_directories(rootDir):
    for dirName, subdirList, fileList in os.walk(rootDir):
        print(f'Found directory: {dirName}')
        for fname in fileList:
            print(f'\t{dirName}/{fname}')

# Specify the directory to scan
rootDir = '.'  # Current directory. Change this to the path you want to scan.

# Start scanning
scan_files_and_directories(rootDir)
