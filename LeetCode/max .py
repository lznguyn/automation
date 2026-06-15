product = [
    {"name": "iPhone", "price": 999},
    {"name": "iPad", "price": 799},
    {"name": "MacBook", "price": 1299},
]



def find_max_price(products):
    max_price = float('-inf')
    for product in products:
        if product['price'] > max_price:
            max_price = product['price']
    return f"name: {product['name']}, max_price: {max_price}"



print(find_max_price(product))