# 按文件后缀整理文件夹

import os

dirPath = "./arrange_dir"
for file in os.listdir(dirPath):
    ext = os.path.splitext(file)[1]
    ext = ext[1:]
    if not os.path.isdir(f"{dirPath}/{ext}"):
        os.mkdir(f"{dirPath}/{ext}")
    print(file, ext)



