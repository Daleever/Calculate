from AdvancedCalc import *
import os
print("Вы запустили супер калькулятор")

str = input("выюерите калькулятор 'Обычный'(1) 'Инженерный'(2): ")
ClearCounter = 0
while (str.upper() == "ОБЫЧНЫЙ" or str == '1'):
    calc = OrdinaryCalc()
    if(ClearCounter % 3 == 0):
        tmp = input("Вы хочете очистить историю?(Yes/No)")
        if(tmp.upper() == "YES"):
            os.system('CLS')
            
    calc.set_num1(float(input("Введите первое число: ")))
    calc.set_num2(float(input("Введите второе число: ")))

    dicta = {"1": calc.Add, "2": calc.Sub, "3":calc.Mul, "4":calc.Div}

    print("Выберите операцию")
    print("1.Add  2.Minus 3.Multi \n4.Devided 5.Change first 6.Change second \n7.Exit")
    operation = input()
    if(operation in dicta):
        print(dicta[operation]())
        ClearCounter+=1
    elif(operation == '5'):
        print("Введите число:")
        calc.set_num1(float(input()))
        
    elif(operation == '6'):
        print("Введите число")
        calc.set_num2(float(input()))
        
    elif(operation =='7'):
        print("Удачной работы")
        break
    else:
        print("Вы ввели неверное значение операции, повторите попытку")
        continue

while (str.upper() == "ИНЖЕНЕРНЫЙ" or str == "2"):

    calc_engi = AdvancedCalc()

    if (ClearCounter % 3 == 0):
        tmp = input("Вы хочете очистить историю?(Yes/No)")
        if (tmp.upper() == "YES"):
            os.system('CLS')

    calc_engi.set_num1(float(input("Введите первое число :")))
    calc_engi.set_num2(float(input("Введите второе число :")))

    dicta = {"1": calc_engi.Add, "2": calc_engi.Sub, "3":calc_engi.Mul, "4":calc_engi.Div, "5": calc_engi.TransformToKBite}

    print("Выберите операцию : ")
    print("1.Add  2.Minus 3.Multi \n4.Devided 5.Transfer to KBytes 6.Change first, 7.Change second \n 8.Exit")
    operation = input()

    if (operation in dicta):
        print(dicta[operation]())
        ClearCounter += 1
    elif (operation == '6'):
        print("Введите число:")
        calc.set_num1(float(input()))

    elif (operation == '7'):
        print("Введите число")
        calc.set_num2(float(input()))

    elif (operation == '8'):
        print("Удачной работы")
        break
    else:
        print("Вы ввели неверное значение операции, повторите попытку")
        continue
