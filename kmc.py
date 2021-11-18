import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#data
dat=pd.read_csv('Basic\ArmyPerformance.csv')
x=np.array(dat)
min_of_features=np.zeros((1,3))
max_of_features=np.zeros((1,3))
for i in range(3):
    min_of_features[0,i]=min(x[:,i])
    max_of_features[0,i]=max(x[:,i])
cluster_centers=np.zeros((3,3))
for i in range(3):
    for j in range(3):
        cluster_centers[i,j]=round(random.uniform(min_of_features[0,j],max_of_features[0,j]),3)
#distance
def distance_find(a,b):
    total_1=np.square(a[0]-b[0,0])+np.square(a[1]-b[0,1])+np.square(a[2]-b[0,2])
    
    total_2=np.square(a[0]-b[1,0])+np.square(a[1]-b[1,1])+np.square(a[2]-b[1,2])
    
    total_3=np.square(a[0]-b[2,0])+np.square(a[1]-b[2,1])+np.square(a[2]-b[2,2])
    
    vec=np.array([total_1,total_2,total_3])
    if min(vec)==total_1:
        return 0
    elif min(vec)==total_2:
        return 1
    elif min(vec)==total_3:
        return 2
#clustermean
def mean_finder():
    cluster_new=np.zeros((3,3))
    for i in range(3):
        number_of_elements=sum(cluster_labels==i)
        for j in range(3):
            total=0
            for z in range(len(cluster_labels)):
                if cluster_labels[z]==i:
                    total=total+x[z,j]
                else:
                    total=total
            cluster_new[i,j]=round(total/(number_of_elements[0]+0.001),4)
    return cluster_new

cluster_labels=np.zeros((len(x),1))
for iteration in range(4):
    for i in range(len(x)):
        row=x[i,:]
        cluster_labels[i]=distance_find(row,cluster_centers)
    cluster_centers=mean_finder()
#plot
cluster_labels2=np.array(cluster_labels)
cluster_labels2=np.zeros(len(x))
cluster_labels2[:]=cluster_labels[:,0]
np.save("finalcluster_centroid.npy",cluster_labels2)
fig=plt.figure()
ax=Axes3D(fig)
ax.scatter(x[cluster_labels2==0,0],x[cluster_labels2==0,1],x[cluster_labels2==0,2],color='red')
ax.scatter(cluster_centers[0,0],cluster_centers[0,1],cluster_centers[0,2],color='red',marker='o',s=120)
ax.scatter(x[cluster_labels2==2,0],x[cluster_labels2==2,1],x[cluster_labels2==2,2],color='green')
ax.scatter(cluster_centers[2,0],cluster_centers[2,1],cluster_centers[2,2],color='green',marker='o',s=120)
ax.scatter(x[cluster_labels2==1,0],x[cluster_labels2==1,1],x[cluster_labels2==1,2],color='blue')
ax.scatter(cluster_centers[1,0],cluster_centers[1,1],cluster_centers[1,2],color='blue',marker='o',s=120)
ax.set_xlabel("Strength-->")
ax.set_ylabel("Obedience-->")
ax.set_zlabel("Mobility-->")
plt.show()
