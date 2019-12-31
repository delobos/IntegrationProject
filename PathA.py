# Daniel Lobos
# Text Based adventure game


import PathALore

FuggsData = {'name' : "Fuggs",
             'health': 100,
             'location Name' : 'Pyramid Entrance',
             'location' : "You are at the entrance of a pyramid."}


class Location:
    def __init__(self, moves, actions, items, doors, second_floor_statues, puzzle_lock, lanterns):
        self.moves = moves
        self.actions = actions
        self.items = items
        self.doors = doors
        self.second_floor_statues = second_floor_statues
        self.puzzle_lock = puzzle_lock
        self.lanterns = lanterns
        self.description = "At the entrance of this pyramid you can barely make out the dimly lit room inside"


def help():
    print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")
    print("You will be exploring places and interacting "
          "with items in the game.\n")

    print("Please use words like 'forward', 'up, 'left', 'right',"
          " 'down', and 'back' for movement "
          "inside a structure.\n")

    print("Every time you step into a room you will be located in the"
          " center facing north or the 'forward'/ 'up' direction\n")

    print("Different rooms have different actions "
          "you can take. They are all one word actions,"
          " where it may ask what do you want to use that action on.\n")

    print("Examples of this are 'use', 'grab',"
          " 'light', 'pry', 'give', to name a few")

    print("To see a description of where you are in a room"
          " or an area, just type 'look', this also "
          "acts as an investigate in certain rooms..\n")

    print("To see this introductory list again, type 'help'.\n")
    print("When you are ready to continue, press the ENTER key.\n")
    input()
    print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")


def floor_puzzle_pt1():
    help()
    print("\nYou step into this musty dimly lit room. Right before the end of"
          " the entry hallway, you see a large arrow pointing ahead into the room")
    print("The floor in front of you is a stone tile floor, decorated"
          " with figures of animals, objects,"
          " and vegetation.")
    print("At the mouth of this room sits four stones in a row,"
          " on each one from left to right is"
          " a Rabbit, Sun, Leaf, and a Hawk")
    print("Which one would you like to step on? or does it even matter?")
    floor_puzzle_loop1 = 0
    while FuggsData['health'] > 1 and floor_puzzle_loop1 == 0:
        try:
            floor_puzzle_choice = input("\nRabbit \nSun \nLeaf \nHawk ").lower()
            if floor_puzzle_choice[0] == 'r':
                print("\nYou hear some mechanisms moving in the walls"
                      " before feeling a sharp pain in your side as you"
                      " jump back towards the entrance and off the stone tile.")
                print("Looking down you see a dart with red feathered tail sticking out of your side")
                FuggsData['health'] -= 25
                print("You have ", FuggsData['health'], " health left")
                fuggs_death_check()
                continue
            elif floor_puzzle_choice[0] == 's':
                print("\nYou hear a click as the tile slides into the floor and stays down.")
                floor_puzzle_loop1 += 1
                floor_puzzle_pt2()
            elif floor_puzzle_choice[0] == 'l':
                print("\nYou hear some mechanisms moving in the walls"
                      " before feeling a sharp pain in your side as"
                      " you jump back towards the entrance and off"
                      " the stone tile.")
                print("Looking down you see a dart with red feathered tail sticking out of your side")
                FuggsData['health'] -= 25
                print("You have ", FuggsData['health'], " health left")
                fuggs_death_check()
                continue
            elif floor_puzzle_choice[0] == 'h':
                print("\nYou hear some mechanisms moving"
                      " in the walls before feeling a sharp pain"
                      " in your side as you jump back towards"
                      " the entrance and off the stone tile.")
                print("Looking down you see a dart with red feathered tail sticking out of your side")
                FuggsData['health'] -= 25
                print("You have ", FuggsData['health'], " health left")
                fuggs_death_check()
                continue
        except IndexError:
            print("\nPlease select one of the options")
            continue


def floor_puzzle_pt2():
    floor_puzzle_loop2 = 0
    while FuggsData['health'] > 1 and floor_puzzle_loop2 == 0:
        try:
            floor_puzzle_choice2 = input("\nHawk \nRabbit \nSun \nLeaf ").lower()
            if floor_puzzle_choice2[0] == 'h':
                print("\nYou hear some mechanisms moving"
                      " in the walls before feeling a sharp pain"
                      " in your side as you jump back towards"
                      " the entrance and off the stone tile.")
                print("Looking down you see a dart with red feathered tail sticking out of your side")
                FuggsData['health'] -= 25
                print("You have ", FuggsData['health'], " health left")
                fuggs_death_check()
                continue
            elif floor_puzzle_choice2[0] == 'r':
                print("\nYou hear some mechanisms moving in the"
                      " walls before feeling a sharp pain in your"
                      " side as you jump back towards the entrance"
                      " and off the stone tile.")
                print("Looking down you see a dart with red feathered tail sticking out of your side")
                FuggsData['health'] -= 25
                print("You have ", FuggsData['health'], " health left")
                fuggs_death_check()
                continue
            elif floor_puzzle_choice2[0] == 's':
                print("\nYou hear some mechanisms moving in the"
                      " walls before feeling a sharp pain in your"
                      " side as you jump back towards the entrance"
                      " and off the stone tile.")
                print("Looking down you see a dart with red feathered tail sticking out of your side")
                FuggsData['health'] -= 25
                print("You have ", FuggsData['health'], " health left")
                fuggs_death_check()
                continue
            elif floor_puzzle_choice2[0] == 'l':
                print("\nYou hear a click as the tile slides into the floor and stays down.")
                floor_puzzle_pt3()
                floor_puzzle_loop2 += 1
        except IndexError:
            print("\nPlease select one of the options")
            continue


