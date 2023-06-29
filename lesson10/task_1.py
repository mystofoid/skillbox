# Задача 1. Таблица умножения
# Математик Паша недавно заметил, что у него уже есть куча разных таблиц степеней, но нет самого основного — таблицы умножения. Пора бы это исправить.

# Напишите программу, которая выводит таблицу умножения для чисел от 1 до 9. Для этого используйте конструкцию вложенного цикла: внешний отвечает за первый множитель, а внутренний — за второй.

# Дополнение: выведите настоящую таблицу умножения, без всяких знаков, только числа. Чтобы она получилась красивой и ровной, используйте литерал \t внутри оператора end. \t — это литерал табуляции, благодаря ему все числа выстраиваются в виде таблицы. Результат должен получиться таким:

# 1       2       3       4       5       6       7       8       9
# 2       4       6       8       10      12      14      16      18
# 3       6       9       12      15      18      21      24      27
# 4       8       12      16      20      24      28      32      36
# 5       10      15      20      25      30      35      40      45
# 6       12      18      24      30      36      42      48      54
# 7       14      21      28      35      42      49      56      63
# 8       16      24      32      40      48      56      64      72
# 9       18      27      36      45      54      63      72      81

for row in range(1, 10):
    for col in range(1, 10):
        print(row * col, end='\t')
    print('')