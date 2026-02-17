pizza = ["Pepperoni", "Combination", "Cheese", "Margherita","Hawaiian", "Sausage"]
prices = [5, 8, 4, 5, 6, 7]

pizzaprices = list(zip(prices, pizza))
pizzaprices.sort()

print(pizzaprices)
print(pizzaprices[-1])
print(pizzaprices[:3])
print(pizzaprices[::2])

pizzaprices.pop(0)
print(pizzaprices)