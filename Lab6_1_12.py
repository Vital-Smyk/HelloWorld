def DigitCount(K:int):
    C = len(str(K))
    return C

l = []
l = list(map(int,input('Введите 5 целых положительных чисел: ').split())) 
for i in range(0,5):
    print('{n} : {c};'.format(n = l[i], c = DigitCount(l[i])))


