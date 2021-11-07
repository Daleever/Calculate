from AdvancedCalc import *

print("Вы запустили супер калькулятор")

str = input("выюерите калькулятор 'Обычный'(1) 'Инженерный'(2): ")

while (str.upper() == "ОБЫЧНЫЙ" or str == '1'):
    calc = OrdinaryCalc()

    ClearCounter = 0

    calc.set_num1(float(input("Введите первое число: ")))
    calc.set_num2(float(input("Введите второе число: ")))

    dicta = {"1": calc.Add, "2": calc.Sub}

    print("Выберите операцию")
    print("1.Add  2.Minus 3.Multi \n4.Devided 5.Change first 6.Change second \n7.Exit")
    operation = input()
    if (operation == 1):
        print(calc.Add())
    print(dicta[operation]())






















































while (str.upper() == "ИНЖЕНЕРНЫЙ" or str == "2"):

    calc_engi = AdvancedCalc()

    calc_engi.set_num1(15)
    calc_engi.set_num2(12)

    print("Выберите операцию : ")

print("Вы вышли из калькулятора.")

print("Вы запустили супер калькулятор")

str = input("Выберите калькулятор 'Обычный'(1) или 'Инженерный'(2): ")
