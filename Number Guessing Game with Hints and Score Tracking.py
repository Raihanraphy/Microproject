import random

def get_hint(secret, guess):
    if abs(secret - guess) <= 3:
        return "🔥 Very close!"
    elif guess < secret:
        return "🔼 Too low!"
    else:
        return "🔽 Too high!"

def play_game():
    secret = random.randint(1, 50)
    attempts = 0
    print("🎯 Guess the number (between 1 and 50):")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess == secret:
                print(f"✅ Correct! You guessed it in {attempts} tries.")
                break
            else:
                print(get_hint(secret, guess))
        except ValueError:
            print("⚠️ Enter a valid number.")

def main():
    high_score = None
    while True:
        play_game()
        if high_score is None or high_score > attempts:
            high_score = attempts
            print(f"🏆 New high score: {high_score}")
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()
