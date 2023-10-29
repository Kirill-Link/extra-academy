import math

def gipotenuza():
	a = int(input('Введите первый катет (a): ' )) 
	b = int(input('Введите второй катет (b): ' )) 

	c = pow(a,2) + pow(b,2)

	print(math.sqrt(c))
	start_program()

def endlesson():
    number_lesson = int(input('Введите № урока: '))

    start_lessons = 9 * 60

    timeline_lesson = 45

    change_lesson = 5 if number_lesson % 2 == 1 else 15

    end_lesson = start_lessons + (number_lesson - 1) * (timeline_lesson + change_lesson)

    hours_lesson = end_lesson // 60
    minutes_lesson = end_lesson % 60

    print(f'Час окончания: {hours_lesson}, Минуты окончания: {minutes_lesson:02}')
    start_program()

def number_is_greater():
	first_numper = int(input('Введите первое число: '))
	two_numper = int(input('Введите второе число: '))

	if first_numper > two_numper:
		print(f'Первое больше второго, большее число: {first_numper}')
	elif first_numper < two_numper:
		print(f'Второе число больше первого, большее число: {two_numper}')
	elif first_numper == two_numper:
		print(f'Первое и второе число равны {first_numper} : {two_numper}')
	start_program()

def maximum__three():
	number1 = int(input('Введите первое число: '))
	number2 = int(input('Введите второе число: '))
	number3 = int(input('Введите третье число: '))

	if number1 >= number2 and number1 >= number3:
		max_number = number1
	elif number2 >= number1 and number2 >= number3:
		max_number = number2
	else:
		max_number = number3

	print(f'Максимальное число: {max_number}')

def coincidence():
	number1 = int(input('Введите первое число: '))
	number2 = int(input('Введите второе число: '))
	number3 = int(input('Введите третье число: '))

	if number1 == number2 == number3:
	    print('Чсло совпадений 3')
	elif number1 == number2 or number1 == number3 or number2 == number3:
	    print('Чсло совпадений 2')
	else:
	    print('Чсло совпадений 0')

def sorting():
	a = int(input('Первое число: '))
	b = int(input('Второе число: '))
	c = int(input('Третье число: '))

	if a > b:
	    a, b = b, a
	if b > c:
	    b, c = c, b
	if a > b:
	    a, b = b, a

	print(a, b, c)

def equation():
	a = float(input('Первое число: '))
	b = float(input('Второе число: '))
	c = float(input('Третье число: '))

	D = b**2 - 4*a*c

	if D > 0:
	    x1 = (-b + D**0.5) / (2*a)
	    x2 = (-b - D**0.5) / (2*a)
	    print(x1, x2)
	elif D == 0:
	    x = -b / (2*a)
	    print(x)
	else:
	    pass 


def start_program():
	while True:
		print('----------------- Старт программы -----------------')
		print('Выберите номер для запуска подпрограммы: ' + '\n'
			  '№ 1 расчитать гипотенузу ' + '\n'
		      '№ 2 Расчитать конец урока ' + '\n'
		      '№ 3 Узнать какое число больше из 2 чисел' + '\n'
		      '№ 4 Узнать какое число больше из 3 чисел" ' + '\n'
		      '№ 5 Узнать сколько из 3 чисел совпадают'  + '\n'
		      '№ 6 Сортировка 3 разных чисел'  + '\n'
		      '№ 7 Квадратное уровнение'  + '\n')
		print('---------------------------------------------------')

		program_number = int(input('Введите номмер программы '))

		if program_number == 1 :
			gipotenuza()
		elif program_number == 2 :
			endlesson()
		elif program_number == 3 :
			number_is_greater()
		elif program_number == 4 :
			maximum__three()
		elif program_number == 5 :
			coincidence()
		elif program_number == 6 :
			sorting()
		elif program_number == 7 :
			equation()
		else :
			print(f'Такой программы как {program_number}, в списке нету !')
		print('-------------------------------------------------')

start_program()