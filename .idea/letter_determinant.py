word = 'test'

length = len(word)
middle = length // 2

if length % 2 == 0:
    # Чётное количество букв — выводим две средних буквы
    result = word[middle - 1:middle + 1]
else:
    # Нечётное количество букв — выводим одну среднюю букву
    result = word[middle]

print(result)
