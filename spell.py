import random

def load_words():
    return ["python", "developer", "programming", "challenge", "computer", "keyboard", "monitor", "software", "hardware", "algorithm"]

def spelling_game():
    words = load_words()
    score = 0
    total_rounds = 5
    
    print("Welcome to the Spelling Game!\n")
    
    for _ in range(total_rounds):
        word = random.choice(words)
        print(f"Spell this word: {word}")
        user_input = input("Your answer: ").strip().lower()
        
        if user_input == word:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct spelling is: {word}\n")
    
    print(f"Game Over! Your final score: {score}/{total_rounds}")

if __name__ == "__main__":
    spelling_game()
