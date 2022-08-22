

import os
print(os.path.getsize("en_content.txt"))

sum_size = 0
for file in os.listdir("."):
    if os.path.isfile(file): # 过滤掉目录
        sum_size += os.path.getsize(file)
        # print(file)

print(sum_size/1000,"kb") # 除以1000 是转成 kb

