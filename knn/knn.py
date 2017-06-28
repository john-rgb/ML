# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:10:41 2017

@author: 刘创业
"""

from numpy import *
import operator

def creatDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,labels
def kNNClassify(newInput, dataSet, labels, k):  
    numSamples = dataSet.shape[0]# shape[0] stands for the num of row样本的个数
    #print(numSamples)
    ## step 1: calculate Euclidean distance  
    # tile(A, reps): Construct an array by repeating A reps times  
    # the following copy numSamples rows for dataSet  
    diff = tile(newInput, (numSamples, 1)) - dataSet # Subtract element-wise求差值
    # print(diff)
    squaredDiff = diff ** 2 # squared for the subtract求x的平方和y的平方
    # print(squaredDiff)
    squaredDist = sum(squaredDiff, axis = 1) # sum is performed by row平方和
    # print(squaredDist)
    distance = squaredDist ** 0.5  #平方和开方也就是距离
    # print(distance)
  
    ## step 2: sort the distance  
    # argsort() returns the indices that would sort an array in a ascending order
    print(distance)
    sortedDistIndices = argsort(distance)
    print(sortedDistIndices)
  
    classCount = {} # define a dictionary (can be append element)  
    for i in range(k):  
        ## step 3: choose the min k distance
        print(i)
        print(sortedDistIndices[i])
        voteLabel = labels[sortedDistIndices[i]]
        print(voteLabel)
  
        ## step 4: count the times labels occur  
        # when the key voteLabel is not in dictionary classCount, get()  
        # will return 0  
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1  
  
    ## step 5: the max voted class will return  
    maxCount = 0  
    for key, value in classCount.items():  
        if value > maxCount:  
            maxCount = value  
            maxIndex = key  
  
    return maxIndex   