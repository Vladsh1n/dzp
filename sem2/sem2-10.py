# программа работает для латинницы 

with open('input.txt', 'r') as file:
    
    #letters = {'а', 'о', 'ю', 'е', 'ё', 'и', 'э', 'я', 'ы', 'у'}
    
    letters = {'a', 'e', 'y', 'u', 'i', 'o'}

    text1 = file.readlines() # читаем файл
    text2 = text1[0].split() # переводим информацию из файла в список слов 
    new_word = ''
    
    # создаём функцию для обработки каждого отдельного слова
    print(text2)
    def ans(word):
        new_word = ''
        for i in range(len(word)):
            if word[i] in letters:
                if word[i -1] not in letters:  
                    new_word += word[i] + 'c' + word[i]
                else:
                    new_word += word[i] 
            else:
                new_word += word[i]       
        print(new_word,  end = ' ')
    
    for j in text2:
        ans(j)
        
    
    