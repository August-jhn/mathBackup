import math
import matplotlib.pyplot as plt
import numpy as np

#vector difference p1-p2
def subtract(p1,p2):
    return (p1[0]-p2[0], p1[1]-p2[1])

#Compute the angle made by three points (the angle <p1p2p3)
def angle(p1,p2,p3):
    v1=subtract(p1,p2)
    v2=subtract(p3,p2)
    return np.math.atan2(np.linalg.det([v1,v2]),np.dot(v1,v2))

#distance between two points
def dist(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

#point of intersection of the lines p1p2 and p3p4
def intersect(p1,p2,p3,p4):
    return (-((p1[0] - p2[0])*(p3[1]*p4[0] - p3[0]*p4[1]) - (p3[0] - p4[0])*(p1[1]*p2[0] - p1[0]*p2[1]))/((p1[0] - p2[0])*(p4[1] - p3[1]) - (p2[1] - p1[1])*(p3[0] - p4[0]))), -(-p1[0]*p2[1]*p3[1] + p1[0]*p2[1]*p4[1] + p1[1]*p2[0]*p3[1] - p1[1]*p2[0]*p4[1] + p1[1]*p3[0]*p4[1] - p1[1]*p3[1]*p4[0] - p2[1]*p3[0]*p4[1] + p2[1]*p3[1]*p4[0])/(p1[0]*p3[1] - p1[0]*p4[1] - p1[1]*p3[0] + p1[1]*p4[0] - p2[0]*p3[1] + p2[0]*p4[1] + p2[1]*p3[0] - p2[1]*p4[0]) 

#checks if two line segments intersect
def segintseg(p1,p2,p3,p4):
    """checks to see if the line segment p1p2 intersects the line segment p3p4"""
    return lineintseg(p1,p2,p3,p4) and lineintseg(p3,p4,p1,p2)


#does the line p1p2 intersect the line segment p3p4?
def lineintseg(p1,p2,p3,p4):
    if p1[0]-p2[0]==0 and p3[0]-p4[0]==0:
        if p1[0]==p3[0]:
            return True
        else: return False
    if p1[0]-p2[0]!=0 and p3[0]-p4[0]!=0 and (p1[1]-p2[1])*(p3[0]-p4[0])==(p3[1]-p4[1])*(p1[0]-p2[0]):
        if (p1[1]-p2[1])*(p1[0]-p4[0])==(p1[1]-p4[1])*(p1[0]-p2[0]):
            return True
        else: return False
    return (p3[0]==p4[0] and ybetween(p3,intersect(p1,p2,p3,p4),p4)) or (p3[0]!=p4[0] and xbetween(p3,intersect(p1,p2,p3,p4),p4))
import matplotlib.pyplot as plt

#Plot a piecewice linear curve.  Input vertices in cyclic order
def plotline(p):
    for i in range(len(p)-1):
        plt.plot([p[i][0],p[i+1][0]],[p[i][1],p[i+1][1]], marker='o')
        
#plot a set of points
def plotpoints(p):
    for i in range(len(p)):
        plt.plot([p[i][0],p[i][0]],[p[i][1],p[i][1]], marker='o')
        

#plot a polygon.  Input vertices in cyclic order
def plotpoly(p):
    for i in range(len(p)-1):
        plt.plot([p[i][0],p[i+1][0]],[p[i][1],p[i+1][1]], marker='o')
    plt.plot([p[len(p)-1][0],p[0][0]],[p[len(p)-1][1],p[0][1]])
    
#From a set of points, find one with smallest y-value
def smally(p):
    p1=p[0]
    for i in range(len(p)):
        if p[i][1]<p1[1]: p1=p[i]
    return p1

#vector difference p1-p2
def subtract(p1,p2):
    return (p1[0]-p2[0], p1[1]-p2[1])

#is the x-coordinate of p2 between the x-coordinates of p1 and p3?
def xbetween(p1,p2,p3):
    return p1[0]<=p2[0]<=p3[0] or p3[0]<=p2[0]<=p1[0]

#is the y-coordinate of p2 between the y-coordinates of p1 and p3?
def ybetween(p1,p2,p3):
    return p1[1]<=p2[1]<=p3[1] or p3[1]<=p2[1]<=p1[1]