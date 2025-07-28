#largest element in an array
import numpy as np
a = np.array([1, 7,3])

def LargestElementArray(a):
	largest = a[0];
	for i in a:
		if(i > largest):
			largest = i
	print(largest)
LargestElementArray(a)
