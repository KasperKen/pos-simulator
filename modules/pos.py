shopping_cart = [
    {"name": "Apple", "price": 1, "quantity": 6},
    {"name": "Pie", "price": 8, "quantity": 1.00},
    {"name": "Magazine", "price": 2, "quantity": 1},]

def display_cart(cart):

    for item in cart:
        print(f"{item['name']}: ${item['price']}ea - Count: {item['quantity']} - Cost: ${item['price'] * item['quantity']}")
    print("\n                  Total: $" + str(add_total(cart)) + '\n')


def add_to_cart(item, price, quantity):
    unit_price = {":.2f"}.format(price) #--Fix ME -- <---------------------------------------------------#
    shopping_cart.append({"name": item, "price": unit_price, "quantity": quantity})


def remove_from_cart(item, quantity):
    for i in range(len(shopping_cart)):
        if shopping_cart[i]["name"] == item:
            shopping_cart[i]["quantity"] -= quantity
            if shopping_cart[i]["quantity"] <= 0:
                shopping_cart.pop(i)
                break


def add_total(cart):
    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]
    return total


credit_cards = [
    {"name": "Visa", "balance": 10},
    {"name": "Master Card", "balance": 0},
    {"name": "Discover Card", "balance": 100},
]


def select_credit_card():
    print('\nPlease Select a Payment Method:')
    for i, card in enumerate(credit_cards):
        print(f"{i}. {card['name']} - ${card['balance']}")
    credit_card_selection = int(input('Select a Credit Card: '))
    return credit_cards[credit_card_selection]


def process_payment(remaining_total):
    print('----------------------------------------------------')
    credit_card = select_credit_card()
    print('...processing Payment with ' + credit_card['name'] + '.\n')
    print('Previous Total Due: $' + str(remaining_total))
    payment_amount = 0
    if credit_card['balance'] > remaining_total:
        payment_amount = remaining_total
    else:
        payment_amount = credit_card['balance']
    credit_card['balance'] -= payment_amount
    remaining_total -= payment_amount
    print('payment amount: $' + str(payment_amount))
    print('\n             Total Due: $' + str(remaining_total))
    print('----------------------------------------------------')
    print('\nYour Remaining ' + credit_card['name'] + ' Balance is $' + str(credit_card['balance']) + '.\n')
    return remaining_total


def checkout(cart):
    remaining_total = add_total(cart)
    while remaining_total > 0:
        remaining_total = process_payment(remaining_total)
    print('----------------------------------------------------')
    print('Transaction Successful! Thank you for shopping with us!\n\n\n')
