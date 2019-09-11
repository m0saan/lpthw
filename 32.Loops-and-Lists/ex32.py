the_count = [1, 2, 3, 4, 5]
friuts = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#The first kind of for loops goes throught a list
for number in the_count:
    print(f"This is count {number}")

#same as above 
for friut in friuts:
    print(f"friut is of type {friut}")

#Also we can go throught mixed lists too
#Notice we have to use {} since we don't know what's in it 
for i in change:
    print(f"I got {i}")

#We can also build lsits, first start with an empty one

element = []

#Then use the range function to do the range 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is function that lists understand 
    element.append(i)

#Now we can print element too 
for i in element:
    print(f"Element was: {i}")