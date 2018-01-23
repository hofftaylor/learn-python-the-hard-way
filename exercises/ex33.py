#Exercise 33 - While Loops

def incrementor():
    i = 0
    e = 10
    o = 0.5
    numbers = []

    while i < e:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + o
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

#incrementor()

def incrementor_for_style():
    i = 0
    e = 10
    o = 0.5
    numbers = []

    for i in range(i, e):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

incrementor_for_style()

