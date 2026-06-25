import random

class RockPaperScissorsGame:
    def __init__(self):
        # Score variables aur choices ke naam badal diye
        self.player_points = 0
        self.bot_points = 0
        self.valid_moves = ['rock', 'paper', 'scissors']

    def start_game(self):
        print("====== WELCOME TO THE RPS ARENA ======")
        
        while True:
            player_input = input("\nSelect rock, paper, or scissors (Type 'exit' to end): ").lower().strip()
            
            if player_input == 'exit':
                print("\n======================================")
                print("Game Over! Thanks for entering the arena.")
                print(f"Final Leaderboard -> Player: {self.player_points} | Bot: {self.bot_points}")
                print("======================================")
                break
                
            if player_input not in self.valid_moves:
                print("Invalid Move! Please select from rock, paper, or scissors.")
                continue
                
            bot_move = random.choice(self.valid_moves)
            
            print(f"\nYour Move: {player_input.capitalize()}")
            print(f"Bot's Move: {bot_move.capitalize()}")
            
            # Win/Lose check karne ka logic thoda restructure kiya
            if player_input == bot_move:
                print("Result: Match Tied!")
            elif (player_input == 'rock' and bot_move == 'scissors') or \
                 (player_input == 'scissors' and bot_move == 'paper') or \
                 (player_input == 'paper' and bot_move == 'rock'):
                print("Result: You secured this point!")
                self.player_points += 1
            else:
                print("Result: Bot takes this point!")
                self.bot_points += 1
                
            print(f"Current Standings -> You: {self.player_points} | Bot: {self.bot_points}")

if __name__ == "__main__":
    # Class object banakar run karne ka tarika
    arena = RockPaperScissorsGame()
    arena.start_game()