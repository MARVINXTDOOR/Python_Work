try:
    x = input("Type a number: ")
    x = int(x)

    y = input("Type another number: ")
    y = int(y)
except ValueError:
    print("Sorry, I really needed a number.")
else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")