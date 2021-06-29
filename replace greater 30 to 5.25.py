import numpy as np
  
# Creating a 2-D Numpy array
n_arr = np.array([[45.42436315, 52.48558583, 10.32924763],
                  [5.7439979, 50.58220701, 25.38213418]])
print("Given array:")
print(n_arr)
  
print("\nReplace all elements of array which are greater than 30. to 5.25")
n_arr[n_arr > 30.] = 5.25
  
print("New array :\n")
print(n_arr)