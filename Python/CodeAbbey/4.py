import math

loop = int(input())

for i in range (loop):
    str_num = input()
    num = str_num.split()
    
    res = int(num[0])/int(num[1])
    res = math.ceil(res)
    
    print(res, " ")
    num = {}
