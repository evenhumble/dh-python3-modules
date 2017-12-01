# -*- coding:utf-8 -*-
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier


def predict_demo(input_features):
    iris = datasets.load_iris()
    knn = KNeighborsClassifier()
    knn.fit(iris.data,iris.target)

    predictInt = knn.predict(input_features)
    if predictInt[0] == 0:
        predictString = 'setosa'
    elif predictInt[0] == 1:
        predictString = 'versicolor'
    elif predictInt[0] == 2:
        predictString = 'virginica'
    else:
        predictString = 'null'

    return predictString