def floor_puzzle_pt3():
    floor_puzzle_loop3 = 0
    while FuggsData['health'] > 1 and floor_puzzle_loop3 == 0:
        try:
            floor_puzzle_choice3 = input("\nHawk \nRabbit \nSun \nLeaf ").lower()
            if floor_puzzle_choice3[0] == 'h':
                print("\nYou hear some mechanisms moving in the"
                      " walls before feeling a sharp pain in your"
                      " side as you jump back towards the entrance"
                      " and off the stone tile.")
                print("Looking down you see a dart with red feathered tail sticking out of your side")
                FuggsData['health'] -= 25
                print("You have ", FuggsData['health'], " health left")
                fuggs_death_check()
                continue
            elif floor_puzzle_choice3[0] == 's':
                print("\nYou hear some mechanisms moving in"
                      " the walls before feeling a sharp pain"
                      " in your side as you jump back towards"
                      " the entrance and off the stone tile.")
                print("Looking down you see a dart with red feathered tail sticking out of your side")
                FuggsData['health'] -= 25
                print("You have ", FuggsData['health'], " health left")
                fuggs_death_check()
                continue
            elif floor_puzzle_choice3[0] == 'l':
                print("\nYou hear some mechanisms moving "
                      "in the walls before feeling a sharp"
                      " pain in your side as you jump back"
                      " towards the entrance and off"
                      " the stone tile.")
                print("Looking down you see a dart with red feathered tail sticking out of your side")
                FuggsData['health'] -= 25
                print("You have ", FuggsData['health'], " health left")
                fuggs_death_check()
                continue
            elif floor_puzzle_choice3[0] == 'r':
                print("\nYou hear a click as the tile slides into the floor and stays down.")
                floor_puzzle_loop3 += 1
                floor_puzzle_pt4()

        except IndexError:
            print("\nPlease select one of the options")
            continue


def floor_puzzle_pt4():
    floor_puzzle_loop4 = 0
    while FuggsData['health'] > 1 and floor_puzzle_loop4 == 0:
        try:
            floor_puzzle_choice2 = input("\nHawk \nRabbit \nSun \nLeaf ").lower()
            if floor_puzzle_choice2[0] == 'l':
                print("\nYou hear some mechanisms moving in"
                      " the walls before feeling a sharp"
                      " pain in your side as you jump back"
                      " towards the entrance and off"
                      " the stone tile.")
                print("Looking down you see a dart with red feathered tail sticking out of your side")
                FuggsData['health'] -= 25
                print("You have ", FuggsData['health'], " health left")
                fuggs_death_check()
                continue
            elif floor_puzzle_choice2[0] == 'r':
                print("\nYou hear some mechanisms moving in the"
                      " walls before feeling a sharp pain in"
                      " your side as you jump back towards"
                      " the entrance and off the stone tile.")
                print("Looking down you see a dart with red feathered tail sticking out of your side")
                FuggsData['health'] -= 25
                print("You have ", FuggsData['health'], " health left")
                fuggs_death_check()
                continue
            elif floor_puzzle_choice2[0] == 's':
                print("\nYou hear some mechanisms moving"
                      " in the walls before feeling a sharp "
                      "pain in your side as you jump back towards"
                      " the entrance and off the stone tile.")
                print("Looking down you see a dart with red feathered tail sticking out of your side")
                FuggsData['health'] -= 25
                print("You have ", FuggsData['health'], " health left")
                fuggs_death_check()
                continue
            elif floor_puzzle_choice2[0] == 'h':
                print("\nYou hear a click as the tile"
                      " slides into the floor and stays down.")
                print("You then hear mechanisms all"
                      " around you as a portion of the"
                      " wall in front of you and to your"
                      " right slide up revealing two rooms.")
                print("The door to the pyramid behind you closes"
                      ", leaving a giant stone wall in its place")
                FuggsData['location Name'] = 'Entrance Room'
                FuggsData['location'] = 'You are in the entrance room of the pyramid'
                doors['Desert Door'] = 'closed'
                entrance_room()
                floor_puzzle_loop4 += 1
        except IndexError:
            print("\nPlease select one of the options")
            continue


def fuggs_death_check():
    if FuggsData['health'] < 1:
        print("\nToo badly inured, you feel yourself become weaker as you fall over dead.")
        print("Maybe next time will be better")
        print("But then, you wake up to the sound of someone yelling 'INTRUDER!'")
    else:
        pass


"""
Room descriptions
"""


def dog_statue_room_description():
    print("\nYou enter the room and are greeted to"
          " the sight of cobwebs and dust"
          " littering the room.")
    print("A large dog shaped statue sits on the"
          " right side of the room against the wall")


def entrance_room_description():
    print("\nYou are in the first room you came into"
          " when coming into the pyramid. A empty room"
          " besides the figures littering the stone"
          " tiles on the floor.")


def storage_room_description():
    print("\nYou enter into what looks like a "
          "storage room. Barrels sit all over the"
          " room, as does various pieces of furniture.")


def base_floor_room_description():
    print("\nYou enter an empty room."
          " The air smells damp and musty."
          " On the north side of the room sits a"
          " staircase that leads up to the second floor.")


def three_statues_room1_description():
    print("\nYou enter the right side"
          " of the room with a staircase "
          "to the north, statue pedestals on"
          " the right, and the other part "
          "of the room on the left"
          " passed a doorway.")


def three_statues_room2_description():
    print("\nYou are in a room with"
          " three statue pedestals on the "
          "left side of the room and a door "
          "way on the right leading to the"
          " right side of the room.")


def seve_statue_room_description():
    print("\nYou enter a large empty room"
          " except for the seven gargoyle "
          "statues each with one are held "
          "outright holding a lantern")


def stone_room_description():
    print("\nYou are in a room where all"
          " the walls of the pyramid meet"
          " at a point above you. In the "
          "center of the room sits an alter")


"""
Items dictionary and global class Location call
"""

items = {'hands': 'not full', 'torch': 'wall', 'Prybar': 'Dog Room', 'Moon Stone': 'Statue hand', 'Chicken Statue': 'Right Side', 'Fox Statue': 'Right Side', 'Grain Statue': 'Right Side', 'Blood Stone': "alter"}

doors = {"Desert Door": "open", 'Second floor stairs door': 'closed', 'Third floor stairs door': 'closed'}

second_floor_statues = {'Chicken Statue': 'Right Side', 'Fox Statue': 'Right Side', 'Grain Statue': 'Right Side'}

puzzle_lock = {'Chicken Statue': 'unlock', 'Fox Statue': 'unlock', 'Grain Statue': 'unlock'}

lanterns = {'Lantern 1': 'unlit', 'Lantern 2': 'unlit', 'Lantern 3': 'unlit', 'Lantern 4': 'unlit', 'Lantern 5': 'unlit', 'Lantern 6': 'unlit', 'Lantern 7': 'unlit'}


