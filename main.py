def example_variables():
    var_int1 = int(input("Введите целое число: "))
    print("Вы ввели число ", var_int1)
    var_str1 = str(input("Как Вас зовут? "))
    print("Привет,", var_str1, "!")
    rezult = var_int1 + 5
    print(rezult)


def time_from_second_to_hhmmss(seconds):
    hours = int(seconds / 3600)
    minutes = int(seconds / 60) - hours * 60
    seconds = seconds - minutes * 60 - hours * 3600
    return f'{hours:02}:{minutes:02}:{seconds:02}'

def sum_n_nn_nnn(number):
    return int(number) * 123

def sum_n_nn_nnn2(number):
    nn = number * 2
    nnn = number * 3
    return int(number) + int(nn) + int(nnn)

def max_number(number):
    n1 = int(number)
    max = 0
    while n1 > 0:
        d = n1 % 10
        if max < d:
            max = d
        n1 = (n1 - d) / 10
    return int(max)

def earning():
    print("Task No.5")
    proceeds = float(input("Введите выручку: "))
    costs = float(input("Введите издержки: "))
    earning = proceeds - costs
    if proceeds > costs:
        print("Фирма работает с прибылью.")
        print("Рентабельность составила: ",earning / costs)
        persons = float(input("Какое количество сотрудников в фирме? "))
        print("Прибыль фирмы на 1 сотрудника составляет: ", earning / persons)
    elif proceeds < costs:
        print("Фирма работает с убытком.")
    else:
        print("Фирма вышла в 0")

def sport(a,b):
    distance = float(a)
    target = float(b)
    days = 0
    while distance < target:
        distance *= 1.2
        days += 1
    return days

if __name__ == '__main__':
    example_variables()
    print(time_from_second_to_hhmmss(int(input("2. Введите секунды: "))))
    print(sum_n_nn_nnn(input("3. Введите число от 1 до 10: ")))
    print(sum_n_nn_nnn2(input("3. Вариант 2. Введите число от 1 до 10: ")))
    print(max_number(input("4. Введите число: ")))
    earning()
    prompt1 = "Введите расстояние. которое пробегает спортсмен в первый день. a = "
    prompt2 = "Введите расстояние, которое должен пробегать спортсмен, b = "
    prompt3 = "Требуемую дистанцию спортсмен будет пробегать через {0} дней с начала занятий"
    print(str.format(prompt3,sport(input(prompt1),input(prompt2))))
