import math

# start_interval = 0
# end_interval = 1
# x = start_interval
# dictionary_of_solution = {}
# epsilon = 0.2
# count_of_step = (end_interval - start_interval) // epsilon


# def function_of_x(x):
#     return x**3 - math.sin(x)

# for i in range(0, int(count_of_step) + 1):
#     function_of_x(x)
#     x += epsilon
#     dictionary_of_solution.fromkeys(x[function_of_x(x)])


# while x <= end_interval:
#     function_of_x(x)
#     if x < end_interval:
#         x += epsilon
#     list_of_solution.append(function_of_x(x))







start_interval = 0
end_interval = 1
x = start_interval
dictionary_of_solution = {}
epsilon = 0.2
count_of_step = (end_interval - start_interval) / epsilon


def function_of_x(x):
    return x**3 - math.sin(x)

for i in range(int(count_of_step + 1)):
    dictionary_of_solution[x] = function_of_x(x)
    x += epsilon

print(dictionary_of_solution)

list_of_func = []

for values in dictionary_of_solution:
    list_of_func.append(dictionary_of_solution[values])

print(min(list_of_func))


# print(f' минимальное значение функция f({dictionary_of_solution[]})min(list_of_func)')

# надо писать функцию поиска ключа по значению. Да и вообще все это в функции запихнуть.