room = Location(('forward', 'back', 'up', 'down', 'left', 'right'), ('look'), items,  doors, second_floor_statues, puzzle_lock, lanterns)


"""
Room possible moves and actions
"""

def entrance_room_move_and_actions(player_input):
    if player_input in room.moves:
            entrance_room_moves(player_input)
    elif player_input in room.actions:
        entrance_room_actions(player_input)
    else:
        print("\nNot a valid input in this room")
        game_on()


def storage_room_move_and_actions(player_input):
    if player_input in room.moves:
            storage_room_moves(player_input)
    elif player_input in room.actions:
        storage_room_actions(player_input)
    else:
        print("\nNot a valid input in this room")
        game_on()


def dog_statue_room_move_and_actions(player_input):
    if player_input in room.moves:
        dog_statue_room_moves(player_input)
    elif player_input in room.actions:
        dog_statue_room_actions(player_input)
    else:
        print("\nNot a valid input in this room")
        game_on()


def base_floor_staircase_room_move_and_actions(player_input):
    if player_input in room.moves:
        base_floor_staircase_room_moves(player_input)
    elif player_input in room.actions:
        base_floor_staircase_room_actions(player_input)
    else:
        print("\nNot a valid input in this room")
        game_on()


def three_statue_room1_move_and_actions(player_input):
    if player_input in room.moves:
        three_statue_room1_moves(player_input)
    elif player_input in room.actions:
        three_statue_room1_actions(player_input)
    else:
        print("\nNot a valid input in this room")
        game_on()


def three_statue_room2_move_and_actions(player_input):
    if player_input in room.moves:
        three_statue_room2_moves(player_input)
    elif player_input in room.actions:
        three_statue_room2_actions(player_input)
    else:
        print("\nNot a valid input in this room")
        game_on()


def seven_statue_room_move_and_actions(player_input):
    if player_input in room.moves:
        seven_statue_room_moves(player_input)
    elif player_input in room.actions:
        seven_statue_room_actions(player_input)
    else:
        print("\nNot a valid input in this room")
        game_on()


def stone_room_move_and_actions(player_input):
    if player_input in room.moves:
        stone_room_moves(player_input)
    elif player_input in room.actions:
        stone_room_actions(player_input)
    else:
        print("\nNot a valid input in this room")
        game_on()


"""
Room moves code
"""

def entrance_room_moves(player_moves):
    if player_moves == 'forward' or player_moves == 'up':
        dog_statue_room_description()
        FuggsData['location Name'] = 'Dog Statue Room'
        FuggsData['location'] = "You are in an old " \
                                "dusty room. A large statue" \
                                " of a dog on the right side" \
                                " of the room"
        global room
        room = Location(('forward', 'back', 'up', 'down', 'left', 'right'), ('look', 'grab', 'take', 'use', 'place', 'put', 'give'), items, doors, second_floor_statues, puzzle_lock, lanterns)
        dog_statue_room()
    elif player_moves == 'back' or player_moves == 'down':
        if doors['Desert Door'] == 'open':
            print("\nYou are back outside!")
            FuggsData['location Name'] = 'Outside Pyramid'
            FuggsData['location'] = 'You are at the' \
                                    ' entrance of a pyramid.'
        else:
            print("\nYou can't go back"
                  " outside with the"
                  " entrance blocked")
            game_on()
    elif player_moves == 'right':
        storage_room_description()
        FuggsData['location Name'] = 'Storage Room'
        FuggsData['location'] = 'You are in a storage' \
                                ' room full of furniture,' \
                                ' barrels, and crates.'
        room = Location(('forward', 'back', 'left','up', 'down', 'right'), ('look', 'grab', 'take', 'pry'), items, doors, second_floor_statues, puzzle_lock, lanterns)
        storage_room()
    elif player_moves == 'left':
        print("\nYou see a big plain wall")
        game_on()
    else:
        print("\nThat is not a valid input,"
              " please visit the 'Help' "
              "option if you need to see"
              " the acceptable responses.")
        game_on()


def storage_room_moves(player_moves):
    if player_moves == 'forward' or player_moves == 'up':
        print("\nYou walk up to the "
              "only source of light in"
              " this room, a lit torch.")
        game_on()
    elif player_moves == 'back' or player_moves == 'down':
        print("\nYou search through"
              " some barrels but find"
              " nothing of interest")
        game_on()
    elif player_moves == 'right':
        print("\nYou rummage through some "
              "items and find a statue of "
              "a human man, a little over 4"
              " feet tall with both of"
              " its arms out stretched"
              " slightly.")
        print("One hand is balled into a fist"
              " and the other has an open"
              " palm facing upward, and "
              "embedded in its palm is"
              " a crescent moon "
              "shaped stone.")
        game_on()
    elif player_moves == 'left':
        entrance_room_description()
        FuggsData['location Name'] = 'Entrance Room'
        FuggsData['location'] = 'The entrance room' \
                                ' with the figures on the floor'
        room = Location(('forward', 'back', 'up', 'down', 'left', 'right'), ('look'), items,  doors, second_floor_statues, puzzle_lock, lanterns)
        entrance_room()
    else:
        print("\nThat is not a valid"
              " input, please visit "
              "the 'Help' option if you"
              " need to see the "
              "acceptable responses.")
        game_on()


