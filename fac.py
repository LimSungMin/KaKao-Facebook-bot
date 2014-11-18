import time
from math import *
now = time.time()
result = 1
n = 100000
while n>=1:
	result *= n
	n = n-1
print result
print time.time()-now
	
