# Python3 код для демонстрации
# считать слова в строке
# используя split ()


# инициализирующая строка

test_string = "Geeksforgeeks is best Computer Science Portal"

# печать оригинальной строки

print("The original string is : " + test_string)

# используя split ()
# считать слова в строке

res = len(test_string.split())

# результат печати

print("The number of words in string are : " + str(res))
