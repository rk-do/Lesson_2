print("Задание 1".upper())

objects = [2, "text", 123, 10.3, None]
print(type(objects[4]))

print("Задание 2".upper())
a = []#
n = int(input())
for i in range(n):
    new_element = int(input())
    a.append(new_element)
print(a)
a[0] = 2
a[1] = 1
a[2] = 4
a[3] = 3
print(a)

print("Задание 3".upper())
months = int(input("Введите номер месяца года: "))
seasons = ["winter", "spring", "summer", "autumn"]
while months == 1 or months == 2 or months == 12:
    print(seasons[0])
    break
while months == 3 or months == 4 or months == 5:
    print(seasons[1])
    break
while months == 6 or months == 7 or months == 8:
    print(seasons[2])
    break
while months == 9 or months == 10 or months == 11:
    print(seasons[3])
    break

print("Задание 4".upper())
my_str = input("введите строку из нескольких слов, разделенных пробелом: ")
my_word = []
num = 1
for i in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(str(num) + str(my_word))
        num += 1
    else:
        print(str(num) + str(my_word[0:10]))
        num += 1

print("Задание 5".upper())
a = []
n = int(input())
for i in range(n):
    new_element = int(input())
    a.append(new_element)
print(a)

print("Задание 6".upper())
goods = []
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
num = 0
feature_ = None
control = None
while True:
    control = input("For quit press 'Q', for continue press 'Enter', for analytics press 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Input feature "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))

'''
goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
print(my_list)
print(my_analys)

'''
goods = []
goods_1 = ("nomber_of_goods_1", {"characteristics_1": "name", "price_1": "price", "quantity": "things"})
goods_2 = ("nomber_of_goods_2", {"characteristics_2": "name_2", "price": "price", "quantity": "things"})
goods_3 = ("nomber_of_goods_3", {"characteristics_3": "name_3", "price": "price", "quantity": "things"})
user = input("Что Вас интересует?: ")
if user in goods_1:
    if goods_1[0] == user:
        print("Вы выбрали информацию о номере товара")
    else:
        if goods_1["characteristics_1"] == user:
            print("Другое: ")

'''
















