f = open("17.txt")  # Открываем файл
arr = [int(x) for x in f.readlines()]  # Создаем массив из чисел из файла (можно объединить с первой строкой в однострочник)
evens = list(filter(lambda x: x % 2 == 0, arr))  # Создаем массив из четных чисел
mid = sum(evens) / len(evens)  # Среднее арифметическое
# mid = round(mid)  # Округляем ср. арифмет.  # Не нужно:(
count = 0  # Счетчик
maxx = -1000000  # Для поиска максимума

for i in range(len(arr) - 1):
    a = arr[i]
    b = arr[i+1]
    if ((a % 3 == 0) or (b % 3 == 0)) and ((a < mid) or (b < mid)):
        count += 1
        if (a + b) > maxx:
            maxx = a + b

print(count, maxx)
