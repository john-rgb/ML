# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:32:32 2017

@author: 刘创业
"""

import knn
from numpy import *

dataSet, labels = knn.creatDataSet()

testX = array([0.5, 0.5])
k = 3
outputLabel = knn.kNNClassify(testX, dataSet, labels, 3)
print("Your input is:", testX, "and classified to class: ", outputLabel)


testX = array([0.1, 0.3])
outputLabel = knn.kNNClassify(testX, dataSet, labels, 3)
print("Your input is:", testX, "and classified to class: ", outputLabel)