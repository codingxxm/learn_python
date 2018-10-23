#追加字符串
from sys import argv

script , filename = argv

target = open(filename,'a')
print("以追加模式打开文件")

str = input("输入追加的内容")

target.write(str)

target.close()
print("追加完成")
