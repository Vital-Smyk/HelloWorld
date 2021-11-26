
n = int(input('Введите N(>2) : '))

l = [int(i) for i in input('Введите значения a, b : ').split()]
sum = l[0] +l[1]
if n > 2 :
    for i in range(2,n) :
        l.append(sum)
        sum += l[i]
    print(l)    
else:
   print('N<2! Повторите ввод!') 
