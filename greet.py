def greet_user(name):
    return f"Hello, {name}! Welcome to the GitHub project."

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet_user(name))