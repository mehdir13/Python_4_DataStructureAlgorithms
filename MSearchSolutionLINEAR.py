import json

def numbersearch_function(number, lst):
    for index, value in enumerate(lst):
        if value == number:
            return index
    return -1  # The number is NOT in the list


targetnumber = 5851136
with open("unsorted.json", "r") as file:
    unsortedlist = json.load(file)

result = numbersearch_function(targetnumber, unsortedlist)

if result != -1:
    print(f"The number << {targetnumber} >> was found at index {result}.")
else:
    print(f"The number {targetnumber} was not found in the list.")

