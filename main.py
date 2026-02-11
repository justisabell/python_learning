# pi = 3
# pie = "pie"
# sentence1 = "i love to eat "
# print(sentence1 + pie)
# sentence2 =  "The value of pi is "
# string_pi = str(pi)
# print(sentence2 + string_pi)


# number = 5+5
# number2= 7**3
# number3 = 3/5
# print(number, number2, pow(7,3))

# print(8**2+3/3%6)

# print(number2 - number3 * number)

item1 = "tomato"
item2 = "ham"
item3 = "lettuce"

item1_count = 10
item2_count = 5
item3_count = 3

item1_price = 1.75
item2_price = 5
item3_price = 3

print("Our grocery store has " + item1 + ", " + item2 + ", " +item3)
print("The price of a ham is " + str(item2_price))

sales_tax = 0.0725
customer_total = 0
customer_items = ""

customer_items += item1
customer_total += 4* item1_price
item1_count -= 4

customer_items +=", " + item2
customer_total += 2 * item2_price
item2_count -= 2

customer_items +=", " + item3
customer_total += item3_price
item3_count -= 1

customer_total += customer_total*sales_tax

print("You bought: " + customer_items + "\nYour total is: " + str(customer_total))

print(item1 + ": " + str(item1_count))
print(item2 + ": " + str(item2_count))
print(item3 + ": " + str(item3_count))