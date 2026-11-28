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
'''转置'''
def transpose(lst):
    lst0=list(list(i) for i in zip(*lst))
    return lst0
'''矩阵的乘法'''
def multiply(lst1,lst2):
    lst0=[[sum(i*j for i,j in zip(row,col)) for col in transpose(lst2)] for row in lst1]
    return lst0

def order_judge(e, mtr, res, num):
    left=multiply(e, mtr)
    right=multiply(mtr, e)
    if left==res and right!=res:
        return "left"
    if right==res and left!=res:
        return "right"
    return "left" if num%2==1 else "right"   # 两式相等时按变换类型兜底

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
    I=func(E,*args)
    result=func(matrix,*args) #用同一个参数处理目标矩阵与单位矩阵，从而获得答案所需的初等矩阵
    truth=order_judge(I,matrix,result,number)
    print(result)
    print(f"本行用于复制:{E},您可以在粘贴的列表上进行修改，使其变成您想要的初等矩阵")
    ans=ast.literal_eval(input("请输入对应初等矩阵:"))
    if ans!=I:
        print(f"遗憾答错，正确初等矩阵为{result},方向为{truth}({'左乘' if truth=='left' else '右乘'})")
        print("是否继续回答？(是请回答y，否请回答n)")
        if input()=="n":
            print("游戏结束")
            break
        else:
            continue
    else:
        print("矩阵正确")
        order=input("请判断左右乘(左用left,右用right)：")
        if order==truth:
            print("恭喜答对!")
        else:
            print(f"遗憾答错,这一步是{truth}({'左乘' if truth=='left' else '右乘'})")
    print("是否继续回答？(是请回答y，否请回答n)")
    if input()=="n":
        print("游戏结束")
        break



if __name__=='__main__':
    pass