def dog_statue_room_moves(player_moves):
    if player_moves == 'forward' or player_moves == 'up':
        print("\nYou see a old rusted "
              "pry bar covered in "
              "cobwebs laying against"
              " the wall.")
        game_on()
    elif player_moves == 'back' or player_moves == 'down':
        entrance_room_description()
        FuggsData['location Name'] = 'Entrance Room'
        FuggsData['location'] = 'The entrance ' \
                                'room with the ' \
                                'figures on the floor'
        global room
        room = Location(('forward', 'back', 'up', 'down', 'left', 'right'), ('look'), items,  doors, second_floor_statues, puzzle_lock, lanterns)
        entrance_room()
    elif player_moves == 'right':
        if items['Moon Stone'] == 'Dog Statue':
            base_floor_room_description()
            FuggsData['location Name'] = 'Base Floor ' \
                                         'Staircase Room'
            FuggsData['location'] = 'You are in an empty ' \
                                    'room. Against the ' \
                                    'north side of the ' \
                                    'wall is a staircase' \
                                    ' leading up.'
            room = Location(('forward', 'back',  'up', 'down', 'left', 'right'), ('look'), items, doors, second_floor_statues, puzzle_lock, lanterns)
            base_floor_room()
        else:
            print("\nYou see a statue of "
                  "a dog, in the sitting position"
                  " and it's tongue out"
                  " as if it was panting.")
            print("Sitting on it's tongue"
                  " is a hole in the "
                  "shape of a crescent moon")
            game_on()
    elif player_moves == 'left':
        print("\nYou see a big plain wall")
        game_on()
    else:
        print("\nThat is not a valid"
              " input, please visit"
              " the 'Help' option if "
              "you need to see the "
              "acceptable responses.")
        game_on()


def base_floor_staircase_room_moves(player_moves):
    if player_moves == 'forward' or player_moves == 'up' or player_moves == 'staircase':
        print("\nYou climb up the "
              "stairs onto the "
              "next floor")
        three_statues_room1_description()
        FuggsData['location'] = 'You are in the' \
                                ' middle of the right rooms,' \
                                ' with three statues on your right' \
                                ' and 3 empty pillars on the' \
                                ' left side of the room'
        FuggsData['location Name'] = 'Three Statue' \
                                     ' Room Right Side'
        global room
        room = Location(('forward','back', 'up', 'down', 'left', 'right'), ('look', 'take', 'carry', 'grab', 'haul', 'place', 'put', 'use', 'set'), items, doors, second_floor_statues, puzzle_lock, lanterns)
        three_statue_room1()
    elif player_moves == 'back' or player_moves == 'down':
        print("\nYou are met with a "
              "plain wall and nothing "
              "of interest to see.")
        game_on()
    elif player_moves == 'right':
        print("\nYou are met with a"
              " plain wall and nothing"
              " of interest to see.")
        game_on()
    elif player_moves == 'left':
        dog_statue_room_description()
        FuggsData['location Name'] = 'Dog Statue Room'
        FuggsData['location'] = "The entrance of the " \
                                "room with small piles of gold," \
                                " a random assortment of jewels, " \
                                "and a large statue of a dog" \
                                " on the right side of the room"
        room = Location(('forward', 'back', 'left', 'up', 'down', 'right'), ('look', 'grab', 'take', 'use', 'place', 'put', 'give'), items, doors, second_floor_statues, puzzle_lock, lanterns)
        dog_statue_room()
    else:
        print("\nThat is not a valid "
              "input, please visit the"
              " 'Help' option if you need"
              " to see the acceptable"
              " responses.")
        game_on()


def three_statue_room1_moves(player_moves):
    if player_moves == 'forward' or player_moves == 'up' or player_moves == 'staircase':
        base_floor_room_description()
        FuggsData['location Name'] = 'Base Floor' \
                                     ' Staircase Room'
        FuggsData['location'] = 'You are in an empty ' \
                                'room. Against the north' \
                                ' side of the wall is' \
                                ' a staircase leading up.'
        global room
        room = Location(('forward', 'back',  'up', 'down', 'left', 'right'), ('look'), items, doors, second_floor_statues, puzzle_lock, lanterns)
        base_floor_room()
    elif player_moves == 'right':
        print("\nYou see three statues on a"
              " pedestal. One of a chicken, "
              "another of a bag of grain, "
              "and the last one of a fox.")
        game_on()
    elif player_moves == 'left':
        three_statue_lock()
        three_statues_room2_description()
        FuggsData['location Name'] = 'Three Statue' \
                                     ' Room Left Side'
        FuggsData['location'] = 'You are in the ' \
                                'left side of the' \
                                ' room with three' \
                                ' empty pedestals'
        room = Location(('forward', 'back', 'left',  'up', 'down', 'right'), ('look', 'take','carry', 'grab', 'haul', 'place', 'put', 'use', 'set'), items, doors, second_floor_statues, puzzle_lock, lanterns)
        three_statue_room2()
    elif player_moves == 'back' or player_moves == 'down':
        print("\nYou are met "
              "with a blank wall")
        game_on()
    else:
        print("\nThat is not a valid input,"
              " please visit the 'Help'"
              " option if you need to "
              "see the acceptable responses.")
        game_on()


def three_statue_room2_moves(player_moves):
    if player_moves == 'forward' or player_moves == 'up' or player_moves == 'staircase':
        if doors['Second floor stairs door'] == 'closed':
            print("\nYou are met"
                  " with a wall")
            game_on()
        elif doors['Second floor stairs door'] == 'open':
            FuggsData['location Name'] = 'Seven Statue Room'
            if items['torch'] == 'inventory':
                seve_statue_room_description()
                FuggsData['location'] = 'You see seven ' \
                                        'statues on the south ' \
                                        'side of the wall,' \
                                        ' each of them ' \
                                        'holding a lantern'
                global room
                room = Location(('forward', 'back',  'up', 'down', 'left', 'right'), ('look', 'light'), items, doors, second_floor_statues, puzzle_lock, lanterns)
                seven_statue_room()
            else:
                FuggsData['location'] = 'You are in' \
                                        ' a pitch black room'
                print(FuggsData['location'])
                game_on()
    elif player_moves == 'right':
        three_statue_lock()
        three_statues_room1_description()
        FuggsData['location Name'] = 'Three Statue' \
                                     ' Room Right Side'
        FuggsData['location'] = 'You are in the ' \
                                'middle of the right ' \
                                'room, with three statues ' \
                                'on your right and ' \
                                '3 empty pillars on ' \
                                'the left side ' \
                                'of the room'
        room = Location(('forward', 'back', 'up', 'down', 'left', 'right'), ('look', 'take','carry', 'grab', 'haul', 'place', 'put', 'use', 'set'), items, doors, second_floor_statues, puzzle_lock, lanterns)
        three_statue_room1()
    elif player_moves == 'left':
        print("\nYou see three "
              "statue pedestals")
        game_on()
    elif player_moves == 'back' or player_moves == 'down':
        print("\nYou are met with a blank wall")
        game_on()
    else:
        print("\nThat is not a valid input,"
              " please visit the "
              "'Help' option if you "
              "need to see the "
              "acceptable responses.")
        game_on()


