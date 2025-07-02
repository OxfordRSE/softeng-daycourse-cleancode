import numpy as np

arr = np.array([1.7, 1.2, 3.4])
ref_value = 4.0

# np.alltrue checks if all elements are true -- this function was removed in numpy v2
result = np.alltrue(arr < ref_value)

if result:
    print(f"All values are smaller than the reference value {ref_value}.")
else:
    print(f"Not all values are smaller than the reference value {ref_value}.")
