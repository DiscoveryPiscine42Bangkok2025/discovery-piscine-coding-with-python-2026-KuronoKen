#!/usr/bin/env python

oriarray = [2, 8, 9, 48, 8, 22,-12, 2]
dupecheck = set()
for i in oriarray:
    if i > 5 and i+2 not in dupecheck:
        dupecheck.add(i+2)

print(f'Original array : {oriarray}')
print('New array :',dupecheck)
