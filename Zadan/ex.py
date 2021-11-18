def zad_1 ():
    print(l)
    list = []
    n = int(input('Введите N(>2) : '))
    a = l.append(int(input('Введите значения A : ')) 
    b = l.append(int(input('Введите значения B : ')) 
    sum = l[0] +l[1]
    if n > 2 :
        for i in range(2,n) :
            l.append(sum)
            sum += l[i]
        print(l)    
    else:
        print('N<2! Повторите ввод!') 