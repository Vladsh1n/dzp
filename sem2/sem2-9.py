symbols = ['.', '!', '?']
count = 0
with open('input.txt', 'r') as f:
    text = f.readlines()
    text_analyz = [i for i in text[0]]
    text_analyz.pop()
    text_analyz.append(' ')
    a = len(text_analyz) - 1
    for i in range(0, a):
        pairs = text_analyz[i] + text_analyz[i+1]
        if pairs == '. ' or pairs == '! ' or pairs == '? ':
            count += 1 
print(count)