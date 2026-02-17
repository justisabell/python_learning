# ex 1

# food = ["mashroom", "cheese", "aubergine", "tomato", "chocolate"]

# def foodlist(fridge):
#     return fridge[-1]

# print(foodlist(food))

# ex 2

# numbers = [5,4,7,2,3,18]
# numbers.append(17)
# print(numbers)
# print(len(numbers))
# numbers.append(5)
# print(numbers.count(5))
# numbers.sort()
# print(numbers)

# ex 3
# def howmanyelements():
#     print(len(countries))

# countries = ["Denmark", "Sweden", "Italy", "Latvia", "Canada"]

# howmanyelements()
# countries.append("Chile")
# howmanyelements()
# countries.append(countries[2])
# print(countries.count("Italy"))

# print(countries.sort())

# ex 4

# newnumbers = [7, 7, 3, 2, 1, 5]
# print(newnumbers)
# newnumbers.remove(7) # if you know the name of the element -> deleting the first element
# print(newnumbers)

# removed_element = newnumbers.pop(-1) # if you know the index of the list
# print(removed_element)

# ex 5

# subjects = ["math", "biology", "PE", "english", "chemistry", "geography"]

# print(subjects[3])
# subjects.remove("english")
# print(subjects)

# four = subjects.pop(3)
# print(four)
# print(subjects[3])

# ex 6

# names = ["Nicolas", "Ekko", "Joanna", "Harry", "Freddy", "Silvana"]
# print(names[:5])
# print(names[2:5])
# print(names[4:])
# print(names[::2]) # goes through the whole list every second step

# ex 7

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number_list[-1])
print(number_list[:5])
print(number_list[5:])
print(number_list[::2])
print(number_list[1::2])
