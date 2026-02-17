# name = "Samantha"
# visual = ['S', 'a', 'm', 'a', 'n', 't', 'h', 'a']
# print(visual[0])
# print(name[0])

# ex1

# sentence = "I like birds."
# print(sentence[-1])
# print(sentence[0])

# print(sentence[0], sentence[2:6], sentence[7:12])
# print(sentence[:12])

# encrypted_message = "Ifdlasoasvqwesupjhysdtvfhsmoasn"
# print(encrypted_message[::3])

# ex2

# username = input("Enter a word: ")
# print(username.lower())
# print(username.upper())
# print(username.title())

# ex3
# sentence = "I love to drive for days and days"
# sentence_list = sentence.split("d")
# print(sentence_list)

# sentence_number = ["123", "456", "7890"]
# connect = "-"
# connect = connect.join(sentence_number)
# print(connect)

# ex4
# news = ["ApPLeS aND BAnanAs", "romeo/and/juliet"] 
# print(news[0].upper())
# print(news[0].lower())

# book = news[1]
# book = book.split("/")

# novel = " "
# novel = novel.join(book)
# print(novel.title())

# ex5
# greet = "My name is Izabela"
# greet = greet.replace("Izabela", "Robert")
# print(greet)
# print(greet.find("Robert"))

# name = "Izabela"
# age = 17

# print(f"Hello my name is {name} and I am {age} years old.")

# ex6

string = "Lewis Carroll: Adam in Wonderland"
error = string.find("Adam")

print(f"The error is on index {error}")

string = string.replace("Adam", "Alice")
print(f"We fixed the string: {string}")
