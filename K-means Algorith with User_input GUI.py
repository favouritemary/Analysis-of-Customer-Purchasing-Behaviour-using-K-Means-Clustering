import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import random

# Global Variables
clusters = {}
centroids = []

# Enter data in csv format
import_file=input('please enter a csv data in format data.csv: ')
data = pd.read_csv(import_file)
data = pd.DataFrame(data)
First_column = input ('please input the first column: ')
Second_column = input ('please the second column: ')
    
data = data[[First_column, Second_column]]

a = int(input('please enter number of clusters')) # number of clusters


def find_centroid(numbers):
    
    """ Function to calculate the centroid of each cluster.
    
    It returns mean point of each cluster """
    
    cent = np.array(numbers)  # group of numbers in array
    cent = np.round(np.mean(cent, axis=0), 2) # find the average of these numbers and round off to 2d.p
    return cent



def find_cluster (clust):
    """ Function to find the cluster a centroid belong.
    
    It returns the nearest point to a centroid """
    
    distance = np.sqrt(np.sum((np.array(clust) - centroids)**2, axis=1))
    minimum_distance = min(distance) # the nearest point to a centroid
    return distance.tolist().index(minimum_distance) + 1



def kmeans(data):
    
    """ Fuction to perform k-means clustering 
    
    It returns the clustering result of our data and the centroids of each cluster """
    
    global centroids
    
    while True:
        
        #select centroids from our data
        if len(centroids) == 0:
            random_numbers = list(set((random.randint(1, data.shape[0]) for i in range(0, len (data)))))[:a] #select random numbers between from our data
            centroids = [data.iloc[i].tolist() for i in random_numbers] # locate the centroids for these numbers

        new_Centroids = []
        #form cluster and assign centroid to each cluster
        for i in range(np.array(centroids).shape[0]):
            clusters[i + 1] = [] # initial clusters
        for i in range(data.shape[0]):
            cluster_pt = find_cluster(np.array(data.iloc[i])) # assign each point to a cluster       
            clusters[cluster_pt].append(list(data.iloc[i]))    
        for i in clusters.keys():
            new_Centroids.append(find_centroid(clusters[i]).tolist()) #add centroid to each cluster

            

        if(new_Centroids == centroids): #stop iteration once there is no change in the location of centroids
            break


        centroids = new_Centroids
        print('The centroid for this clustering is', new_Centroids)

        plot_graph()

    
    
def plot_graph():
    """ Function to plot the cluster with the centroid"""

    for key in clusters.keys(): 
        cluster = np.array(clusters.get(key))
        plt.scatter(cluster[:, 0], cluster[:, 1])
        plt.scatter(np.array(centroids)[:, 0], np.array(centroids)[:, 1], marker="x", s=50)
        plt.title("Clustering result by Mary Omotosho")

    plt.show()


kmeans(data)


# In[ ]:
