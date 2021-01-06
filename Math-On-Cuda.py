from numba import jit, cuda 
import numpy as np 
from timeit import default_timer as timer    
  
# Run on CPU
def func(a):                                 
    for i in range(10000000): 
        a[i]+= 1      
  
# Run on GPU 
@jit(target ="cuda")                          
def func2(a): 
    for i in range(10000000): 
        a[i]+= 1
        
if __name__=="__main__": 
    n = 10000000                            
    a = np.ones(n, dtype = np.float64) 
      
    start = timer() 
    func(a) 
    print("CPU:", timer()-start)     
      
    start = timer() 
    func2(a) 
    print("GPU:", timer()-start) 
