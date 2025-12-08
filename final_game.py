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
        
        self.used_values = []
        self.used_equation = []
        
    def shuffle_decks(self):
        """
            The shuffle_decks method uses the equation deck dictionary to 
            rearrange the order of the equation deck and value deck when first 
            called on in the beginning of the game and later on, individually, 
            when playing the game. 
            
            Side effects: Changes the contents in the value_deck and 
                          equation_deck while also printing shuffle messages.
            Return (None): Only meant for the first run of the game. 
        """
        if len(self.value_deck) == 0:
            if self.used_values:
                print("All value cards have been used. Reshuffling the value deck.")
                self.value_deck = self.used_values[:]
                self.used_values.clear()
            else:
                self.value_deck = list(range(1, 11))
            random.shuffle(self.value_deck)

        # Shuffle equation deck
        if len(self.equation_deck) == 0:
            if self.used_equation:
                print("All equation cards have been used. Reshuffling the equation deck.")
                self.equation_deck = self.used_equation[:]
                self.used_equation.clear()
            else:
                for eq_list in equation_deck.values():
                    self.equation_deck.extend(eq_list)
            random.shuffle(self.equation_deck)

        print("Decks have been shuffled.")
    
    
    def deal_cards(self, num_players):
        deck = copy.deepcopy(self.equation_deck)
        hands = []

        for player in range(num_players):
            player_hand = random.sample(deck, 7)
            hands.append(player_hand)
            #list comprehension
            deck = [card for card in deck if card not in player_hand]

        return hands, deck

    def find_playable_cards(self, player_hand, drawn_value):
        return [
            equation
            for equation in player_hand
            if eval(equation) == drawn_value
        ]
    
    def draw_value_card(self, num_cards: int = 1):
        if num_cards <= 0:
            raise ValueError("num_cards must be at least 1")

        drawn_values = []

        for _ in range(num_cards):
            if len(self.value_deck) == 0:
                self.shuffle_decks()

            value = self.value_deck.pop()
            drawn_values.append(value)

            # Track used values so shuffle_decks can rebuild the deck later
            self.used_values.append(value)

        return drawn_values[0] if num_cards == 1 else drawn_values
    
    def check_for_winner(self):
        if len(self.player1_hand) == 0:
            return self.player1
    # conditional expression used here ↓
        return self.player2 if len(self.player2_hand) == 0 else None
        
    def draw_equation_card(self):
        if len(self.equation_deck) == 0:
            self.shuffle_decks()
        card = self.equation_deck.pop()
        return card
            
    
    def turn(self, drawn_value):
    
        p1_playable = self.find_playable_cards(self.player1_hand, drawn_value)
        p2_playable = self.find_playable_cards(self.player2_hand, drawn_value)

    #PLAYER 1
        if p1_playable:
            print(f"{self.player1}, you may play: {p1_playable}")
            choice = input("Choose a card to play: ")

            # Keep asking until player chooses a legal card
            while choice not in p1_playable:
                choice = input("Invalid choice. Choose again: ")

            self.player1_hand.remove(choice)
            self.used_equation.append(choice)#
        else:
            print(f"{self.player1} has no playable cards and passes.")
            new_card = self.draw_equation_card()#
            self.player1_hand.append(new_card)#
            print(f"{self.player1} drew {new_card}.\n")#

    #PLAYER 2 
        if p2_playable:
            print(f"{self.player2}, you may play: {p2_playable}")
            choice = input("Choose a card to play: ")

            while choice not in p2_playable:
                choice = input("Invalid choice. Choose again: ")

            self.player2_hand.remove(choice)
            self.used_equation.append(choice)#
        else:
            print(f"{self.player2} has no playable cards and passes.")
            new_card = self.draw_equation_card()#
            self.player2_hand.append(new_card)#
            print(f"{self.player2} drew {new_card}.\n")#

        
    def display_game(self):
        print("------- Welcome to the Math Game -------\n")
        self.player1 = input(f"Player 1, Please enter your name: ")
        self.player2 = input(f"Player 2, Please enter your name: ")
        self.shuffle_decks()
        print()
        
        print("----- Dealing Cards -----\n")
        hands, deck = self.deal_cards(2)
        self.player1_hand = hands[0]
        self.player2_hand = hands[1]
        
        print(f"{self.player1}'s hand: {self.player1_hand}")
        print(f"{self.player2}'s hand: {self.player2_hand}\n")
        
        winner = None
        round_num = 1
        
        while winner is None:
            print(f"----- Round {round_num} -----")
            
            drawn_value = self.draw_value_card()
            print(f"The drawn value card is: {drawn_value}")
            
            p1_playable = self.find_playable_cards(self.player1_hand, drawn_value)
            p2_playable = self.find_playable_cards(self.player2_hand, drawn_value)
            
            print(f"{self.player1}'s playable cards: {p1_playable}")
            print(f"{self.player2}'s playable cards: {p2_playable}\n")
            
            self.turn(drawn_value)
            
            print(f"After this turn: ")
            print(f"{self.player1}'s hand: {self.player1_hand}")
            print(f"{self.player2}'s hand: {self.player2_hand}\n")
            
            winner = self.check_for_winner()
            round_num += 1
        
        print(f"{winner} is the WINNER!")
        
       
def main():
    game = MathCardGame("","")
    game.display_game()
    
    
if __name__ == "__main__":
    main()