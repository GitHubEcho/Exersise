import math
points =[[4,6],[4,7],[4,4],[2,5],[1,1]]
dict = {}
def kClosest( points, origin, k):
    for x,y in points:
        l = math.sqrt((x- origin[0])**2 + (y- origin[0])**2)
        dict[l] = [x,y]
    print(dict.items())
    sorted(dict.items())
    print(dict)
kClosest(points,[0,0],3)