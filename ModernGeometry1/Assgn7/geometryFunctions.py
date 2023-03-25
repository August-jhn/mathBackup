import math
import matplotlib.pyplot as plt
import numpy as np
import random as rand

#vector difference p1-p2
def subtract(p1,p2):
    return (p1[0]-p2[0], p1[1]-p2[1])

#Compute the angle made by three points (the angle <p1p2p3)
def angle(p1,p2,p3):
    v1=subtract(p1,p2)
    v2=subtract(p3,p2)
    return np.math.atan2(np.linalg.det([v1,v2]),np.dot(v1,v2))

#do two segments intersect
def segintseg(p1,p2,p3,p4):
    """checks to see if the line segment p1p2 intersects the line segment p3p4"""
    return lineintseg(p1,p2,p3,p4) and lineintseg(p3,p4,p1,p2)


#check whether a list of points forms a polygon in cyclic order
def check_poly(polygon):
    if len(set(polygon)) != len(polygon):
        print(set(polygon), polygon)
        print("the vertices are not all distinct")
        return False #if the vertices are not all distinct
            
    for i in range(len(polygon)):
        
        
        for j in range(i + 2, len(polygon)): 
            if i != j:
                if segintseg(polygon[i], 
                             polygon[(i+1) % len(polygon)], 
                             polygon[j], polygon[(j+1)%len(polygon)]):
                    print("edges cross somewhere other than where they're supposed to")
                    return False #if the edges intersect anywhere but the vertices
    return True
    #this algorithm is O(n log(n)) I believe
             
                
#distance between two points
def dist(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

#point of intersection of the lines p1p2 and p3p4
def intersect(p1,p2,p3,p4):
    return (-((p1[0] - p2[0])*(p3[1]*p4[0] - p3[0]*p4[1]) - (p3[0] - p4[0])*(p1[1]*p2[0] - p1[0]*p2[1]))/((p1[0] - p2[0])*(p4[1] - p3[1]) - (p2[1] - p1[1])*(p3[0] - p4[0]))), -(-p1[0]*p2[1]*p3[1] + p1[0]*p2[1]*p4[1] + p1[1]*p2[0]*p3[1] - p1[1]*p2[0]*p4[1] + p1[1]*p3[0]*p4[1] - p1[1]*p3[1]*p4[0] - p2[1]*p3[0]*p4[1] + p2[1]*p3[1]*p4[0])/(p1[0]*p3[1] - p1[0]*p4[1] - p1[1]*p3[0] + p1[1]*p4[0] - p2[0]*p3[1] + p2[0]*p4[1] + p2[1]*p3[0] - p2[1]*p4[0]) 

def square_distance_to_line(p1,p2,p):

    a = -(p2[0] - p1[0])
    b = p2[1] - p1[1]

    return p1



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

def plotgraph(g):
    for edge in g:
        p1 = edge[0]
        p2 = edge[1]
        plt.plot([p1[0],p2[0]],[p1[1],p2[1]], marker='o')
        
    
#From a set of points, find one with smallest y-value
def smally(p):
    p1=p[0]
    for i in range(len(p)):
        if p[i][1]<p1[1]: p1=p[i]
    return p1

def find_center(polygon):
    sx = 0
    xy = 0
    for p in polygon:
        sx += p[0]
        sy += p[1]
    return (sx/len(polygon), sy/len(polygon))

def create_regular_ngon(n, radius= 1, center = (0,0)):
    """creates regular ngon centered at a specified point, with a specified radius"""
    points = []
    for i in range(n):
        theta = i*2*np.pi/n
        x = 2* radius * np.cos(theta) + center[0]
        y = radius * np.sin(theta) + center[1]
        points.append((x,y))
    return points

#vector difference p1-p2
def subtract(p1,p2):
    return (p1[0]-p2[0], p1[1]-p2[1])

#is the x-coordinate of p2 between the x-coordinates of p1 and p3?
def xbetween(p1,p2,p3):
    return p1[0]<=p2[0]<=p3[0] or p3[0]<=p2[0]<=p1[0]

#is the y-coordinate of p2 between the y-coordinates of p1 and p3?
def ybetween(p1,p2,p3):
    return p1[1]<=p2[1]<=p3[1] or p3[1]<=p2[1]<=p1[1]

#do the points of a point-set S lie on the same side of the line p1p2?
def check_sameside(p1,p2,S):
    p3 = S[0]
    for p4 in S[0]:
        if p4 != p3 and lineintseg(p1,p2,p3,p4):
            return False
    return True

def interior_to_triangle(p, t):
    for i in range(3):
        if not check_sameside(t[i], t[(i+1)%3], [p, t[(i + 2)%3]]):
            return False
    return True
       
#find which traingle a point p lies in, assuming everything is in general position, otherwise we're DOOOMED!!
def which_triangle(T, p):
    for t in T:
        if interior_to_triangle(p, t):
            return t



if __name__ == "__main__":
    plotpoly(create_regular_ngon(10))
    
    print(check_poly(create_regular_ngon(10)))
    plt.show()
    print(intersect((0,0), (1,1), (1,2), (5,-10)))