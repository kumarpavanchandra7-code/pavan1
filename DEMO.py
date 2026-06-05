# A simple greeting and guessing game
def welcome_user():
    pri
    name = input("What is your name? ")
    print(f"Hello, {name}! Let's play a quick game.")
    
    # Simple conditional logic
    secret_number = 7
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == secret_number:
            print("Spot on! You got it.")
        elif guess < secret_number:
            print("Too low! Maybe next time.")
        else:
            print("Too high! Close one.")
    except ValueError:
        print("Oops! That wasn't a valid number.")

# Run the program
if __name__ == "__main__":
    welcome_user()
