def print_list():
    i = 0
    numbers = []
    while i < usernum:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + userincrement
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

usernum = int(input("What number do you want the list to go too? "))
userincrement = int(input("How much do you want each number to increment by? "))
print_list()
