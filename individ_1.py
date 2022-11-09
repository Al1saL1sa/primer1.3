from helpindivid import fun1


print("Введите a: ")
a = int(input())
print("Введите b: ")
b = int(input())
print("Введите 0, если фигура треугольник, 1, если фигура прямоугольник: ")
t = int(input())
n = fun1(a, t)
print(n(b))