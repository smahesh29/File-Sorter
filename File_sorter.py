#File Sorter by Mahesh Sawant 

import os,shutil

s=os.chdir("Downloads")
current = os.getcwd()

files=os.listdir(current)

images=[".jpeg",".png",".jpg",".gif"] #extensions for images
text=[".doc",".txt",".pdf",".xlsx",".docx",".xls",".rtf"] #extensions for text files
videos=[".mp4",".mkv"] #extensions for videos
sounds=[".mp3",".wav",".m4a"] #extensions for sounds
applications=[".exe",".lnk"] #extensions for applications
codes = [".c",".py",".java",".cpp",".js",".html",".css",".php"] #extensions for codes

print("Sorting the files...")

for file in files:
    dest = ""
    for ex in images:
        if file.endswith(ex):
            dest='../Images'
            shutil.move(file,dest)
            break

    for ex in text:
        if file.endswith(ex):
            dest='../Text'
            shutil.move(file,dest)
            break

    for ex in sounds:
        if file.endswith(ex):
            dest='../Sounds'
            shutil.move(file,dest)
            break

    for ex in videos:
        if file.endswith(ex):
            dest='../Videos'
            shutil.move(file,dest)
            break

    for ex in applications:
        if file.endswith(ex):
            dest= '../Applications'
            shutil.move(file,dest)
            break

    for ex in codes:
        if file.endswith(ex):
            dest= '../Codes'
            shutil.move(file,dest)
            break

    if dest == "":
        shutil.move(file,'../Others')

print("Sorting Completed...")
