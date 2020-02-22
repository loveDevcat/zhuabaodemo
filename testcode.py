#coding=utf-8
import os

print(os.getcwd())
f = open('/Users/plantkon/PycharmProjects/zhuabaodemo/2.txt')
file = f.readlines()
for line in file:
    print(line)


