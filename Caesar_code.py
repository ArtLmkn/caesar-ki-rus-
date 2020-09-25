def Code():
    b = ''
    for i in range(len(a)):
        if a[i] in alphUpper:
            b += alphUpper[alphUpper.index(a[i]) + n % len(alphUpper) - len(alphUpper)]
        elif a[i] in alphLower:
            b += alphLower[alphLower.index(a[i]) + n % len(alphLower) - len(alphLower)]
        else:
            b += a[i]
    print('Результат:', b)

def Decode():
    b = ''
    for i in range(len(a)):
        if a[i] in alphUpper:
            b += alphUpper[::-1][alphUpper[::-1].index(a[i]) + n % len(alphUpper) - len(alphUpper)]
        elif a[i] in alphLower:
            b += alphLower[::-1][alphLower[::-1].index(a[i]) + n % len(alphLower) - len(alphLower)]
        else:
            b += a[i]
    print('Результат:', b)


alphUpper = [i for i in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦСШЩЪЫЬЭЮЯ']
alphLower = [i for i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']

var = (1 if input('Код или декод? ').upper() == 'код'.upper() else 0)
n = int(input('Ключ: '))
a = input('Фраза: ')
if var:
    Code()
else:
    Decode()








