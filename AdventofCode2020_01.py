import pandas as pd 

df = pd.read_excel('AdventofCode01_Col.xlsx')
mylist = df['List'].tolist()

T = 2020

def findPairs(mylist, T):  
    res = [] 
    while mylist: 
        num = mylist.pop() 
        diff = T - num 
        if diff in mylist: 
            res.append((diff, num)) 
          
    res.reverse() 
    return res 
      
print(findPairs(mylist, T)) 

fProduct = 1162*858
print(fProduct)
