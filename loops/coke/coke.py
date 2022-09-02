def main():
    coke_price = 50
    remaining_coke = 2
    remaining_amount = 0
    while remaining_coke > 0:
        inserted_coin = insert_coin(input('Insert Coin: '))
        remaining_amount += inserted_coin
        if remaining_amount >= coke_price:
            remaining_coke -= 1
            remaining_amount = remaining_amount - coke_price
            print('Change owed: ', remaining_amount)
        print('Amount Due: ', coke_price - remaining_amount)
    print('There is not enough Coke to serve you. Here is your changed owned: ', remaining_amount)


def insert_coin(amount):
    amount = int(amount) 
    assert amount == 5 or amount == 10 or amount == 25
    return amount


main()