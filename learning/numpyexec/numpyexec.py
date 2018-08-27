# -*- coding:utf-8 -*-
import numpy as np

array_0 = np.array([
    [1,2,3],
    [2,3,4],
    [3,4,5],
    [4,5,6]
], dtype=np.int16)
print(array_0)
print(array_0.shape)

#reshape
print("\n11111111111111111")
array_1 = np.arange(12).reshape((4,3))
print(array_1)

#线段
print("\n2222222222222222222")
array_2 = np.linspace(0,12,6).reshape(2,3)
print(array_2)

#元素判断
print("\n3333333333333333333")
array_3 = np.array([10,20,30,40])
array_4 = np.arange(4)
print(array_3 - array_4)
print((array_3 - array_4) < 20)

#矩阵乘法
print("\n555555555555555555")
array_5 = np.array([[0,1],[2,3]])
array_6 = np.arange(4).reshape(2,2)
print(np.dot(array_5, array_6))
print(array_5.dot(array_6))

#random, 二维数组中, axis=1表示行, axis=0表示列
print("\n777777777777777777")
array_7 = np.random.randint(0, 12, size=(3,4))
print(array_7)
print(array_7.sum(axis=1), array_7.min(axis=0), array_7.max(axis=1))
#最大最小值索引
print("\naaaaa")
print(np.max(array_7), np.argmax(array_7))
print(np.min(array_7), np.argmin(array_7))
#平均值,axis=0表示按列求平均
print("\nbbbbbb")
print(np.mean(array_7), array_7.mean())
print(np.mean(array_7, axis=0))
print(np.average(array_7))
#中位数
print("\nccccc")
print(np.median(array_7))
#降为一维
print(array_7.flatten())
#生成迭代器
for i in array_7.flat:
    print(i)
#累加
print("\ndddddd")
print(np.cumsum(array_7))
#累差
print(np.diff(array_7))
#nonzero
print("\neeeeee")
print(np.nonzero(array_7))
#转置
print(np.transpose(array_7))
#过滤,所有小于5的变成5，大于9的变成9
print(np.clip(array_7,5,9))

#索引
print("\n888888888888888")
array_8 = np.random.randint(0, 12, size=(3,4))
print(array_8)
print(array_8[2,1])
print(array_8[2,:])
print(array_8[2,1:3])

#合并, vstack是垂直合并, 每个元素
print("\n999999999999")
array_9 = np.arange(5)
array_10 = np.arange(0, 10, 2)
print(array_9)
print(array_10)
print(np.vstack((array_9, array_10)))
print(np.hstack((array_9, array_10)))
print(np.c_[array_9])
print(np.c_[array_9, array_10])
print(np.concatenate((np.c_[array_9], np.c_[array_10]), axis=1))
print(np.concatenate((np.c_[array_9], np.c_[array_10]), axis=0))

#分割
print("\naaaaaaaaaaaaaa")
array_11 = np.arange(12).reshape(3,4)
print(array_11)
print(np.split(array_11, 3, axis=0))
print(np.vsplit(array_11, 3))
print(np.split(array_11, 4, axis=1))
print(np.hsplit(array_11, 4))
print(np.array_split(array_11, 3, axis=1))

#拷贝
print("\nbbbbbbbbbbbbbb")
array_12 = np.arange(4)
tmp = array_12.copy()
array_12[0] = 123
print(array_12)
print(tmp)
