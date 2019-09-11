def while_iter(end , iter):
    i = 0
    numbers = []

    while i < end:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + iter
    print("Numbers now ", numbers)
    print(f"At the buttom i is {i}")

    print("The numbers : ")
    for num in numbers:
        print(num)

while_iter(6 , 2)