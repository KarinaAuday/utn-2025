set1= {1, 2, 3, 4, 4, 4, 2, 5}
set2= {8, 5, 6, 7}
union_set = set1.union(set2)
interseccion_set = set1.intersection(set2)
print(type(set1))
print(set1)
set1.add(5)
print(set1)
print ("Union " ,union_set)
print ("Intersección ",     interseccion_set)
set1.discard(77)