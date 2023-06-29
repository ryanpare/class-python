#!/usr/bin/env python3


multiples = []
for outer in range(1,5):
  multiples.append([])
  for inner in range(1,2):
    print("Outer:", outer, ", Inner:", inner)
    multiples[outer-1].append(inner)
print(multiples)


