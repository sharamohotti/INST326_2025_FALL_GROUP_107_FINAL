import sys
import random
import copy

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
    
    # add self in parameter, equations_list might not be nesscary and instead 
    # of eqautions_deck use self.equation_deck.
    def deal_cards(self, num_players):
        deck = copy.deepcopy(self.equation_deck)
        hands = []

        for player in range(num_players):
            player_hand = random.sample(deck, 7)
            hands.append(player_hand)
            #list comprehension
            deck = [card for card in deck if card not in player_hand]

        return hands, deck

    # use self in parameter
    def find_playable_cards():

    
    # use self in parameter.
    def draw_value_card(self):
    
    # add self in parameter and try and see if you can use self.playerhand1 
    # and self.playerhand2 (if it helps I have a set up in the display game)
    def check_for_winner(self):
        if len(self.player1_hand) == 0:
            return self.player1
    # conditional expression used here ↓
        return self.player2 if len(self.player2_hand) == 0 else None

        
    # use self in parameter.
    def turn(self, drawn_value):
    
        p1_playable = find_playable_cards(self.player1_hand, drawn_value)
        p2_playable = find_playable_cards(self.player2_hand, drawn_value)

    #PLAYER 1
        if p1_playable:
           print(f"{self.player1}, you may play: {p1_playable}")
           choice = input("Choose a card to play: ")

        # Keep asking until player chooses a legal card
           while choice not in p1_playable:
            choice = input("Invalid choice. Choose again: ")

           self.player1_hand.remove(choice)
        else:
           print(f"{self.player1} has no playable cards and passes.")

    #PLAYER 2 
        if p2_playable:
            print(f"{self.player2}, you may play: {p2_playable}")
            choice = input("Choose a card to play: ")

            while choice not in p2_playable:
                choice = input("Invalid choice. Choose again: ")

            self.player2_hand.remove(choice)
        else:
            print(f"{self.player2} has no playable cards and passes.")

     


   
         
        
        
    def display_game(self):
        print("------- Welcome to the Math Game -------\n")
        self.player1 = input(f"Player 1, Please enter your name: ")
        self.player2 = input(f"Player 2, Please enter your name: ")
        self.shuffle_decks()
        print()
        
        print("-----Dealing Cards-----")
        hands, deck = self.deal_cards(2)
        self.player1_hand = hands[0]
        self.player2_hand = hands[1]
        
        print(f"{self.player1}'s deck: {self.player1_hand}")
        print(f"{self.player2}'s deck: {self.player2_hand}\n")
                
        ## This might work its only a guideline for me.
        winner = None
        while winner is None:
            
            drawn_value = self.draw_value_card()
            print(f"------The value card is : {self.draw_value_card}-----")
            
            player1 = self.find_playable_cards(self.player1_hand, drawn_value)
            player2 = self.find_playable_cards(self.player1_hand, drawn_value)
            
            print(f"{self.player1}'s playable cards: {self.player1_hand}")
            print(f"{self.player2}'s playable cards: {self.player2_hand}\n")
            
            self.turn(drawn_value)
            winner = self.check_for_winner([self.player1_hand, self.player2_hand])
        
       
def main():
    game = MathCardGame("","")
    game.display_game()
    
    
if __name__ == "__main__":
    main()