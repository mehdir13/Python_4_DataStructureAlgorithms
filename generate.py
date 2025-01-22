"""This is the source code that was used to generate the large numbers."""

import random
import json

LIST_SIZE = 1_000_000 # Here I use underscores to make reading the number a bit easier.

# Generate a list of 10 million random integers between 1 and 10 million (allowing duplicates)
unsorted_list = [random.randint(1, 10000000) for _ in range(LIST_SIZE)]

# Save the list to a JSON file
with open('unsorted.json', 'w') as f:
    json.dump(unsorted_list, f)

# Now sort it and do the same
unsorted_list.sort()

with open("sorted.json", "w") as f:
    json.dump(unsorted_list, f)
