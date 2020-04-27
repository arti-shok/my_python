value_1 = int(input("Код города:\n"))
value_2 = int(input("Длительность переговора:\n"))
if value_1 and value_2:
    city_code = value_1
    call_duration = value_2
    if city_code == 343:
        print("стоимость переговоров:\n",15*call_duration)
    elif city_code == 381:
        print("стоимость переговоров:\n",18*call_duration)
    elif city_code == 473:
        print("стоимость переговоров:\n",13*call_duration)
    elif city_code == 485:
        print("стоимость переговоров:\n",11*call_duration)
    else:
        print("неверный код города")
else:
    print("неверный формат входных данных")
