def salary():
    try:
        work_time = float(input('Выработка часов: '))
        rate = float(input('Ставка з/п: '))
        bonus = float(input('Премия: '))
        result = work_time * rate + bonus
        print(f'Заработная плата сотрудника:  {result}')
    except ValueError:
        return print('Введено не число!')


salary()
#
