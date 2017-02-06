#
#  Shopping List App
#  Python Techdegree
#
#  Created by Dulio Denis on 2/5/17.
#  Copyright (c) 2017 ddApps. All rights reserved.
# ------------------------------------------------
#  Shopping List To-Do List
#  - Run the script to start using it
#  - Put new things into the List
#  - Enter the word DONE - in all CAPS - to quit the program
#  - And, once I quit, I want the app to show me everything that's on my List
#
# make a list to hold our items
shopping_list = []

# print out instructions on how to use the app
print("What should we do today?")
print("Enter 'DONE' to stop adding items.")


while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break
    else:
        # add new items to our List
        shopping_list.append(new_item)

# print out the List
print("Here is your list:")

for item in shopping_list:
    print(item)
