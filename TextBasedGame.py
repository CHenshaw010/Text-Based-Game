# Christian Alexander Henshaw

# displays the initial game prompt, current location, and equipment.
def game_instructions():
    print('You are the commander of an elite force of soldiers.')
    print('There is a large enemy presence nearby blocking your\n'
          'route to your main force.')
    print('Gather all the resources to outfit your troops properly\n'
          'or your team will surely be defeated by the enemy.')
    print('----------------------------------------------------')
    print('Move commands: go North, go South, go East, go West')
    print('Gathering supplies: get item name')
    print('----------------------------------------------------')
    print('Your team is currently in the Tree Line.')
    print('Equipment: []')


# displays the current location, what the equipment in the room(if applicable) is, and the inventory.
# will be called frequently throughout the game
def game_status(current_location, locations, inventory=None):
    print('Your team is currently in the {}.'.format(current_location))
    # first if statement will check dictionary for equipment in the room while the current location is not the start.
    if current_location != 'Tree Line':
        # second if statement retrieves and displays the equipment found in the current room
        # as long as it is not in the players inventory already. if in inventory, item found prompt will not play
        if locations[current_location]['equipment'] not in inventory:
            print('Your team found {}'.format(locations[current_location]['equipment']))
    # prints player's inventory
    print('Equipment: {}'.format(inventory))
    print('---------------------------------')


# main game function below
def game():
    inventory = []
    # nested dictionary with all the room locations, directions to other locations, and equipment in each location
    locations = {

        'Tree Line': {'South': 'Abandoned Warehouse', 'East': 'Bunker'},
        'Abandoned Warehouse': {'North': 'Tree Line', 'South': 'Supply Depot', 'East': 'Cargo Bay',
                                'equipment': 'Body Armor'},
        'Supply Depot': {'North': 'Abandoned Warehouse', 'East': 'Residential Area', 'equipment': 'Ammunition'},
        'Bunker': {'West': 'Tree Line', 'East': 'Burned HQ', 'equipment': 'Grenades'},
        'Cargo Bay': {'West': 'Abandoned Warehouse', 'East': 'Battlefield', 'South': 'Residential Area',
                      'equipment': 'Two Tanks'},
        'Residential Area': {'North': 'Cargo Bay', 'West': 'Supply Depot', 'equipment': 'Food & Water'},
        'Burned HQ': {'West': 'Bunker', 'South': 'Battlefield', 'equipment': 'Enemy Intelligence'},
        'Battlefield': {'North': 'Burned HQ', 'West': 'Cargo Bay', 'equipment': 'Enemy Ground Force'},
    }

    # sets the start location to the Tree Line
    current_location = 'Tree Line'

    # calls the function to display the initial game prompt
    game_instructions()

    # True as so the game runs continuously until the game is won or lost
    while True:
        # first two statements check if the player is at the final room and with/without enough equipment
        # first if statement prints the winning statement if player has all items and is on the final location
        # will also break the loop to exit the game
        if len(inventory) == 6 and current_location == 'Battlefield':
            print('Your team engages the enemy ground force.\n'
                  'The battle was hard fought but your team\n'
                  'is victorious!')
            break
        # second if statement prints the losing message if player doesnt have all items and is at the final location
        # will also break the loop to exit the game
        elif len(inventory) < 6 and current_location == 'Battlefield':
            print('Your team engages the enemy ground force.\n'
                  'You did not gather enough supplies and your\n'
                  'team was forced to surrender.')
            print('GAME OVER')
            break

        # prompts the player for their move. .title().strip() is used to ensure the game accepts all variations of caps
        player_move = input('Where should your team go or what should your team do?\n').title().split()
        # first word is 'Go' or 'Get' so all following words are placed into variable the player specifically requested
        # such as the direction to move or the full name of the equipment to retrieve
        player_requested_item = ' '.join(player_move[1:])

        # following statements for player movement throughout the game
        if player_move[0] == 'Go':
            # checks the dictionary to verify if it is a valid move
            if player_move[1] in locations[current_location]:
                # updates current location variable to the location in the player specified direction
                current_location = locations[current_location][player_move[1]]
                print('Your team is moving.')
                # calls earlier function to print new current location and equipment
                game_status(current_location, locations, inventory)
            # else statement is a catch all if the players requested direction is not valid and not in dictionary
            else:
                print('You cannot go that way!')
                # calls earlier function to print new current location and equipment
                game_status(current_location, locations, inventory)
        # following statements for player retrieval of items throughout the game
        elif player_move[0] == 'Get':
            # if statement verifies requested item is correct for the current room and verifies its not in inventory
            if (player_requested_item == locations[current_location]['equipment']) \
                    and (player_requested_item not in inventory):
                # adds requested item into inventory
                inventory.append(player_requested_item)
                # calls earlier function to print new current location and equipment
                game_status(current_location, locations, inventory)
            # elif statement is used if the player is requesting an item that is not correct for the current location
            elif player_requested_item != locations[current_location]['equipment']:
                print('That equipment is not in the {}!'.format(current_location))
                # calls earlier function to print new current location and equipment
                game_status(current_location, locations, inventory)
            # elif statement is used if the player is requesting an item they already have (ensures no duplicates)
            elif player_requested_item in inventory:
                print('Your team already has that item!')
                # calls earlier function to print new current location and equipment
                game_status(current_location, locations, inventory)
            # else statement is a catch all if the player otherwise enters not valid item to prevent errors
            else:
                print('Error. Please try again.')
                # calls earlier function to print new current location and equipment
                game_status(current_location, locations, inventory)
        # following elif statements used to exit the game early if player requests it
        elif player_move[0] == 'Exit':
            print('Thanks for playing! Goodbye.\n')
            # exits the loop
            break
        # following statement is a catch all if the player inputs a not valid request to prevent errors
        else:
            print('Invalid Command!')
            # calls earlier function to print new current location and equipment
            game_status(current_location, locations, inventory)


# calls the game function to run the game itself
game()

# will print to provide a visual break following the game
print('---------------------------------')
print('=================================')
print('---------------------------------')
print('=================================')
print('---------------------------------')

# after game one, new variable for the amount of times played starts at one
game_counter = 1
# after game is complete (whether win or lose) will ask player if they want to play again
play_again = input('Do you want to play again? Yes/No\n').title().strip()
# if player inputs 'yes' to restart the game and will loop while they player inputs 'yes' to play again
while play_again == 'Yes':
    # calls the game function to run the game itself again
    game()
    # will play to provide a visual break following the game
    print('---------------------------------')
    print('=================================')
    print('---------------------------------')
    print('=================================')
    print('---------------------------------')
    # after game is complete (whether win or lose) will ask player if they want to play again
    play_again = input('Do you want to play again? Yes/No\n').title().strip()
    # updates variable game counter adding one after every attempt
    game_counter += 1
# if player inputs 'no' indicating not to restart the game
if play_again == 'No':
    print('Thank you again for playing!\n')
    # prints total number of game attempts
    print('Total Game Attempts: {}'.format(game_counter))
# following statement is a catch all in case player inputs a not valid request to prevent errors
else:
    print('Invalid Command! Please run the game again if you so wish.')
