import numpy as np

flowers=np.array(["Lotus","Tulip","Sunflower","Aster","Lilly"])
# size of the array
print(flowers.size)
# Dimention of an  array
print(flowers.ndim)
# Shape of an Array
print(flowers.shape)
# Read Elements
for i in range(0,5):
    print(flowers[i])