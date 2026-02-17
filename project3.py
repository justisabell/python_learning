catalogue = "Pride9and9Prejudice;;To9Kill9a9Mockingbird;;tHe9GrEAt9gATsBy;;One9Hundred9Years9of9Solitude;;In9Cold9Blood;;Wide9Sargasso9Sea;;Brave9New9World;;I9Capture9the9Castle;;Jane9Eyre;;Crime9and9Punishment;;The9Secret9History;;The9Call9Of9The9Wild"

catalogue = catalogue.replace("9", " ")
catalogue = catalogue.split(";;")

print(catalogue)

error = catalogue[2].title()
print(error)

print(f"{error} was fixed")

last_book = ["The", "Invisible", "Man"]
add = " "
last_book = add.join(last_book)

print(last_book)

catalogue.append(last_book)
print(catalogue)
print(catalogue[-1][::2])