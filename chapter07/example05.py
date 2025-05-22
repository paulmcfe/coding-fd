def greet():
    user_name = input("What's your name? ") # local variable
    print(f"Hi, {user_name}!")  # works just fine

greet()
print(user_name)  # Not gonna happen