import sys
import random

equation_deck = {
    1: ["1+0",
        "2-1",
        "3-2",
        "4-3",
        "5-4",
        "6-5",
        "7-6",
        "8-7",
        "9-8",
        "10-9"],
    2: ["1+1",
        "2-0",
        "3-1",
        "4-2",
        "5-3",
        "6-4",
        "7-5",
        "8-6",
        "9-7",
        "10-8"],
    3: ["1+2",
        "2+1",
        "4-1",
        "5-2",
        "6-3",
        "7-4",
        "8-5",
        "9-6",
        "10-7"],
    4: ["2+2",
        "1+3",
        "3+1",
        "5-1",
        "6-2",
        "7-3",
        "8-4",
        "9-5",
        "10-6"],
    5: ["2+3",
        "3+2",
        "1+4",
        "4+1",
        "6-1",
        "7-2",
        "8-3",
        "9-4",
        "10-5"],
    6: ["3+3",
        "2+4",
        "4+2",
        "1+5",
        "5+1",
        "7-1",
        "8-2",
        "9-3",
        "10-4"],
    7: ["3+4",
        "4+3",
        "2+5",
        "5+2",
        "1+6",
        "6+1",
        "8-1",
        "9-2",
        "10-3"],
    8: ["4+4",
        "3+5",
        "5+3",
        "2+6",
        "6+2",
        "1+7",
        "7+1",
        "9-1",
        "10-2"],
    9: ["4+5",
        "5+4",
        "3+6",
        "6+3",
        "2+7",
        "7+2",
        "1+8",
        "8+1",
        "10-1"],
    10: ["5+5",
         "4+6",
         "6+4",
         "3+7",
         "7+3",
         "2+8",
         "8+2",
         "1+9",
         "9+1"]
}

class MathCardGame:
    
    def __init__(self, player1, player2):
        
        self.player1 = player1
        self.player2 = player2
        self.equation_deck = []
        self.value_deck = []
        self.player1_hand = []
        self.player2_hand = []
        
    def shuffle_decks(self):
        first_game_run = True
        
        if first_game_run:
            for value in range(1,11):
                self.value_deck.append(value)
            random.shuffle(self.value_deck)
                
            for key, equations in equation_deck.items():
                for equation in equations:
                    self.equation_deck.append(equation)
            random.shuffle(self.equation_deck)
            print("All cards have been shuffled")
            first_game_run = False
            return
        
        if len(self.value_deck) == 0:
            print("All value cards have been used. Reshuffling the value deck.")
            self.value_deck = self.used_values[:]
            random.shuffle(self.value_deck)
            self.used_values.clear()
        
        if len(self.equation_deck) == 0:
            print("All equation cards have been used. Reshuffling Deck.")
            self.equation_deck = self.used_equation[:]
            random.shuffle(self.equation_deck)
            self.used_equation.clear()
            
    def deal_cards(equations_list, num_players):
        deck = []
        for card, card_list in equation_deck.items():
           for equation in card_list:
            deck.append(equation)
        hands = []

        for player in range(num_players):
            player_hand = random.sample(deck, 7)
            hands.append(player_hand)
    
        for card in player_hand:
            deck.remove(card)

        return hands, deck

    
    def find_playable_cards():
        pass
    
    def check_for_winner(player_hands):
        for i in range(len(player_hands)):   
           hand = player_hands[i]        
        if len(hand) == 0:               
            return i                 

        return None
        
    
    def turn():
        pass
        
    def display_game(self):
        print("------- Welcome to the Math Game -------\n")
        self.player1 = input(f"Player 1, Please enter your name: ")
        self.player2 = input(f"Player 2, Please enter your name: ")
        self.shuffle_decks()
        print()
        
        print("-----Dealing Cards-----")
        # calls deals cards method
        
        print(f"{self.player1}'s deck: {self.player1_hand}")# add prints player 1 card list
        print(f"{self.player2}'s deck: {self.player2_hand}\n")# add prints player 2 card list
        print(f"------The value card is : -----")# adds value card
        
        # calls turn method 
        
        # calls check winner method
       
def main():
    game = MathCardGame("","")
    game.display_game()
    
    
if __name__ == "__main__":
    main()