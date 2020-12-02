import pandas as pd 

df = pd.read_excel('AdventofCode01_Col.xlsx')
mylist = df['List'].tolist()

T = 2020

from itertools import combinations 
  
def findTrio(mylist, T):    
    res = [] 
    for var in combinations(mylist, 3): 
        if var[0] + var[1] + var[2] == T: 
            res.append((var[0], var[1], var[2])) 
          
    return res 
      
print(findTrio(mylist, T)) 

import numpy as np
myTrio = (findTrio(mylist, T)) 
result = np.prod(np.array(myTrio))  
print(result)
print('This is overwhelmingly gratifying')
