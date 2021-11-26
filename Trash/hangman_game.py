import random
import os

word_list = {
    'автомобиль': 'Это транспорт.' ,
    'яблоко':'Это фрукт.', 
    'учитель':'Это профессия', 
    'береза':'Это фрукт.', 
    'чупачупс':'Это сладость.', 
    'гамбургер':'Это еда, фастфуд.',
    'рука':'Это часть тела.' }

def game():
    select_word = random.choice(list(word_list.keys()))
    help = word_list[select_word]
    used_letters = ''
    word_len = 0
    num_moves = 5
    while num_moves > 0:
        os.system('cls') 
        print ('Подсказка :', help)    
        print('[',end='   ')
        for letter in select_word:
            if letter in used_letters :
                print (letter,end=' ')
                word_len += 1
            else:
                print ('_',end=' ') 
        print('   ]')

        if word_len is len(select_word):
            os.system('cls')
            print ('Поздаравляю!Ты победил!')
            print ('Искомое слово : ', select_word)
            break  

    
        print (f'Осталось : {num_moves} попыток!')

        input_letter = input('Введите букву: ')
        used_letters += input_letter

        if word_len is len(select_word):
            os.system('cls')
            print ('Поздаравляю!Ты победил!')
            print ('Искомое слово : ', select_word)
            break  
        if input_letter not in select_word and input_letter != '' and num_moves>0:
            num_moves -= 1
        word_len = 0

    if num_moves == 0:
        os.system('cls')    
        print('Ты использовал все попытки! Игра окончена!')
        print ('Искомое слово : ', select_word)


game()
