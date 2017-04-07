# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 20:43:29 2017

@author: parithy
"""

import numpy as np
from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs

import matplotlib.pyplot as plt

centers = [[1,1] ,[5,5],[3,9]]

X, _ = make_blobs(n_samples = 200, centers= centers , cluster_std=1)

plt.scatter(X[:,0],X[:,1])
plt.show()


ms = MeanShift()
ms.fit(X)

labels = ms.labels_
center = ms.cluster_centers_

n_clusters = len(np.unique(labels))

print("Number of cluster =:", n_clusters)

colors= 2*['r.' ,'g.', 'c.','y.']

for i in range(len(X)):
    plt.plot(X[i][0], X[i][1] , colors[labels[i]])

plt.scatter(center[:,0],center[:,1],marker="x" ,s=10 , linewidths=10, zorder= 5)

plt.show()