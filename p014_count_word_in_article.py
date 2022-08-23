# 统计英语文章每个单词出现的次数

word_count = {}

with open("./en_content.txt") as fin:
    for line in fin:
        line = line[:-1]
        words = line.split()
        for word in words:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1

print(sorted(
    word_count.items(),
    key=lambda x: x[1],
    reverse=True
)[:10])