def seven_statue_room_moves(player_moves):
    if items['torch'] == 'inventory':
        if player_moves == 'forward' or player_moves == 'up':
            if doors['Third floor stairs door'] == 'open':
                stone_room_description()
                FuggsData['location Name'] = 'Stone Room'
                FuggsData['location'] = "You are" \
                                        " in the room with" \
                                        " an alter and sitting" \
                                        " in it's own stand " \
                                        "is the Blood Stone"
                global room
                room = Location(('forward', 'back', 'up', 'down', 'left', 'right'), ('look', 'take', 'grab'), items, doors, second_floor_statues, puzzle_lock, lanterns)
                stone_room()
            else:
                print("\nYou are met with"
                      " a blank wall")
                game_on()
        elif player_moves == 'left':
            print("\nYou see a drawing of "
                  "three pyramids all within"
                  " a big circle, where one "
                  "pyramid is divided "
                  "into four floors.")
            print("One is divided into 2 "
                  "floors and the last one"
                  " is not divided at all.")
            game_on()
        elif player_moves == 'back' or player_moves == 'down':
            print("\nYou see seven identical gargoyle statues"
                  " each with a lantern in hand. "
                  "The middle one the biggest"
                  " of the seven.")
            game_on()
        elif player_moves == 'right':
            three_statues_room2_description()
            FuggsData['location Name'] = 'Three Statue' \
                                         ' Room Left Side'
            FuggsData['location'] = 'You are in the ' \
                                    'left side of the room ' \
                                    'with three statue pedestals'
            room = Location(('forward', 'back', 'up', 'down', 'left', 'right'), ('look', 'take', 'carry', 'grab', 'haul', 'place', 'put', 'use', 'set'), items, doors, second_floor_statues, puzzle_lock, lanterns)
            three_statue_room2()
        else:
            print("\nThat is not a valid input,"
                  " please visit the 'Help'"
                  " option if you need to "
                  "see the acceptable responses.")
            game_on()
    else:
        FuggsData['location'] = 'You are in a ' \
                                'pitch black room'
        print(FuggsData['location'])
        game_on()


def stone_room_moves(player_moves):
    if player_moves == 'forward' or player_moves == 'up':
        seve_statue_room_description()
        FuggsData['location'] = 'You see seven statues' \
                                ' on the south side ' \
                                'of the wall, each of ' \
                                'them holding a lantern'
        FuggsData['location Name'] = 'Seven' \
                                     ' Statue Room'
        global room
        room = Location(('forward', 'back', 'up', 'down', 'left', 'right'), ('look', 'light'), items, doors, second_floor_statues, puzzle_lock, lanterns)
        seven_statue_room()
    elif player_moves == 'back' or player_moves == 'down':
        print("\nYou are met with a "
              "blank wall that is slanting"
              " upward to meet at the "
              "vertex of the four walls.")
        game_on()
    elif player_moves == 'left':
        print("\nYou are met with a blank "
              "wall that is slanting "
              "upward to meet at the "
              "vertex of the four walls.")
        game_on()
    elif player_moves == 'right':
        print("\nYou are met with a blank"
              " wall that is slanting "
              "upward to meet at the "
              "vertex of the four walls.")
        game_on()
    else:
        print("\nThat is not a valid input"
              ", please visit the 'Help' "
              "option if you need to "
              "see the acceptable"
              " responses.")
        game_on()


"""
Room actions code
"""


def entrance_room_actions(player_action):
    if player_action == 'look':
        print(FuggsData['location'])
        game_on()


def storage_room_actions(player_action):
    if player_action == 'look':
        print("\nYou see a lit torch illuminated"
              " the storage room in front "
              "of you and a figure of a"
              " man behind some barrels"
              " in the right side "
              "of the room.")
        game_on()
    elif player_action == 'grab' or player_action == 'take':
        storage_room_grab_action = input("\nWhat would you like to {}? ".format(player_action)).lower()
        if storage_room_grab_action == 'torch':
            items['torch'] = 'inventory'
            print("\nYou grab the torch"
                  " off the wall and "
                  "hold it in one of "
                  "your hands.")
            game_on()
        else:
            print("\nYou can not {} that".format(player_action))
            game_on()
    elif player_action == 'pry':
        if items['Prybar'] == 'inventory':
            storage_room_pry_action = input("\nWhat do you want to use the pry bar on? ").lower()
            if storage_room_pry_action == 'stone' or storage_room_pry_action == 'moon stone' or storage_room_pry_action == 'statue':
                items['Moon Stone'] = 'inventory'
                print("\nYou successfully pry"
                      " the stone out of the"
                      " statues hand and "
                      "put it in your bag.")
                game_on()
            else:
                print("\nYou can not use "
                      "the Pry bar on that")
                game_on()
        else:
            print("\nYou do not have a pry bar")
            game_on()
    else:
        print("\nThat is not a valid "
              "action for the"
              " {}".format(FuggsData['location Name']))
        game_on()


def dog_statue_room_actions(player_action):
    if player_action == 'look':
        print("\nYou see a item covered in "
              "cobwebs on the north side"
              " of the room and a statue"
              " of a dog on the right"
              " side of the room.")
        game_on()
    elif player_action == 'grab' or player_action == 'take':
        dog_statue_room_grab_actions = input("\nWhat would you like to {}? ".format(player_action)).lower()
        if dog_statue_room_grab_actions == 'prybar' or dog_statue_room_grab_actions == 'pry bar':
            items['Prybar'] = 'inventory'
            print("\nYou dust off the"
                  " pry bar and put "
                  "it in your bag.")
            game_on()
        else:
            print("\nYou can not {} that".format(player_action))
            game_on()
    elif player_action == 'use' or player_action == 'give' or player_action == 'put' or player_action == 'place':
        if items['Moon Stone'] == 'inventory':
            dog_statue_use_action = input("\nWhat do you want to "
                                       "use the Moon Stone on? ").lower()
            if dog_statue_use_action == 'dog statue' or dog_statue_use_action == 'dog' or dog_statue_use_action == 'statue':
                items['Moon Stone'] = 'Dog Statue'
                print("\nYou place the stone"
                      " on the dog's tongue. "
                      "The wall to the left of "
                      "it begins to slide "
                      "upward, revealing "
                      "another room.")
                game_on()
            else:
                print("\nYou can not use "
                      "the Pry bar on that")
                game_on()
        else:
            print("\nYou have nothing that "
                  "you could use in your "
                  "inventory in this room")
            game_on()
    else:
        print("\nThat is not a valid action"
              " for the {}".format(FuggsData['location Name']))
        game_on()


