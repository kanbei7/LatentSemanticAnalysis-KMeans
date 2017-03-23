import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import linalg
import time

#record running time of each stage seperately


#foreach patient collect a set of dates
	#foreach date select all the data
		
#worker process thread safe
#clean commas
#cancatenate strings, use comma to seperate
#add doc to list

#wordvocab

#map doc to vectors


#get a matrix

#tfidf

#svd



#k-means(in another python file)


#foreach (number of clusters)  run 10 times
#pick up the cluster with optimal silhoutte score 

#pick up the number of cluster with optimal silhoutte score 

#visualization

#write result

'''
more efficient ways to calculate silhoutte score
'''

def vectorNorm(v):
	return math.sqrt(np.dot(v,v))
	#return linalg.norm(v)

def cosineDistance(u,v):
	return float(np.dot(u,v))/(vectorNorm(u)*vectorNorm(v))

def distance(u,v):


'''
then define the average dissimilarity of point i
to a cluster c 
as the average of the distance from i 
to all points in c
'''
def dissimilarity(i,c):
	ans=0.0
	for u in c:
		ans+=distance(i,u)
	return ans/len(c)

def measure_A():


def measure_B():


def avg_Silhouette(clusters):
	ans=[]
	for k in range(len(clusters)):
		c=clusters[k]
		tmp=0.0
		for i in c:
			a=measure_A(i,clusters,k)
			b=measure_B(i,clusters,k)
			d=max(a,b)
			tmp+=(b-a)/d
		ans.append(tmp/len(c))
	return ans


