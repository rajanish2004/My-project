import random

def main():
    print("Welcome to the Little Professor Game!")

    # Prompt user for level
    level = get_level()

    # Generate 10 math problems
    problems = generate_problems(level)

    # Play the game
    score = play_game(problems)

    # Output final score
    print(f"Your score: {score}/10")

def get_level():
    while True:
        try:
            level = int(input("Enter a level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid integer (1, 2, or 3).")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

def generate_problems(level):
    problems = []
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problem = (x, y, x + y)
        problems.append(problem)
    return problems

def play_game(problems):
    score = 0
    for x, y, expected_answer in problems:
        tries = 0
        while tries < 3:
            try:
                user_answer = int(input(f"What is {x} + {y} = "))
                if user_answer == expected_answer:
                    print("Correct!")
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"Sorry, the correct answer was {expected_answer}")

    return score

if __name__ == "__main__":
    main()