def base_floor_staircase_room_actions(player_action):
    if player_action == 'look':
        print("\nYou see a bland room compared"
              " to the others and a staircase"
              " on the north side of the "
              "wall leading to the next floor.")
        game_on()
    else:
        print("\nThat is not a valid action for "
              "the {}".format(FuggsData['location Name']))
        game_on()


def three_statue_room1_actions(player_action):
    if player_action == 'look':
        print("T\nhere is a staircase to your north"
              " that you first came up. To"
              " your left is the doorway to"
              " the other part of the room.")
        print("To your right is the statues "
              "of the chicken, fox, and"
              " bag of grain.")
        game_on()

    elif player_action == 'grab' or player_action == 'take' or player_action == 'carry' or player_action == 'grab' or player_action == 'haul':
        three_statue_room1_grab = input("\nWhat would you like"
                                     " to {}? ".format(player_action)).lower()
        if three_statue_room1_grab == 'chicken' or three_statue_room1_grab == 'chicken statue':
            if second_floor_statues['Chicken Statue'] == 'Right' \
                                                       ' Side' and items['hands'] == 'not full':
                if puzzle_lock['Chicken Statue'] == 'lock':
                    print("\nStatue locked in place"
                          ", try resetting the statues")
                    game_on()
                else:
                    second_floor_statues['Chicken ' \
                                       'Statue'] = 'carry'
                    items['hands'] = 'full'
                    print("\nYou pick up the "
                          "statue of the chicken")
                    game_on()
            else:
                print("\nNot a valid input,"
                      " try something else or "
                      "check your spelling"
                      " room 1 error chick")
                game_on()
        elif three_statue_room1_grab == 'fox' or three_statue_room1_grab == 'fox statue':
            if second_floor_statues['Fox Statue'] == 'Right Side' and items['hands'] == 'not full':
                if puzzle_lock['Fox Statue'] == 'lock':
                    print("\nStatue locked in "
                          "place, try resetting"
                          " the statues")
                    game_on()
                else:
                    second_floor_statues['Fox Statue'] = 'carry'
                    items['hands'] = 'full'
                    print("\nYou pick up the "
                          "statue of the fox.")
                    game_on()
            else:
                print("\nNot a valid input,"
                      " try something else "
                      "or check your spelling "
                      "room 1 error fox")
                game_on()
        elif three_statue_room1_grab == 'grain' or three_statue_room1_grab == 'grain statue' or three_statue_room1_grab == 'bag of grain statue':
            if second_floor_statues['Grain Statue'] == 'Right Side' and items['hands'] == 'not full':
                if puzzle_lock['Grain Statue'] == 'lock':
                    print("\nStatue locked in"
                          " place, try"
                          " resetting the "
                          "statues")
                    game_on()
                else:
                    second_floor_statues['Grain Statue'] = 'carry'
                    items['hands'] = 'full'
                    print("\nYou pick up the "
                          "statue of the bag of grain.")
                    game_on()
            else:
                print("\nNot a valid input, try something"
                      " else or check your "
                      "spelling room 1 error grain")
                game_on()
        else:
            print("\nThe statues are on the other side")
            game_on()
    elif player_action == 'place' or player_action == 'put' or player_action == 'use' or player_action == 'set':
        if items['hands'] == 'full' and second_floor_statues['Chicken Statue'] == 'carry':
            print("\nYou place the chicken "
                  "statue down on the pedestal")
            second_floor_statues['Chicken Statue'] = 'Right Side'
            items['hands'] = 'not full'
            puzzle_lock_reset()
            game_on()
        elif items['hands'] == 'full' and second_floor_statues['Fox Statue'] == 'carry':
            print("\nYou place the Fox statue"
                  " down on the pedestal")
            second_floor_statues['Fox Statue'] = 'Right Side'
            items['hands'] = 'not full'
            puzzle_lock_reset()
            game_on()
        elif items['hands'] == 'full' and second_floor_statues['Grain Statue'] == 'carry':
            print("\nYou place the grain "
                  "statue down on the pedestal")
            second_floor_statues['Grain Statue'] = 'Right Side'
            items['hands'] = 'not full'
            puzzle_lock_reset()
            game_on()
        else:
            print("\nYou have nothing to put down")
            game_on()
    else:
        print("\nThat is not a valid action for"
              " the {}".format(FuggsData['location Name']))
        game_on()


