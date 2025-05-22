while True:
    try:
        number = int(input("Enter a number: "))
        print(f"The square of your number is {number ** 2}.")
        print(f"The cube of your number is {number ** 3}.")
        break
    except ValueError:
        print("Oops! That wasn't a number.")
