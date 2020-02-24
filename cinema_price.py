value_1 =input("выберите фильм:\n")
value_2 =input("выберите дату (сегодня, завтра):\n")
value_3 =int(input("выберите время:\n"))
value_4 =int(input("выберите количество билетов:\n"))
if value_1 and value_2 and value_3 and value_4:
    film = value_1
    date = value_2
    time = value_3
    count_of_tickets = value_4
    print('вы выбрали:\nфильм: {0}, дата: {1},время: {2},количетво билетов: {3}'.format(value_1,value_2,value_3,value_4))
    if film == 'паразиты':
        if date == 'сегодня':
            if count_of_tickets >= 20:
                if time == 12:
                    print('стоимость:\n',0.8*250*count_of_tickets)
                elif time == 16:
                    print('стоимость:\n',0.8*350*count_of_tickets)
                elif time == 20:
                    print('стоимость:\n',0.8*450*count_of_tickets)
                else:
                    print('ошибка: сеанса на такое время нет')
            else:
                if time == 12:
                    print('стоимость:\n',250*count_of_tickets)
                elif time == 16:
                    print('стоимость:\n',350*count_of_tickets)
                elif time == 20:
                    print('стоимость:\n',450*count_of_tickets)
                else:
                    print('ошибка: сеанса на такое время нет')
        elif date == 'завтра':
            if count_of_tickets >= 20:
                if time == 12:
                    print('стоимость:\n',0.75*250*count_of_tickets)
                elif time == 16:
                    print('стоимость:\n',0.75*350*count_of_tickets)
                elif time == 20:
                    print('стоимость:\n',0.75*450*count_of_tickets)
                else:
                    print('ошибка: сеанса на такое время нет')
            else:
                if time == 12:
                    print('стоимость:\n',0.95*250*count_of_tickets)
                elif time == 16:
                    print('стоимость:\n',0.95*350*count_of_tickets)
                elif time == 20:
                    print('стоимость:\n',0.95*450*count_of_tickets)
                else:
                    print('ошибка: сеанса на такое время нет')
        else:
            print('ошибка: неправильная дата')
    elif film == '1917':
        if date == 'сегодня':
            if count_of_tickets >=20:
                if time == 10:
                    print('стоимость:\n',0.8*250*count_of_tickets)
                elif time == 13:
                    print('стоимость:\n',0.8*350*count_of_tickets)
                elif time == 16:
                    print('стоимость:\n',0.8*350*count_of_tickets)
                else:
                    print('ошибка: сеанса на такое время нет')
            else:
                if time == 10:
                    print('стоимость:\n',250*count_of_tickets)
                elif time == 13:
                    print('стоимость:\n',350*count_of_tickets)
                elif time == 16:
                    print('стоимость:\n',350*count_of_tickets)
                else:
                    print('ошибка: сеанса на такое время нет')
        elif date == 'завтра':
            if count_of_tickets >=20:
                if time == 10:
                    print('стоимость:\n',0.75*250*count_of_tickets)
                elif time == 13:
                    print('стоимость:\n',0.75*350*count_of_tickets)
                elif time == 16:
                    print('стоимость:\n',0.75*350*count_of_tickets)
                else:
                    print('ошибка: сеанса на такое время нет')
            else:
                if time == 10:
                    print('стоимость:\n',0.95*250*count_of_tickets)
                elif time == 13:
                    print('стоимость:\n',0.95*350*count_of_tickets)
                elif time == 16:
                    print('стоимость:\n',0.95*350*count_of_tickets)
                else:
                    print('ошибка: сеанса на такое время нет')
        else:
            print('ошибка: неправильная дата')
    elif film == 'соник в кино':
        if date == 'сегодня':
            if count_of_tickets >= 20:
                if time == 10:
                    print('стоимость:\n',0.8*350*count_of_tickets)
                elif time == 14:
                    print('стоимость:\n',0.8*450*count_of_tickets)
                elif time == 18:
                    print('стоимость:\n',0.8*450*count_of_tickets)
                else:
                    print('ошибка: сеанса на такое время нет')
            else:
                 if time == 10:
                    print('стоимость:\n',350*count_of_tickets)
                 elif time == 14:
                    print('стоимость:\n',450*count_of_tickets)
                 elif time == 18:
                    print('стоимость:\n',450*count_of_tickets)
                 else:
                    print('ошибка: сеанса на такое время нет')
        elif date == 'завтра':
            if count_of_tickets >= 20:
                if time == 10:
                    print('стоимость:\n',0.75*350*count_of_tickets)
                elif time == 14:
                    print('стоимость:\n',0.75*450*count_of_tickets)
                elif time == 18:
                    print('стоимость:\n',0.75*450*count_of_tickets)
                else:
                    print('ошибка: сеанса на такое время нет')
            else:
                 if time == 10:
                    print('стоимость:\n',0.95*350*count_of_tickets)
                 elif time == 14:
                    print('стоимость:\n',0.95*450*count_of_tickets)
                 elif time == 18:
                    print('стоимость:\n',0.95*450*count_of_tickets)
                 else:
                    print('ошибка: сеанса на такое время нет')
        else:
            print('ошибка: неправильная дата')
    else:
        print('ошибка: такого фильма нет')
else:
    print('ошибка: неверный формат входных данных')
    
    
