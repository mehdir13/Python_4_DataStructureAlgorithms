import time
import random

rank_order = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14}
suit_order = {'Clubs': 1, 'Diamonds': 2, 'Hearts': 3, 'Spades': 4}

def create_deck():
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [(rank, suit) for suit in suits for rank in ranks]

# Merge function to combine two sorted halves
def merge(left, right):
    sorted_deck = []
    i, j = 0, 0
    
    # Merge the two halves in order
    # index i tracks the left half and index j tracks the right half
    # the smaller card is appended to the "sorded_deck" list
    # then the index moves on to the next card in the half that already had a smaller card which is appened to the sorted deck
    while i < len(left) and j < len(right):
        if (rank_order[left[i][0]], suit_order[left[i][1]]) <= (rank_order[right[j][0]], suit_order[right[j][1]]):
            sorted_deck.append(left[i])
            i += 1
        else:
            sorted_deck.append(right[j])
            j += 1
    
    # Add any remaining cards from the left half
    while i < len(left):
        sorted_deck.append(left[i])
        i += 1
    
    # Add any remaining cards from the right half
    while j < len(right):
        sorted_deck.append(right[j])
        j += 1
    
    return sorted_deck

# Recursive Merge Sort function
def merge_sort(deck):
    if len(deck) <= 1:
        return deck  # Base case: a deck with 0 or 1 card is already sorted

    mid = len(deck) // 2  # Find the middle index
    left_half = merge_sort(deck[:mid])  # Recursively sort the left half
    right_half = merge_sort(deck[mid:])  # Recursively sort the right half
    
    return merge(left_half, right_half)  # Merge the sorted halves

start_time = time.time()
deck = create_deck()
random.shuffle(deck)
print("-----------<><><><><><><><><><><><><><>--------------------------")
print("Here is our UNsorted deck of cards (it ain't much but it's honest work): ")
for card in deck:
    print(card)
shuffle_deck_time = time.time() - start_time
print(f"Δt is: ", shuffle_deck_time)
print("-----------<><><><><><><><><><><><><><>--------------------------")

start_time = time.time()
sorted_deck = merge_sort(deck)
print("Et Voilà: your deck is SORTED now:")
print("(may cometh a day whereupon your dick gets sorted too)")
for card in sorted_deck:
    print(card)
bubble_sort_time = time.time() - start_time
print(f"Δt is: ", bubble_sort_time)