value_1 =input("выберите фильм:\n")
value_2 =input("выберите дату (сегодня, завтра):\n")
value_3 =int(input("выберите время:\n"))
value_4 =int(input("выберите количество билетов:\n"))
if value_1 and value_2 and value_3 and value_4:
    film = value_1
    date = value_2
    time = value_3
    count_of_tickets = value_4
    if film == 'паразиты':
        if date == 'сегодня' or date == 'завтра':
            if time == 12:
                print('стоимость:\n',250*count_of_tickets)
            elif time == 16:
                print('стоимость:\n',350*count_of_tickets)
            elif time == 20:
                print('стоимость:\n',450*count_of_tickets)
            else:
                print('сеанса на такое время нет')
        else:
            print('неправильная дата')
    elif film == '1917':
        if date == 'сегодня' or date == 'завтра':
            if time == 10:
                print('стоимость:\n',250*count_of_tickets)
            elif time == 13:
                print('стоимость:\n',350*count_of_tickets)
            elif time == 16:
                print('стоимость:\n',350*count_of_tickets)
            else:
                print('сеанса на такое время нет')
        else:
            print('неправильная дата')
    elif film == 'соник в кино':
        if date == 'сегодня' or date == 'завтра':
            if time == 10:
                print('стоимость:\n',350*count_of_tickets)
            elif time == 14:
                print('стоимость:\n',450*count_of_tickets)
            elif time == 18:
                print('стоимость:\n',450*count_of_tickets)
            else:
                print('сеанса на такое время нет')
        else:
            print('сеанса на такое время нет')
    else:
        print('такого фильма нет')
else:
    print('неверный формат входных данных')
    
    
