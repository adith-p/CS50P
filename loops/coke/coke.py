
coin = [25, 10, 5]
amt = 50
change = 0

while amt != 0:
    insert_coin = int(input("Insert Coin: "))
    if insert_coin in coin:
        amt -= insert_coin
        change += insert_coin

        if amt <= 0:
            print(f"Change Owed: {change-50}")
            break
    print(f"Amount Due: {amt}")
