import copy

def row_exchange(lst,a,b):
    lst0=copy.deepcopy(lst)
    lst0[a],lst0[b]=lst0[b],lst0[a]
    return lst0

def col_exchange(lst,a,b):
    lst0=copy.deepcopy(lst)
    for i in range(len(lst0)):
        lst0[i][a],lst0[i][b]=lst0[i][b],lst0[i][a]
    return lst0

def row_multiple(lst,a,num):
    lst0=copy.deepcopy(lst)
    lst0[a]=[x*num for x in lst0[a]]
    return lst0

def col_multiple(lst,a,num):
    lst0=copy.deepcopy(lst)
    for i in range(len(lst0)):
        lst0[i][a]*=num
    return lst0

def row_addition(lst,a,b,num):
    lst0=copy.deepcopy(lst)
    lst0[a]=[x+y*num for x,y in zip(lst0[a],lst0[b])]
    return lst0

def col_addition(lst,a,b,num):
    lst0=copy.deepcopy(lst)
    for i in range(len(lst0)):
        lst0[i][a]+=lst0[i][b]*num
    return lst0

import random

E=[[1,0,0],[0,1,0],[0,0,1]]




if __name__=='__main__':
    print(row_exchange([[1,0,0],[0,1,0],[0,0,1]],1,0))