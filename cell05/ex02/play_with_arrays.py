#!/usr/bin/env python

oriarray = [1,2,3,4,5]
newarray = []
for i in oriarray:
    if i > 5:
        newarray.append(i+2)

print(f'Original array : {oriarray}')
print('New array :',newarray)
