#coding:utf-8
import numpy as np
import csv
import os
import sys

argv = sys.argv
argc = len(argv)

if argc < 2:
    exit()

os.chdir(argv[1])


fileTemplate = "fscMat%s.csv"

#a = np.loadtxt( "preMat0.csv", delimiter=","  )
#a = a[1:]

aveArray = np.zeros((9,10))

for i in range(30):
    filename = fileTemplate % i
    buff = np.loadtxt(filename, delimiter=",")
    buff = buff[1:] #先頭はインデックスなので取り除く
    aveArray += buff

aveArray /= 30.0 #平均を算出
# 書き出す
np.savetxt("aveOut.csv", aveArray, delimiter=",")
