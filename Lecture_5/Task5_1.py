# -*- coding: utf-8 -*-

"""
A = {1, 8, 2,4}

B = {4, 9, 2, 7}

print(A)

print(B)

print(A|B)

print(A&B)

print(A-B)

print(A^B)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict['model'])


import numpy as np


out_arr_1 = np.random.randint(2, 10, 8) 

print(out_arr_1);



out_arr_2 = np.random.randint(2, 10, (2, 3)) 

print(out_arr_2);



out_arr_3 = np.random.randint(2, 10, (2, 3, 4)) 

print(out_arr_3);

"""

import numpy as np

from scipy import stats


data = np.random.randint(1, 11, 5) 

print(data);

print(np.mean(data))

print(np.median(data))

print(stats.mode(data))

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)

print(data);
print(np.mean(data))
print(np.var(data))
print(np.std(data))



























