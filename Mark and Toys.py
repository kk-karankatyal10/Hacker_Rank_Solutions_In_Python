def maximumToys(prices, k):
    suma = 0
    cout = 0
    prices = sorted(prices)
    for i in range(len(prices)):
        if suma+prices[i] <= k:
            suma += prices[i]
            cout += 1
        else:
            break
    return cout
