import random

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
            
shuffle_decks()
    
    
        
       
            
    
