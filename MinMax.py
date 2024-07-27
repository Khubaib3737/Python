import math
def minMax(depth, maxdepth, Index, values, turn):
  if(depth==maxdepth):
    return values[Index]
  if(turn):
    return max(minMax(depth+1,maxdepth,Index*2, values,False),minMax(depth+1,maxdepth,Index*2+1, values,False))
  else:
    return min(minMax(depth+1,maxdepth,Index*2, values,True),minMax(depth+1,maxdepth,Index*2+1, values,True))

Terminal_values = [2,3,6,7,77,-9,11,23]
result = minMax(0, 3, 0, Terminal_values, True)
print(result)
