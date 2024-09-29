menu_items = [
    'D1 SODA 3', 'D2 LEMONADE 3', 'D3 TEA 2', 'D4 WATER 1',
    'A1 POTATO_CAKES 7', 'A2 SPINACH_DIP 5', 'A3 OYSTERS 13', 
    'A4 CHEESE_FRIES 4', 'A5 ONION_RINGS 7',
    'S1 COBB 14', 'S2 CAESAR 13', 'S3 GREEK 12',
    'E1 BURGER 16', 'E2 PASTA 15', 'E3 GNOCCHI 14', 
    'E4 GRILLED_STEAK_SANDWICH 17',
    'T1 CARAMEL_CHEESECAKE 13', 'T2 APPLE_COBBLER 12', 'T3 BROWNIE_SUNDAE 9', 'T4 FLAN 8'
]

drink_items = ['D1', 'D2',  'D3', 'D4']

# Convert the list of menu items to a list of dictionaries with random stock
import random

menu_dict = []
for item in menu_items:
    code, name, price = item.split(maxsplit=2)
    price = int(price)
    if code in drink_items:
        stock = random.randint(3000,10000)  # Random stock for drink items
    else:
        stock = random.randint(25, 50)  # Random stock for non-drink items
    menu_dict.append({"code": code, "name": name, "price": price, "stock": stock})

