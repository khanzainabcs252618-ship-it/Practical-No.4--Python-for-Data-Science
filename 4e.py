print("S096 Zainab Khan")

import numpy as np

arr = np.array([10, 25, 15, 40, 30])

filter_arr = arr == arr.max()

print(arr[filter_arr])
