from enum import Enum
import random

# Dificultad del juego
class DifficultyLevel(Enum):
    EASY = 10
    MEDIUM = 7
    HARD = 5

# Logica del juego
class GameLogic:
    def __init__(self, difficulty: DifficultyLevel) -> None:        
        self.target_number = random.randint(1, 100)
        self.max_attemps = difficulty.value
        self.attemps_made = 0
        self.is_game_over = False

    def make_guess(self, guess: int) -> str:
        if self.is_game_over:
            return "The game is over"

        self.attemps_made += 1

        # Si se adivina el numero
        if guess == self.target_number:
            self.is_game_over = True
            return f"Congratulations! You guessed the number in {self.attemps_made} attempts."

        # Si se supera el maximo de intentos
        elif self.attemps_made >= self.max_attemps:
            self.is_game_over = True
            return f"Maximum number of attempts reached. The target number was {self.target_number}."

        # Si el numero es menor al objetivo
        elif guess < self.target_number:
            return "Too low! Try again."

        # Si el numero es mayor al objetivo
        else:
            return "Too high! Try again."

    def play_again(self) -> bool:
        while True:
            try:
                choice = input("\nDo you want to play again? (y/n): ").strip().lower()
                if choice == 'y':
                    return True
                elif choice == 'n':
                    return False
                else:
                    raise ValueError("Invalid choice. Please enter 'y' or 'n'.")
            except ValueError as e:
                print(e)


class UserUI:
    def __init__(self):
        self.game =  None

    def start_game(self):
        print("\nWelcome to the Number Guessing Game!")
        print("Rules: Guess the number between 1 and 100. You have a limited number of attempts based on the difficulty level you choose.")

        difficulty = self.select_difficulty()
        self.game = GameLogic(difficulty)

        while not self.game.is_game_over:
            try:
                guess = int(input(f"\nAttemp {self.game.attemps_made + 1}/{self.game.max_attemps}: Enter your guess: "))
                result = self.game.make_guess(guess)
                print(result)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if self.game.play_again():
            self.start_game()
        else:
            print("\nThanks for playing! Goodbye.")

    def select_difficulty(self) -> DifficultyLevel:
        while True:
            try:
                print("\nSelect difficulty level: [e] Easy, [m] Medium, [h] Hard")
                choice = input("Enter your choice: ").strip().lower()
                if choice == 'e':
                    return DifficultyLevel.EASY
                elif choice == 'm':
                    return DifficultyLevel.MEDIUM
                elif choice == 'h':
                    return DifficultyLevel.HARD
                else:
                    raise ValueError("Invalid choice. Please select a valid difficulty level.")
            except ValueError as e:
                print(e)


if __name__ == "__main__":
    ui = UserUI()
    ui.start_game()

