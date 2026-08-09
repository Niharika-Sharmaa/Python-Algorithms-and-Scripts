import random

print("=" * 50)
print("          🎯 GUESS THE NUMBER 🎯")
print("=" * 50)

best_score = None

while True:
    print("\nChoose Difficulty:")
    print("1. Easy   → Number between 1 and 50 | 10 attempts")
    print("2. Medium → Number between 1 and 100 | 7 attempts")
    print("3. Hard   → Number between 1 and 200 | 6 attempts")

    while True:
        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == "1":
            maximum = 50
            max_attempts = 10
            difficulty = "Easy"
            break
        elif choice == "2":
            maximum = 100
            max_attempts = 7
            difficulty = "Medium"
            break
        elif choice == "3":
            maximum = 200
            max_attempts = 6
            difficulty = "Hard"
            break
        else:
            print("❌ Invalid choice! Please select 1, 2, or 3.")

    number = random.randint(1, maximum)
    attempts = 0

    print(f"\n🎮 {difficulty} Mode Selected!")
    print(f"I'm thinking of a number between 1 and {maximum}.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:

        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}: "))

            if guess < 1 or guess > maximum:
                print(f"⚠️ Please enter a number between 1 and {maximum}.")
                continue

            attempts += 1

            if guess == number:
                score = (max_attempts - attempts + 1) * 100

                print("\n" + "=" * 50)
                print("🎉 CONGRATULATIONS! 🎉")
                print("=" * 50)
                print(f"You guessed the number: {number}")
                print(f"Attempts used: {attempts}")
                print(f"🏆 Your score: {score}")

                if best_score is None or score > best_score:
                    best_score = score
                    print("🌟 NEW BEST SCORE!")

                break

            elif guess < number:
                print("📈 Too low! Try a higher number.")

            else:
                print("📉 Too high! Try a lower number.")

            # Give a hint after 3 incorrect attempts
            if attempts == 3:
                if number % 2 == 0:
                    print("💡 Hint: The number is EVEN.")
                else:
                    print("💡 Hint: The number is ODD.")

        except ValueError:
            print("❌ Invalid input! Please enter a whole number.")

    else:
        print("\n" + "=" * 50)
        print("😢 GAME OVER!")
        print("=" * 50)
        print(f"The correct number was: {number}")

    if best_score is not None:
        print(f"\n🏆 Best Score: {best_score}")

    play_again = input("\nWould you like to play again? (y/n): ").lower()

    if play_again != "y":
        print("\nThanks for playing! 👋")
        print("See you next time! 🎯")
        break