# Задача 1

str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
str2 = ""

for i in range(len(str1)):
    if i % 2 == 0 and str1[i] == 'N':
        change = str1[i].replace('N', 'P')
        str2 += change
    else:
        str2 += str1[i]
print(str1)
print(str2)

# ================================================================================

# Задача 2

# s = "0123456789"
# n = int(input("Введите номер позиции который хотите удалить: "))
# s2 = s[:n] + s[n+1:]
# print(s2)


# ================================================================================

# Задача 3

# s = "012345363738494"
# print(s)
# sim = input("Введите символ который хотите удалить из строки: ")
#
# s2 = s.replace(sim, "")
#
# print("s2 =", s2)

# ================================================================================

# Задача 4

# def change_ten_two(n):
#     b = ''
#
#     while n > 0:
#         b = str(n % 2) + b
#         n = n // 2
#     return b
#
#
# x = int(input("Введите десятичное целое число: "))
#
# print(change_ten_two(x))