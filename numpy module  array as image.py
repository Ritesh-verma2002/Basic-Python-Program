import numpy as np
import matplotlib.pyplot as plt
mat=np.zeros([100,100,3])
print(mat)
for i in range(0,100,20):
    mat[i+10:i+20,:]=1
    mat[:,i + 10: i+20] = 1
plt.imshow(mat)
plt.plot(color='green')
plt.show()