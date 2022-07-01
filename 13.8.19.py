price= 0
while True:
    try:
        ticket=int(input('Сколько билетов вы хотите приобрести? '))
        if type(ticket) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(ticket):
    i += 1
    while True:
        try:
            age = int(input(f'Для какого возраста билет №{i}? '))
            if 0 < age < 18:
                print('Билет бесплатный')
            elif 18 <= age < 25:
                price += 990
                print('Стоимость билета: 990 руб.')
            elif 25 <= age < 99:
                price += 1390
                print('Стоимость билета: 1390 руб.')
            else:
                print('Возможно Вы ошиблись с возрастом')
                continue
            if type(age) == int:
                break
        except ValueError:
            print('Введите целое число')
if ticket > 3:
    price = price - (price*10 / 100)
    print(f'Сумма к оплате {price} руб. с учетом 10%-ой скидки за регистрацию больше 3 человек')
else:
    print(f'Сумма к оплате {price} руб.')