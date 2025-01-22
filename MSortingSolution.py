import time
import random # we are going to need randomization to "shuffle" out deck before sorting it

# Define the custom order for ranks and suits: rank_order dictionary + suit_order dictionary
rank_order = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14}
suit_order = {'Clubs': 1, 'Diamonds': 2, 'Hearts': 3, 'Spades': 4}

# list comprehention to create an unabridged deck of cards
def create_decklist_function():
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [(rank, suit) for suit in suits for rank in ranks] # each card is tuple including two elements: suit & rank; each are a dictionary 

# Bubble sort function for sorting cards
def bubblesortcard_function(deck):
    n = len(deck)
    for i in range(n): # i is the number of times we go through the whole deck. every time the biggest value is "bubbled-up" at the end of the list.
        for j in range(0, n - i - 1): # n - i - 1 because the last i card is already sorted and in the correct position

             # Comparing two adjacent cards (ranks first, then suits if ranks are equal) 
             # deck[j]: The current card. Dictionary of ("rank_order, suit_order")
             # deck[j + 1]: The next card.
             # every card is a tuple; eg. ('3', 'Hearts'). Therefore deck[j][0] refers to the index 0 of the tuple, i.e., the rank value (3 in eg), and deck[j][1] referes to the index 1 of the tuple, i.e., the suit value (Hearts in eg).             
            if (rank_order[deck[j][0]], suit_order[deck[j][1]]) > (rank_order[deck[j + 1][0]], suit_order[deck[j + 1][1]]):
                # Swap if cards are out of order. Tuple unpacking
                deck[j], deck[j + 1] = deck[j + 1], deck[j]
    return deck

start_time = time.time()
deck = create_decklist_function()
random.shuffle(deck) #shuffling the deck to make sure it is unsorted
print("-----------<><><><><><><><><><><><><><>--------------------------")
print("Here is our UNsorted deck of cards (it ain't much but it's honest work): ")
for card in deck:
    print(card)
shuffle_deck_time = time.time() - start_time
print(f"Δt is: ", shuffle_deck_time)
print("-----------<><><><><><><><><><><><><><>--------------------------")

start_time = time.time()
sorted_deck = bubblesortcard_function(deck)
print("Et Voilà: your deck is SORTED now:")
print("(may cometh a day whereupon your dick gets sorted too)")
for card in sorted_deck:
    print(card)
# eahc card is tuple including rank dictionary & suit dictionary. That is why every card is printed out as a tuple; eg. ('3', 'Hearts')
bubble_sort_time = time.time() - start_time
print(f"Δt is: ", bubble_sort_time)