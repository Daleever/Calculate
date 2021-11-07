from AdvancedCalc import *

print("Вы запустили супер калькулятор")

str = input("Выберите калькулятор 'Обычный'(1) или 'Инженерный'(2): ")

while(str.upper()=="ОБЫЧНЫЙ" or str == '1'):
    calc = OrdinaryCalc()
    
    ClearCounter = 0
    
    calc.set_num1 (float(input("Введите первое число: ")))
    calc.set_num2 (float(input("Введите второе число: ")))
    
    dicta = {"1":calc.Add,"2":calc.Sub}
        
    print("Выберите операцию")
    print("1.Add  2.Minus 3.Multi \n4.Devided 5.Change first 6.Change second \n7.Exit")
    
    if(operation == 1):
        print(calc.Add())
    print(dicta[operation]())
    
    