def three_statue_room2_actions(player_action):
    if player_action == 'look':
        if doors['Second floor stairs door'] == 'open':
            print("\nThere is a staircase to your"
                  " north that you first came up. "
                  "To your left is the doorway "
                  "to the other part of the room.")
            game_on()
        else:
            print("\nTo your right is the doorway"
                  " to the other part of the "
                  "room. To your left is the "
                  "three statue pedestals")
            game_on()
    elif player_action == 'grab' or player_action == 'take' or player_action == 'carry' or player_action == 'grab' or player_action == 'haul':
        three_statue_room2_grab = input("\nWhat would you like"
                                     " to {}? ".format(player_action)).lower()
        if three_statue_room2_grab == 'chicken' or three_statue_room2_grab == 'chicken statue':
            if second_floor_statues['Chicken Statue'] == 'Left Side' and items['hands'] == 'not full':
                if puzzle_lock['Chicken Statue'] == 'lock':
                    print("\nStatue locked "
                          "in place, try "
                          "resetting the statues")
                    game_on()
                else:
                    second_floor_statues['Chicken Statue'] = 'carry'
                    items['hands'] = 'full'
                    print("\nYou pick up "
                          "the statue of the chicken")
                    game_on()
            else:
                print("\nNot a valid input, "
                      "try something else or "
                      "check your spelling "
                      "room 2 error chick")
                game_on()
        elif three_statue_room2_grab == 'fox' or three_statue_room2_grab == 'fox statue':
            if second_floor_statues['Fox Statue'] == 'Left' \
                                                   ' Side' and items['hands'] == 'not full':
                if puzzle_lock['Fox Statue'] == 'lock':
                    print("\nStatue locked in"
                          " place, try resetting"
                          " the statues")
                    game_on()
                else:
                    second_floor_statues['Fox Statue'] = 'carry'
                    items['hands'] = 'full'
                    print("\nYou pick up the statue of the fox")
                    game_on()
            else:
                print("\nNot a valid input,"
                      " try something else "
                      "or check your spelling"
                      " room 2 error fox")
                game_on()
        elif three_statue_room2_grab == 'grain' or three_statue_room2_grab == 'grain ' \
                                                                        'statue' or three_statue_room2_grab == 'bag of grain statue':
            if second_floor_statues['Grain Statue'] == 'Left' \
                                                     ' Side' and items['hands'] == 'not full':
                if puzzle_lock['Grain Statue'] == 'lock':
                    print("\nStatue locked in place,"
                          " try resetting the statues")
                    game_on()
                else:
                    second_floor_statues['Grain Statue'] = 'carry'
                    items['hands'] = 'full'
                    print("\nYou pick up the statue"
                          " of the bag of grain.")
                    game_on()
            else:
                print("\nNot a valid input, "
                      "try something else or "
                      "check your spelling "
                      "room 2 error grain")
                game_on()
        else:
            print("\nThe statues are "
                  "on the other side")
            game_on()
    elif player_action == 'place' or player_action == 'put' or player_action == 'use' or player_action == 'set':
        if items['hands'] == 'full' and second_floor_statues['Chicken' \
                                                           ' Statue'] == 'carry':
            print("\nYou place the chicken statue down on the pedestal")
            second_floor_statues['Chicken Statue'] = 'Left Side'
            items['hands'] = 'not full'
            three_statue_solution_check()
            game_on()
        elif items['hands'] == 'full' and second_floor_statues['Fox Statue'] == 'carry':
            print("\nYou place the Fox "
                  "statue down on the pedestal")
            second_floor_statues['Fox Statue'] = 'Left Side'
            items['hands'] = 'not full'
            three_statue_solution_check()
            game_on()
        elif items['hands'] == 'full' and second_floor_statues['Grain Statue'] == 'carry':
            print("\nYou place the grain"
                  " statue down on the pedestal")
            second_floor_statues['Grain Statue'] = 'Left Side'
            items['hands'] = 'not full'
            three_statue_solution_check()
            game_on()
        else:
            print("\nYou have nothing to put down")
            game_on()
    else:
        print("\nThat is not a valid action for"
              " the {}".format(FuggsData['location Name']))
        game_on()


def seven_statue_room_actions(player_action):
    if player_action == 'look':
        print("\nYou see the staircase you came up from, "
              "the seven identical gargoyle statues,"
              " and the drawing of the three "
              "pyramids in a big circle"
              " on the far wall")
        game_on()
    elif player_action == 'light' or player_action == 'ignite':
        gargoyle_light = input("\nWhich lantern would you like to light? ").lower()
        if gargoyle_light == '3' or gargoyle_light == 'third':
            print("\nThe lantern illuminates"
                  " extremely bright before "
                  "fading to a constant "
                  "dim light")
            lanterns['Lantern 3'] = 'lit'
            seven_statues_solution_check()
            game_on()
        elif gargoyle_light == '4' or gargoyle_light == 'fourth':
            print("\nThe lantern illuminates "
                  "extremely bright before"
                  " fading to a constant "
                  "dim light")
            lanterns['Lantern 4'] = 'lit'
            seven_statues_solution_check()
            game_on()
        elif gargoyle_light == '7' or gargoyle_light == 'seventh':
            print("\nThe lantern illuminates "
                  "extremely bright before "
                  "fading to a constant"
                  " dim light")
            lanterns['Lantern 7'] = 'lit'
            seven_statues_solution_check()
            game_on()
        else:
            print("\nNothing happens."
                  " Lantern doesn't even catch fire.")
            game_on()
    else:
        print("\nThat is not a valid action"
              " for the {}".format(FuggsData['location Name']))
        game_on()


def stone_room_actions(player_action):
    if player_action == 'look':
        print("\nYou are in the room with"
             " an alter and sitting in "
             "it's own stand is"
             " the Blood Stone")
        game_on()
    elif player_action == 'take' or player_action == 'grab':
        items['Blood Stone'] = 'inventory'
        doors['Desert Door'] = 'open'
        print("\nYou take the Blood Stone"
              " and put it in your"
              " bag. You also feel a"
              " rumble deep beneath you.")
        game_on()
    else:
        print("\nThat is not a valid action for the {}".format(FuggsData['location Name']))
        game_on()


"""
Puzzle Solution Check
"""


def three_statue_solution_check():
    if second_floor_statues['Chicken Statue'] == 'Left' \
                                               ' Side' and second_floor_statues['Grain Statue'] == 'Left Side' and second_floor_statues['Fox Statue'] == 'Left Side':
        doors['Second floor stairs door'] = 'open'
        print("\nThe wall on the north"
              " side of the room slides"
              " up to reveal another staircase.")
    else:
        pass


def three_statue_lock():
    if second_floor_statues['Chicken Statue'] == 'Right Side' and second_floor_statues['Grain Statue'] == 'Right Side' and second_floor_statues['Fox Statue'] == 'Left Side':
        puzzle_lock['Grain Statue'] = 'lock'
        puzzle_lock['Chicken Statue'] = 'lock'
        print('1')
    elif second_floor_statues['Chicken Statue'] == 'Left Side' and second_floor_statues['Grain Statue'] == 'Left Side' and second_floor_statues['Fox Statue'] == 'Right Side':
        puzzle_lock['Grain Statue'] = 'lock'
        puzzle_lock['Chicken Statue'] = 'lock'
        print('2')
    elif second_floor_statues['Chicken Statue'] == 'Left Side' and second_floor_statues['Grain Statue'] == 'Right Side' and second_floor_statues['Fox Statue'] == 'Left Side':
        puzzle_lock['Fox Statue'] = 'lock'
        puzzle_lock['Chicken Statue'] = 'lock'
        print('3')
    elif second_floor_statues['Chicken Statue'] == 'Right Side' and second_floor_statues['Grain Statue'] == 'Left Side' and second_floor_statues['Fox Statue'] == 'Right Side':
        puzzle_lock['Fox Statue'] = 'lock'
        puzzle_lock['Chicken Statue'] = 'lock'
        print('4')
    else:
        pass


