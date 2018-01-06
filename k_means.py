#!/usr/bin/python3

from math import *

def dists(point, center):
    dist = []
    dist.append(sqrt((point[0] - center[0][0]) **
                     2 + (point[1] - center[0][1])**2))
    dist.append(sqrt((point[0] - center[1][0]) **
                     2 + (point[1] - center[1][1])**2))
    return dist

def new_center(cl, points):
    new_c1 = [0,0]
    sum_c1 =0
    new_c2 = [0,0]
    sum_c2 = 0
    for i in range(len(points)):
        if cl[i] == 1:
            new_c1 = [ new_c1[0]+points[i][0], new_c1[1] + points[i][1]]
            sum_c1 += 1
        else:
            new_c2 = [ new_c2[0]+points[i][0], new_c2[1] + points[i][1]]
            sum_c2 += 1
    new_c1 = [x / sum_c1 for x in new_c1]
    new_c2 = [x / sum_c2 for x in new_c2]
    print("Novos centros {c1} e {c2}".format(c1=new_c1,c2=new_c2))
    return [new_c1, new_c2]

def main():
    points = [[1, 3], [2, 2], [3, 3], [3, 5], [5, 4], [6, 4], [6, 5], [6, 7], [8, 8], [9, 6]]
    center = [[4, 7], [8, 4]]
    for t in range(20):
        d = []
        c = []
        for p in points:
            d.append(dists(p, center))
            if(d[-1][0] < d[-1][1] or d[-1][0] == d[-1][1]):
                c.append(1)
            else:
                c.append(2)

            print("Ponto {p} é da classe {c} ".format(p=p, c=c[-1]))
    
        new_c = new_center(c, points)
        if new_c == center:
            print("O algoritmo convergiu na iteração {i}".format(i=t))
            break
        
        center = new_c
        
            
if __name__ == "__main__":
    exit(main())
