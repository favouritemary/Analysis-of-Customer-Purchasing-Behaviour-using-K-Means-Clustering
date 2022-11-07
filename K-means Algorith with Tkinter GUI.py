#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import DataFrame
import numpy as np
import random
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox

# Global Variables
file_csv = {}
centroids = []
clusters = {}


def import_file():
    """Function to import file in csv format
    
    It returns file.csv"""
    
    global file_csv
    try:
        file_name = filedialog.askopenfilename() #to open file path
        file_csv = pd.read_csv(file_name) #read file in csv format
        file_csv = pd.DataFrame(file_csv) #convert file to DataFrame
        file_csv.columns = range(file_csv.shape[1]) #arrange file in column
        tk.messagebox.showinfo (title='File Imported', message='Enter the number of clusters and click Enter')
    except:
        tk.messagebox.showerror(title="Error", 
                                message="You have entered the wrong file. Try again")
    

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
            random_numbers = list(set((random.randint(1, data.shape[0]) for i in range(0, 10))))[:int(entry.get())] #select random numbers between from our data
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
        print('The centroids for this clustering are', new_Centroids)

        plot_graph()
    
def plot_graph():
    """ Function to plot the cluster with the centroid"""

    for key in clusters.keys(): 
        cluster = np.array(clusters.get(key))
        plt.scatter(cluster[:, 0], cluster[:, 1])
        plt.scatter(np.array(centroids)[:, 0], np.array(centroids)[:, 1], marker="x", s=50)
        plt.title("Clustering result by Mary Omotosho")

    plt.show()
    
#tkinter call up
        
root = tk.Tk()
root.title ('K-means algorithm developed by Mary Onotosho')

frame = tk.Frame(master=root, width=500, height=500)
frame.pack()

label1 = tk.Label(master=frame, text="K-Means Clustering Analys=is", bg="white", fg="green", width=30, height=3,)
label1.place(x=150, y=0)

button = tk.Button(master=frame, text='1. Click here to import your CSV file', command=import_file, width=30, height=2, bg="black", fg="white")
button.place(x=150,y=100)

label2 = tk.Label(master=frame, text="2. Enter the number of clusters below", bg="blue", fg="white", width=30, height=2,)
label2.place(x=150, y=180)

entry = tk.Entry(master=frame, fg="blue", bg="white")
entry.place(x=150, y=220)

Enter = tk.Button(master=frame, text=' Enter ', command = lambda: kmeans(file_csv), padx=12, pady=9, fg='black')
Enter.place(x=200,y=350)


root.mainloop();