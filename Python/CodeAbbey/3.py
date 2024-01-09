loop = int(input())

for i in range (loop):
    str_in = input()
    num = str_in.split()
    
    num1 = int(num[0])
    num2 = int(num[1])
    num3 = int(num[2])
    
    high = min(num1, num2, num3)
    
    print(high, " ")