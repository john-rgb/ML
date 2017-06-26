# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:32:32 2017

@author: 刘创业
"""

import knn
#from numpy import *

group,labels=knn.creatDataSet()

#print(group)
#print(labels)
def classify(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    diffMat=tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistanses=sqDiffMat.sum(axis=1)
    distenses=sqDistanses**0.5
    sortedDistenses=distenses.argsort()
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistenses[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]