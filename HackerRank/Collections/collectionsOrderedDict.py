from collections import OrderedDict

def ex1():
    ordered_dictionary = OrderedDict()
    ordered_dictionary['a'] = 1
    ordered_dictionary['a'] += +1
    ordered_dictionary['a'] += 3
    ordered_dictionary['b'] = 3
    print(ordered_dictionary)


n = int(input())
shop = []
item_name = []
net_price = []
products = OrderedDict()

for i in range(n):
    shop.append(input())

for i in range(len(shop)):  # dict of words
    words = shop[i].split()
    key_join = ' '.join(words[:-1])
    value = int(words[-1])
    products[key_join] = 0

for k in range(len(shop)):  # put values to key
    words = shop[k].split()
    key_join = ' '.join(words[:-1])
    value = int(words[-1])
    products[key_join] += value

item_name = list(products.keys())
item_price = list(products.values())

for u in range(len(item_name)):
    print(str(item_name[u]) + ' ' + str(item_price[u]))
