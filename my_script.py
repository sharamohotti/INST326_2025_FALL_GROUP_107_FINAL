import random
from argparse import ArgumentParser
import re
import sys
import copy


#Jordan worte this code
# Equation_deck Dictionary only 1-10 add and sub.
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

def shuffle_decks():
    """
    This is reshuffles both decks after calling every value left 
    in the deck.
    
    Side Effects:
        - Prints the drawn values and equations to the terminal.
        - Shuffles both decks in place.
        - Clears and reuses lists to simulate a continuous game cycle.
    """
    
    # Value Deck
    """This creates a new list of values 1-10 and shuffles them."""
    value_deck = []
    for value in range(1,11):
        value_deck.append(value)
    random.shuffle(value_deck)
    
    """This creates a used values list so when a value is picked from the deck 
       there are no duplicates and the deck can reshuffle."""
    used_values = []
    for value_card in value_deck:
        print(f"Value: {value_card}")
        used_values.append(value_card)
    
    """This just prints a message saying the deck will reshuffle and the cards 
       will get randomized again. 
    """
    print("All value cards have been used. Reshuffling the deck.")
    random.shuffle(value_deck)
    used_values.clear()
    
    
    # Equation Deck
    """This turns the equation_deck dictionary into a list of just 
       equations for now and shuffles it so it is random."""
    equations_list = []
    for value, equations in equation_deck.items():
        for equation in equations:
            equations_list.append(equation)
    random.shuffle(equations_list)
    
    """This creates another used list but for the equations so there are no 
       duplicates. Then it prints out each equation randomly until it needs to
       reshuffle. """
    used_equations = []
    for equation in equations_list:
        print(f"Equation picked from deck: {equation}")
        used_equations.append(equation)
        
    """Does the same thing at the end of the value deck part but with 
       the equations."""
    print("All equations have been used reshuffling.")
    used_equations.clear()
    
    # Murad wrote this method
def find_playable_cards(player_hand, drawn_value):
    """
    Returns all equations in the player's hand that evaluate to the drawn value.
    If none match, returns an empty list (meaning the player should draw a card).

    Args:
        player_hand (list[str]): All equation cards as strings, e.g. ["2+3", "7-4"]
        drawn_value (int): Value card drawn, e.g. 5

    Returns:
        list[str]: All playable equation cards matching the drawn value.
    """

    # This creates an empty list that will store the equations that match
    playable_cards = []

    # This loops through every equation in the player's hand
    for equation in player_hand:
        # This evaluates the equation string into a number result
        calculated_value = eval(equation)

        # This checks if the result of the equation matches the drawn value
        if calculated_value == drawn_value:
            playable_cards.append(equation)

    # This returns all equations that match the value card
    return playable_cards
    
shuffle_decks()
    
#shara's code
def deal_cards(equations_list, num_players):
    """
    Deal 7 random equation cards to each player from a list of equations taken
    from equation deck.

    This function takes a list of equation strings and deals 7 random, 
    non-repeating equations to each player. Dealt cards are removed from 
    the deck to ensure no duplicates. The function returns both the 
    list of player hands and the remaining deck after dealing.

    Parameters:
        equations_list (list):
            A list of equation strings that represents the full deck.
        num_players (int):
            Number of players to deal cards to. Each player receives 7 cards.

    Returns:
        tuple:
            - hands (list of lists): 
                A list where each item is a player's hand 
            - deck (list):
                The remaining equation cards after dealing the cards.
    """

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

# this checks that the function outputs correctly
player_hands, updated_deck = deal_cards(equation_deck, 2)
print(f"Player One's hand: {player_hands[0]} Player Two's hand: {player_hands[1]}")
print(f"Remaining cards in deck: {updated_deck}")

        
    
    
    
    
      
        
        
       
            
    
