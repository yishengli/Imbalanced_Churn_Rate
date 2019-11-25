# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:08:52 2019

@author: yl18yn
"""

# Returns the maximum value that can be put in a knapsack of 
# capacity cap 
def knapSack(cap, weight, val, n): 
  
    # Base Case 
    if n == 0 or cap == 0: 
        return 0
  
    # If weight of the nth item is more than Knapsack of capacity 
    # cap, then this item cannot be included in the optimal solution 
    if (weight[n-1] > cap): 
        return knapSack(cap, weight, val , n-1) 
  
    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
    else: 
        return max(val[n-1] + knapSack(cap-weight[n-1], weight, val, n-1), 
                   knapSack(cap, weight, val, n-1)) 
  
  
if __name__ == '__main__':

    # To test above function 
    val = [60, 100, 120] 
    weight = [10, 20, 30] 
    cap = 50
    n = len(val) 
    print(knapSack(cap, weight, val, n))
    # output 220
