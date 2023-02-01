"""
作业1：
    （1）、创建文件：data.txt，一共10000行，每行存放一个1-100间的随机整数。
    （2）、读数据：把文件中的数据读出来，以列表的形式存储，不带换行符
作业2：
    找出文件中数字出现最多的十个数字。
"""
# 函数式编程
import random
import re
from collections import Counter
def write_data():
    """
    写数据
    :return:
    """
    with open("data.txt","w") as f:
        for i in range(10000):
            f.write(str(random.randint(1,100))+"\n")
    print("数据写入完毕")


def read_data():
    """
    读数据
    :return:
    """
    list_data = []  # 定义空列表，存放每行数据
    with open("data.txt","r") as f: # 读取文件
        for line in f: # 循环遍历每行数据
            result = re.findall(r"\d+",line) # 匹配数字
            list_data.append(result[0]) # 添加数据到列表
    print(list_data)
    return list_data


def deal_data():
    """
    数据处理
    :return:
    """
    count_list = Counter(read_data())
    #  传进去一个可选参数n(代表获取数量最多的前n个元素，如果不传参数，代表返回所有结果)
    #  返回一个列表（里面的元素是一个元组，元组第0位是被计数的具体元素，元组的第1位是出现的次数
    most_count_list = count_list.most_common(10)
    print(most_count_list)



if __name__ == '__main__':
    write_data()
    deal_data()




