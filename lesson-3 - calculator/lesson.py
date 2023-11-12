def addition(a :int, b :int) -> int:
    sum = a + b
    return sum

def subtraction(a :int, b :int) -> int:
    sum = a - b
    return sum

def multiplication(a: int, b:int) -> int:
    sum = a * b
    return sum

def division(a :int, b:int) -> int:
    sum = a / b
    return sum

def division_remainder(a :int, b :int) -> float:
    sum = a % b
    return sum


while True:
    print()
    print('Вас приветсвует калкулятор на python для завершение программы нажмите пожалуйста сочетания клавиш (ctrl+c)')
    
    a_input = input('Укажите первое число: ')
    b_input = input('Укажите второе число: ')

    if not a_input.isdigit() and not a_input.replace('.', '', 1).isdigit():
        print('Ошибка: первое значение не является числом, укажите пожалуйста число')
        continue

    if not b_input.isdigit() and not b_input.replace('.', '', 1).isdigit():
        print('Ошибка: второе значение не является числом, укажите пожалуйста число')
        continue

    a = float(a_input)
    b = float(b_input)


    print('Пожалайста выберите одну из предложенных операций (+,-,*,/,%) для выполнение расчётов')
    operation = input('Укажите операцию: ')

    if (operation == '+'):
        print(f'Ответ (операции сложения): {addition(a, b)}') 
    elif (operation == '-'):
        print(f'Ответ (операции вычитания): {subtraction(a, b)}') 
    elif (operation == '*'):
        print(f'Ответ (операции умножения): {multiplication(a, b)}') 
    elif (operation == '/'):
        if (b == 0) :
            print('Извините но на ноль делить нельзя')
        else :
            print(f'Ответ (операции деления): {division(a, b)}') 
    elif (operation == '%'):
        print(f'Ответ (операции деления с остатком): {division_remainder(a, b)}') 
    else:
        print('Данной операции не сущетвует выберите пожалуйста одну из данных операций (+,-,*,/) ')