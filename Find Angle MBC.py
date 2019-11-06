import math

AB = int(input())
BC = int(input())
 
h = math.sqrt(AB**2 + BC**2)
h = h / 2.0
adj = BC / 2.0
print(str(int(round(math.degrees(math.acos(adj/h))))) + "°")
