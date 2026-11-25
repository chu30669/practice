import copy
'''行交换'''
def row_exchange(lst,a,b):
    lst0=copy.deepcopy(lst)
    lst0[a],lst0[b]=lst0[b],lst0[a]
    return lst0
'''列交换'''
def col_exchange(lst,a,b):
    lst0=copy.deepcopy(lst)
    for i in range(len(lst0)):
        lst0[i][a],lst0[i][b]=lst0[i][b],lst0[i][a]
    return lst0
'''行倍乘'''
def row_multiple(lst,a,num):
    lst0=copy.deepcopy(lst)
    lst0[a]=[x*num for x in lst0[a]]
    return lst0
'''列倍乘'''
def col_multiple(lst,a,num):
    lst0=copy.deepcopy(lst)
    for i in range(len(lst0)):
        lst0[i][a]*=num
    return lst0
'''行倍加'''
def row_addition(lst,a,b,num):
    lst0=copy.deepcopy(lst)
    lst0[a]=[x+y*num for x,y in zip(lst0[a],lst0[b])]
    return lst0
'''列倍加'''
def col_addition(lst,a,b,num):
    lst0=copy.deepcopy(lst)
    for i in range(len(lst0)):
        lst0[i][a]+=lst0[i][b]*num
    return lst0

import random
import ast

while True:
    functions = [row_exchange, col_exchange, row_multiple, col_multiple, row_addition, col_addition]
    func_dict = dict(zip([1, 2, 3, 4, 5, 6], functions))
    number = random.randint(1, 6)
    # 给6种变换函数编号，方便后续调用
    params = {1: (*random.sample(range(3), 2),),
              2: (*random.sample(range(3), 2),),
              3: (random.randint(0, 2), random.randint(2, 6)),
              4: (random.randint(0, 2), random.randint(2, 6)),
              5: (*random.sample(range(3), 2), random.randint(2, 6)),
              6: (*random.sample(range(3), 2), random.randint(2, 6))}
    func=func_dict[number]
    args=params[number]
    E=[[1,0,0],[0,1,0],[0,0,1]]
    matrix=[[random.randint(-5,5) for _ in range(3)] for _ in range(3)]
    print(matrix)
    n=(*args,)             #固定一个随机参数
    I=func(E,*n)
    result=func(matrix,*n) #用同一个参数处理目标矩阵与单位矩阵，从而获得答案所需的初等矩阵
    print(result)
    ans=ast.literal_eval(input("请输入对应初等矩阵，并判断左右乘(以空格间隔)："))
    if ans==I:
        print("恭喜答对")
        print("是否继续回答？(是请回答y，否请回答n)")
        if input()=="n":
            print("游戏结束")
            break
        else:
            continue
    else:
        print("遗憾答错")
        print("是否继续回答？(是请回答y，否请回答n)")
        if input() == "n":
            print("游戏结束")
            break
        else:
            continue


#if __name__=='__main__':
    #print(func([[1,0,0],[0,1,0],[0,0,1]],1,0))
#    func=func_dict[number]
#    args=params[number]
#    result=func(E, *args)
#    print(result)