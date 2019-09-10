def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that is enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly : ")
cheese_and_crackers(12, 256)

print("Or we can use variables from our script : ")
amount_of_cheese = 20
amount_of_crackers = 30

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside : ")
cheese_and_crackers(10 + 15 , 45 - 25 )

print("And we can combine the two variables and math :")
cheese_and_crackers(amount_of_cheese + 12 , amount_of_crackers - 10)

print("We can also get data from the user : ")
am_of_cheese = int(input("> Enter the amount of cheese : "))
am_of_crackers = int(input("> Enter the amount of boxes of crackers : "))
cheese_and_crackers(am_of_cheese , am_of_crackers)