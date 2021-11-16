import time

def sum_of_n_2(n):
  start = time.time()
  the_sum = 0
  for i in range(1, n + 1):
    the_sum = the_sum + i
    end = time.time()
    
  return the_sum, end - start 

for i in range(5):
  print("sum is %d required %10.7f seconds" % sum_of_n_2(10000))

#using the time import, we can take a note of the time at the start of the function and another at the end.

 
