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

class NumberMatch:
    """
    Represents a two-player math-based card game where players match equations 
    to drawn value cards.
    """
    
    def __init__(self, player1, player2):
        """
            Initilizes a NumberMatch game with 2 players. 

            Args:
                player1 (str): Name of the first player. 
                player2 (str): Name of the second player.
        """
        
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
        Uses the equation deck dictionary to rearrange the order of the equation 
        deck and value deck for the beginning of the game and later on, 
        individually, when playing the game. 
        
        Author: Jordan Stone
        
        Techniques:
            - Sequence Unpacking: used to unpakc each key, value pair from the 
              equation deck.
            
        Side effects: Changes the contents in the value_deck and 
                      equation_deck while also printing shuffle messages.
        """
        
        if len(self.value_deck) == 0:
            if self.used_values:
                print("All value cards have been used. Reshuffling the value deck.")
                self.value_deck = self.used_values[:]
                self.used_values.clear()
            else:
                self.value_deck = list(range(1,11))
            random.shuffle(self.value_deck)
            
        if len(self.equation_deck) == 0:
            if self.used_equation:
                print("All equation cards have been used. Reshuffling the equation deck.")
                self.equation_deck = self.used_equation[:]
                self.used_equation.clear()
            else:
                self.equation_deck = []
                for key, equation_list in equation_deck.items():
                    for card in equation_list:
                        self.equation_deck.append(card)
        
            random.shuffle(self.equation_deck)
        
        print("Decks have been shuffled.")
            
    def deal_cards(self, num_players):
        """
        Deals 7 equation cards to each player at the start of the game.

        Author: Shara Mohotti

        Techniques:
            - List comprehension: Used to rebuild the remaining deck while ensuring
              no duplicate cards are dealt to players.

        Args:
            num_players (int): Number of players in the game.

        Returns:
            tuple: (hands, deck)
                - hands is a list containing each player's starting hand
                - deck is the updated equation deck with dealt cards removed
        """
        
        deck = copy.deepcopy(self.equation_deck)
        hands = []

        for player in range(num_players):
            player_hand = random.sample(deck, 7)
            hands.append(player_hand)
            deck = [card for card in deck if card not in player_hand]

        return hands, deck

    def find_playable_cards(self, player_hand, drawn_value):
        """
        Determines and returns all playable equation cards from a player's hand
        that correctly match to a answer as the drawn value.

        Author: Murad Habtu

        Techniques: Generator expression - Used to efficiently filter valid equations
              based on their evaluated result.

        Args:
            player_hand (list[str]): The player's current hand of equation cards.
            drawn_value (int): The current value card players must match.

        Returns:
            list[str]: A list of equations from the hand that evaluate
            to the drawn value.
        """
        
        # Generator expression wrapped in list() for return
        gen_expression = (
            equation
            for equation in player_hand
            if eval(equation) == drawn_value
        )
        return list(gen_expression)
        
            
    def draw_value_card(self, num_cards: int = 1):
        """
        Draws one or more value cards from the value deck. If the deck is empty,
        it will be reshuffled before drawing.

        Author: Murad Habtu

        Techniques: Optional parameter - num_cards allows flexible drawing behavior.

        Args: num_cards (int, optional) - Number of value cards to draw (default = 1).

        Returns:
            int or list[int]:
                - If num_cards == 1, returns a single int value card.
                - If num_cards > 1, returns a list of drawn value cards.
        """
        
        if num_cards <= 0:
            raise ValueError("num_cards must be at least 1")

        drawn_values = []

        for _ in range(num_cards):
            if len(self.value_deck) == 0:
                self.shuffle_decks()

            value = self.value_deck.pop()
            drawn_values.append(value)
            self.used_values.append(value)

        return drawn_values[0] if num_cards == 1 else drawn_values
    
    def check_for_winner(self):
        """
        Determines whether either player has emptied their hand and won the game.

        Author: Shara Mohotti

        Techniques:
            - Conditional expression (ternary operator): Used to return
              the winner if Player 2 has an empty hand, or None otherwise.

        Returns:
            str or None: The name of the winning player, or None if no winner exists yet.
        """
        
        if len(self.player1_hand) == 0:
            return self.player1
        return self.player2 if len(self.player2_hand) == 0 else None
        
    def draw_equation_card(self):
        """
        Draws a single equation card from the equation deck.
        
        Author: Jordan Stone
        
        Returns:
            str: The equation card that was drawn from the deck.
        """
        
        if len(self.equation_deck) == 0:
            self.shuffle_decks()
        card = self.equation_deck.pop()
        return card
            
    
    def turn(self, drawn_value):
        """
        Runs a full turn for both players. Each player either plays a valid
        equation card that matches the drawn value or draws a new card if no such
        equation matches.

        Author: Shara Mohotti

        Args:
            drawn_value (int): The value card drawn for this round, determining which
                               equation cards are playable.

        Side Effects:
            - Modifies player hands by removing played cards or adding drawn cards.
            - Updates the used_equation list when a card is played.
            - Prints prompts and results for player interaction.
        """
        
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
        """
        This displays the entrie game and uses almost all of the methods in 
        this class.
        
        Author: Jordan Stone
        
        Techniques:
            - f-strings: formats players names, hands, and drawn values.
            
        Side effects:
            - Prints game status, hands, messages, modified players hands, and 
              updates the winner. 
        """
        
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
    """
    This uses a NumberMatch game instace with empty player names and starts 
    the game by calling the display_game() method.
    """
    
    game = NumberMatch("","")
    game.display_game()
    
    
if __name__ == "__main__":
    """
    Makes sure the NumberMatch game runs when it is executed. 
    """
    
    main()