def puzzle_lock_reset():
    if second_floor_statues['Chicken Statue'] == 'Right Side' and second_floor_statues['Grain Statue'] == 'Right Side' and second_floor_statues['Fox Statue'] == 'Right Side':
        puzzle_lock['Fox Statue'] = 'unlock'
        puzzle_lock['Chicken Statue'] = 'unlock'
        puzzle_lock['Grain Statue'] = 'unlock'
        print('5')
    elif second_floor_statues['Chicken Statue'] == 'Left Side' and second_floor_statues['Grain Statue'] == 'Left Side' and second_floor_statues['Fox Statue'] == 'Left Side':
        puzzle_lock['Fox Statue'] = 'unlock'
        puzzle_lock['Chicken Statue'] = 'unlock'
        puzzle_lock['Grain Statue'] = 'unlock'
        print('6')
    else:
        pass



def seven_statues_solution_check():
    if lanterns['Lantern 3'] == 'lit' and lanterns['Lantern 4'] == 'lit' and lanterns['Lantern 7'] == 'lit':
        doors['Third floor stairs door'] = 'open'
        print("\nThe north side of the wall"
              " slides up to reveal another staircase")


"""

Room initiate code

"""

def entrance_room():
    player_input = input('What would you like to do? ').lower()
    if player_input == '':
        print("\nPlease try another input")
        game_on()
    elif player_input == 'help':
        help()
        game_on()
    elif player_input == 'look':
        entrance_room_actions(player_input)
        game_on()
    else:
        current_location = FuggsData['location Name']
        if FuggsData['location Name'] == 'Entrance Room':
            entrance_room_move_and_actions(player_input)


def storage_room():
    player_input = input('What would you like to do? ').lower()
    if player_input == '':
        print("\nPlease try another input")
        game_on()
    elif player_input == 'help':
        help()
        game_on()
    elif player_input == 'look':
        storage_room_actions(player_input)
    else:
        if FuggsData['location Name'] == 'Storage Room':
            storage_room_move_and_actions(player_input)


def dog_statue_room():
    player_input = input('What would you like to do? ').lower()
    if player_input == '':
        print("\nPlease try another input")
    elif player_input == 'help':
        help()
    elif player_input == 'look':
        dog_statue_room_actions(player_input)
    else:
        if FuggsData['location Name'] == 'Dog Statue Room':
            dog_statue_room_move_and_actions(player_input)


def base_floor_room():
    player_input = input('What would you like to do? ').lower()
    if player_input == '':
        print("\nPlease try another input")
    elif player_input == 'help':
        help()
    elif player_input == 'look':
        base_floor_staircase_room_actions(player_input)
    else:
        if FuggsData['location Name'] == 'Base Floor Staircase Room':
            base_floor_staircase_room_move_and_actions(player_input)


def three_statue_room1():
    player_input = input('What would you like to do? ').lower()
    if player_input == '':
        print("\nPlease try another input")
    elif player_input == 'help':
        help()
    elif player_input == 'look':
        three_statue_room1_actions(player_input)
    else:
        if FuggsData['location Name'] == 'Three Statue Room Right Side':
            three_statue_room1_move_and_actions(player_input)


def three_statue_room2():
    player_input = input('What would you like to do? ').lower()
    if player_input == '':
        print("\nPlease try another input")
        game_on()
    elif player_input == 'help':
        help()
        game_on()
    elif player_input == 'look':
        three_statue_room2_actions(player_input)
    else:
        if FuggsData['location Name'] == 'Three Statue Room Left Side':
            three_statue_room2_move_and_actions(player_input)


def seven_statue_room():
    player_input = input('What would you like to do? ').lower()
    if player_input == '':
        print("\nPlease try another input")
        game_on()
    elif player_input == 'help':
        help()
        game_on()
    elif player_input == 'look':
        seven_statue_room_actions(player_input)
    else:
        if FuggsData['location Name'] == 'Seven Statue Room':
            seven_statue_room_move_and_actions(player_input)


def stone_room():
    player_input = input('What would you like to do? ').lower()
    if player_input == '':
        print("\nPlease try another input")
        game_on()
    elif player_input == 'help':
        help()
        game_on()
    elif player_input == 'look':
        stone_room()
    else:
        if FuggsData['location Name'] == 'Stone Room':
            stone_room_move_and_actions(player_input)


def start_path_a():
    PathALore.chapter1_path_a()
    floor_puzzle_pt1()


def game_on():
    player_input = input("\nWhat would you like to do now? ").lower()
    if player_input == "help":
        help()
        game_on()
    elif player_input == "":
        print("\nPlease try again.")
        game_on()
    else:
        current_location_name = FuggsData['location Name']
        if current_location_name == 'Entrance Room':
            entrance_room_move_and_actions(player_input)
        elif current_location_name == 'Storage Room':
            storage_room_move_and_actions(player_input)
        elif current_location_name == 'Dog Statue Room':
            dog_statue_room_move_and_actions(player_input)
        elif current_location_name == 'Base Floor Staircase Room':
            base_floor_staircase_room_move_and_actions(player_input)
        elif current_location_name == 'Three Statue Room Right Side':
            three_statue_room1_move_and_actions(player_input)
        elif current_location_name == "Three Statue Room Left Side":
            three_statue_room2_move_and_actions(player_input)
        elif current_location_name == 'Seven Statue Room':
            seven_statue_room_move_and_actions(player_input)
        elif current_location_name == 'Stone Room':
            stone_room_move_and_actions(player_input)
        else:
            print('error')

    if FuggsData['health'] < 1:
        pass
    elif FuggsData['location Name'] == 'Outside Pyramid':
        PathALore.path_a_return()
        FuggsData['health'] = 0
    else:
        game_on()


