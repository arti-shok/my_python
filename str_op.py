s = 'У лукоморья 123 дуб зеленый 456'
if 'я' in s:
    print(s.find('я'))
print(s.count('у'))
if s.isupper() == False:
    print(s.upper())
if len(s) > 4:
    print(s.lower())
print(s.replace('У','О'))

