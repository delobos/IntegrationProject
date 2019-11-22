

FuggsData = {'name': "Fuggs", 'health':100, 'location Name': 'Pyramid Entrance', 'location': "You are at the entrance of a pyramid."}


class Location:
    def __init__(self, moves, actions, items):
        self.moves = moves
        self.actions = actions
        self.items = items
        self.description = "At the entrace of this pyramid you can barely make out the dimly lit room inside"

def help():
    print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")
    print("You will be exploring places and interacting with items in the game.\n")
    print("Please use words like 'forward', 'up, 'left', 'right', 'down', and 'back' for movement inside a structure.\n")
    print("Every time you step into a room you will be located in the center facing north or the 'forward'/ 'up' direction\n")
    print("Different rooms have different actions you can take. They are all one word actions, where it may ask what do you want to use that action on.\n")
    print("To see a description of where you are in a room or an area, just type 'look', this also acts as an investigate in certain rooms..\n")
    print("To see this introductory list again, type 'help'.\n")
    print("When you are ready to continue, press the ENTER key.\n")
    input()
    print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")

def floorPuzzlePt1():
   # help()
    print("\nYou step into this musty dimly lit room. Right before the end of the entry hallway, you see a large arrow pointing ahead into the room")
    print("The floor in front of you is a stone tile floor, decorated with figures of animals, objects, and vegetation.")
    print("At the mouth of this room sits four stones in a row, on each one from left to right is a Rabbit, Sun, Leaf, and a Hawk")
    print("Which one would you like to step on? or does it even matter?")
    floorPuzzleloop1 = 0
    while FuggsData['health'] > 1 and floorPuzzleloop1 == 0:
        floorPuzzleChoice = input("\nRabbit \nSun \nLeaf \nHawk ").lower()
        if floorPuzzleChoice[0] == 'r':
            print("You hear some mechanisms moving in the walls before feeling a sharp pain in your side as you jump back towards the entrance and off the stone tile.")
            print("Looking down you see a dart with red feathered tail sticking out of your side")
            FuggsData['health'] -= 25
            print("You have ", FuggsData['health'], " health left")
            FuggsDeathCheck()
            continue
        elif floorPuzzleChoice[0] == 's':
            print("You hear a click as the tile slides into the floor and stays down.")
            floorPuzzleloop1 += 1
            floorPuzzlePt2()
        elif floorPuzzleChoice[0] == 'l':
            print("You hear some mechanisms moving in the walls before feeling a sharp pain in your side as you jump back towards the entrance and off the stone tile.")
            print("Looking down you see a dart with red feathered tail sticking out of your side")
            FuggsData['health'] -= 25
            print("You have ", FuggsData['health'], " health left")
            FuggsDeathCheck()
            continue
        elif floorPuzzleChoice[0] == 'h':
            print("You hear some mechanisms moving in the walls before feeling a sharp pain in your side as you jump back towards the entrance and off the stone tile.")
            print("Looking down you see a dart with red feathered tail sticking out of your side")
            FuggsData['health'] -= 25
            print("You have ", FuggsData['health'], " health left")
            FuggsDeathCheck()
            continue
        else:
            print("Please select one of the options")
            floorPuzzleChoice = input("Rabbit \nSun \nLeaf \nHawk ").lower()
            continue

def floorPuzzlePt2():
    floorPuzzleloop2 = 0
    while FuggsData['health'] > 1 and floorPuzzleloop2 == 0:
        floorPuzzleChoice2 = input("\nHawk \nRabbit \nSun \nLeaf ").lower()
        if floorPuzzleChoice2[0] == 'h':
            print("You hear some mechanisms moving in the walls before feeling a sharp pain in your side as you jump back towards the entrance and off the stone tile.")
            print("Looking down you see a dart with red feathered tail sticking out of your side")
            FuggsData['health'] -= 25
            print("You have ", FuggsData['health'], " health left")
            FuggsDeathCheck()
            continue
        elif floorPuzzleChoice2[0] == 'r':
            print("You hear some mechanisms moving in the walls before feeling a sharp pain in your side as you jump back towards the entrance and off the stone tile.")
            print("Looking down you see a dart with red feathered tail sticking out of your side")
            FuggsData['health'] -= 25
            print("You have ", FuggsData['health'], " health left")
            FuggsDeathCheck()
            continue
        elif floorPuzzleChoice2[0] == 's':
            print("You hear some mechanisms moving in the walls before feeling a sharp pain in your side as you jump back towards the entrance and off the stone tile.")
            print("Looking down you see a dart with red feathered tail sticking out of your side")
            FuggsData['health'] -= 25
            print("You have ", FuggsData['health'], " health left")
            FuggsDeathCheck()
            continue
        elif floorPuzzleChoice2[0] == 'l':
            print("You hear a click as the tile slides into the floor and stays down.")
            floorPuzzlePt3()
            floorPuzzleloop2 += 1
        else:
            print("Please select one of the options")
            floorPuzzleChoice2 = input("Rabbit \nSun \nLeaf \nHawk ").lower()
            continue

def floorPuzzlePt3():
    floorPuzzleloop3 = 0
    while FuggsData['health'] > 1 and floorPuzzleloop3 == 0:
        floorPuzzleChoice3 = input("\nHawk \nRabbit \nSun \nLeaf ").lower()
        if floorPuzzleChoice3[0] == 'h':
            print("You hear some mechanisms moving in the walls before feeling a sharp pain in your side as you jump back towards the entrance and off the stone tile.")
            print("Looking down you see a dart with red feathered tail sticking out of your side")
            FuggsData['health'] -= 25
            print("You have ", FuggsData['health'], " health left")
            FuggsDeathCheck()
            continue
        elif floorPuzzleChoice3[0] == 's':
            print("You hear some mechanisms moving in the walls before feeling a sharp pain in your side as you jump back towards the entrance and off the stone tile.")
            print("Looking down you see a dart with red feathered tail sticking out of your side")
            FuggsData['health'] -= 25
            print("You have ", FuggsData['health'], " health left")
            FuggsDeathCheck()
            continue
        elif floorPuzzleChoice3[0] == 'l':
            print("You hear some mechanisms moving in the walls before feeling a sharp pain in your side as you jump back towards the entrance and off the stone tile.")
            print("Looking down you see a dart with red feathered tail sticking out of your side")
            FuggsData['health'] -= 25
            print("You have ", FuggsData['health'], " health left")
            FuggsDeathCheck()
            continue
        elif floorPuzzleChoice3[0] == 'r':
            print("You hear a click as the tile slides into the floor and stays down.")
            floorPuzzleloop3 += 1
            floorPuzzlePt4()

        else:
            print("Please select one of the options")
            floorPuzzleChoice3 = input("Rabbit \nSun \nLeaf \nHawk ").lower()
            continue

def floorPuzzlePt4():
    floorPuzzleloop4 = 0
    while FuggsData['health'] > 1 and floorPuzzleloop4 == 0:
        floorPuzzleChoice2 = input("\nHawk \nRabbit \nSun \nLeaf ").lower()
        if floorPuzzleChoice2[0] == 'l':
            print("You hear some mechanisms moving in the walls before feeling a sharp pain in your side as you jump back towards the entrance and off the stone tile.")
            print("Looking down you see a dart with red feathered tail sticking out of your side")
            FuggsData['health'] -= 25
            print("You have ", FuggsData['health'], " health left")
            FuggsDeathCheck()
            continue
        elif floorPuzzleChoice2[0] == 'r':
            print(
                "You hear some mechanisms moving in the walls before feeling a sharp pain in your side as you jump back towards the entrance and off the stone tile.")
            print("Looking down you see a dart with red feathered tail sticking out of your side")
            FuggsData['health'] -= 25
            print("You have ", FuggsData['health'], " health left")
            FuggsDeathCheck()
            continue
        elif floorPuzzleChoice2[0] == 's':
            print(
                "You hear some mechanisms moving in the walls before feeling a sharp pain in your side as you jump back towards the entrance and off the stone tile.")
            print("Looking down you see a dart with red feathered tail sticking out of your side")
            FuggsData['health'] -= 25
            print("You have ", FuggsData['health'], " health left")
            FuggsDeathCheck()
            continue
        elif floorPuzzleChoice2[0] == 'h':
            print("\nYou hear a click as the tile slides into the floor and stays down.")
            print("You then hear mechanisms all around you as a portion of the wall in front of you and to your right slide up revealing two rooms.")
            print("The door to the pyramid behind you closes, leaving a giant stone wall in its place")
            FuggsData['location Name'] = 'Entrance Room'
            FuggsData['location'] = 'You are in the entrance room of the pyramid'
            doors['Desert Door'] = 'closed'
            EntranceRoom()
            floorPuzzleloop4 += 1
        else:
            print("Please select one of the options")
            floorPuzzleChoice = input("Rabbit \nSun \nLeaf \nHawk ").lower()
            continue

def FuggsDeathCheck():
    if FuggsData['health'] < 1:
        print("Too badly inured, you feel yourself become weaker as you fall over dead.")
        print("Maybe next time will be better")
        print("But then, you wake up to the sound of someone yelling 'INTRUDER!'")
    else:
        pass

"""
Room descriptions
"""
def DogStatueRoomDescription():
    print("\nYou enter the room and are greeted to the sight of cobwebs and dust littering the room.")
    print("A large dog shaped statue sits on the right side of the room against the wall")

def EntranceRoomDescription():
    print("\nYou are in the first room you came into when coming into the pyramid. A empty room besides the figures littering the stone tiles on the floor.")

def StorageRoomDescription():
    print("\nYou enter into what looks like a storage room. Barrels sit all over the room, as does various pieces of furniture.")

def baseFloorRoomDescription():
    print("\nYou enter an empty room. The air smells damp and musty. On the north side of the room sits a staricase that leads up to the second floor.")

def threeStatueRoom1Description():
    print("You enter the right side of the room with a staircase to the north, statue pedestals on the right, and the other part of the room on the left passed a doorway.")

def threeStatueRoom2Description():
    print("You are in a room with three statue pedestals on the left side of the room and a door way on the right leading to the right side of the room.")

def SevenStatueRoomDescription():
    print("You enter a large empty room except for the seven gargoyle statues each with one are held outright holding a lantern")

def stoneRoomDescription():
    print("You are in a room where all the walls of the pyramid meet at a point above you. In the center of the room sits an alter")

"""
Items dictionary and global class Location call
"""
items = {'hands':'empty','torch': 'wall', 'Prybar': 'Dog Room', 'Moon Stone': 'Statue hand', 'Chicken Statue': 'Right Side', 'Fox Statue': 'Right Side', 'Grain Statue': 'Right Side', 'Blood Stone': "alter"}
doors = {"Desert Door":"open", 'Second floor stairs door': 'closed', 'Third floor stairs door': 'closed'}
secondFloorStatues = {'Chicken Statue': 'Right Side', 'Fox Statue': 'Right Side', 'Grain Statue': 'Right Side'}
puzzleLock = {'Chicken Statue': 'unlock','Fox Statue': 'unlock', 'Grain Statue': 'unlock'}
lanterns = {'Lantern 1': 'unlit','Lantern 2': 'unlit','Lantern 3': 'unlit', 'Lantern 4': 'unlit', 'Lantern 5': 'unlit', 'Lantern 6': 'unlit','Lantern 7': 'unlit'}


Room = Location(('forward','back', 'up', 'down', 'left', 'right'), ('look'), items)

"""
Room possible moves and actions
"""

def entranceRoom_MoveAndActions(player_input):
    if player_input in Room.moves:
            entranceRoomMoves(player_input)
    elif player_input in Room.actions:
        entranceRoomActions(player_input)
    else:
        print("Not a valid input in this room")
        gameOn()

def storageRoom_MoveAndActions(player_input):
    if player_input in Room.moves:
            storageRoomMoves(player_input)
    elif player_input in Room.actions:
        storageRoomActions(player_input)
    else:
        print("Not a valid input in this room")
        gameOn()

def DogStatueRoom_MoveAndActions(player_input):
    if player_input in Room.moves:
        DogStatueRoomMoves(player_input)
    elif player_input in Room.actions:
        DogStatueRoomActions(player_input)
    else:
        print("Not a valid input in this room")
        gameOn()

def baseFloorStaircaseRoom_MoveAndActions(player_input):
    if player_input in Room.moves:
        baseFloorStaircaseRoomMoves(player_input)
    elif player_input in Room.actions:
        baseFloorStaircaseRoomActions(player_input)
    else:
        print("Not a valid input in this room")
        gameOn()

def threeStatueRoom1_MoveAndActions(player_input):
    if player_input in Room.moves:
        threeStatueRoom1Moves(player_input)
    elif player_input in Room.actions:
        threeStatueRoom1Actions(player_input)
    else:
        print("Not a valid input in this room")
        gameOn()

def threeStatueRoom2_MoveAndActions(player_input):
    if player_input in Room.moves:
        threeStatueRoom2Moves(player_input)
    elif player_input in Room.actions:
        threeStatueRoom2Actions(player_input)
    else:
        print("Not a valid input in this room")
        gameOn()

def sevenStatueRoom_MoveAndActions(player_input):
    if player_input in Room.moves:
        sevenStatueRoomMoves(player_input)
    elif player_input in Room.actions:
        sevenStatueRoomActions(player_input)
    else:
        print("Not a valid input in this room")
        gameOn()

def stoneRoom_MoveAndActions(player_input):
    if player_input in Room.moves:
        stoneRoomMoves(player_input)
    elif player_input in Room.actions:
        stoneRoomActions(player_input)
    else:
        print("Not a valid input in this room")
        gameOn()

"""
Room moves code
"""

def entranceRoomMoves(playerMoves):
    if playerMoves == 'forward' or playerMoves == 'up':
        DogStatueRoomDescription()
        FuggsData['location Name'] = 'Dog Statue Room'
        FuggsData['location'] = "You are in an old dusty room. A large statue of a dog on the right side of the room"
        global Room
        Room = Location(('forward', 'back', 'up', 'down', 'left', 'right'), ('look', 'grab', 'take', 'use', 'place', 'put', 'give'), items)
        DogStatueRoom()
    elif playerMoves == 'back' or playerMoves == 'down':
        if doors['Desert Door'] == 'open':
            print("You are back outside!")
            FuggsData['location Name'] = 'Outside Pyramid'
            FuggsData['location'] = 'You are at the entrance of a pyramid.'
        else:
            print("You can't go back outside with the entrance blocked")
            gameOn()
    elif playerMoves == 'right':
        StorageRoomDescription()
        FuggsData['location Name'] = 'Storage Room'
        FuggsData['location'] = 'You are in a storage room full of furniture, barrels, and crates.'
        Room = Location(('forward', 'back', 'left','up', 'down', 'right'), ('look', 'grab', 'take', 'pry'), items)
        StorageRoom()
    elif playerMoves == 'left':
        print("You see a big plain wall")
        gameOn()
    else:
        print("That is not a valid input, please visit the 'Help' option if you need to see the acceptable responses.")
        gameOn()

def storageRoomMoves(playerMoves):
    if playerMoves == 'forward' or playerMoves == 'up':
        print("You walk up to the only source of light in this room, a lit torch.")
        gameOn()
    elif playerMoves == 'back' or playerMoves == 'down':
        print("You search through some barrels but find nothing of interest")
        gameOn()
    elif playerMoves == 'right':
        print("You rummage through some items and find a statue of a human man, a little over 4 feet tall with both of its arms outstreached slightly.")
        print("One hand is balled into a fist and the other has an open palm facing upward, and embedded in its palm is a crescent moon shaped stone.")
        gameOn()
    elif playerMoves == 'left':
        EntranceRoomDescription()
        FuggsData['location Name'] = 'Entrance Room'
        FuggsData['location'] = 'The entrance room with the figures on the floor'
        Room = Location(('forward', 'back', 'up', 'down', 'left', 'right'), ('look'), items)
        EntranceRoom()
    else:
        print("That is not a valid input, please visit the 'Help' option if you need to see the acceptable responses.")
        gameOn()

def DogStatueRoomMoves(playerMoves):
    if playerMoves == 'forward' or playerMoves == 'up':
        print("You see a old rusted pry bar covered in cobwebs laying against the wall.")
        gameOn()
    elif playerMoves == 'back' or playerMoves == 'down':
        EntranceRoomDescription()
        FuggsData['location Name'] = 'Entrance Room'
        FuggsData['location'] = 'The entrance room with the figures on the floor'
        global Room
        Room = Location(('forward','back', 'up', 'down', 'left', 'right'), ('look'), items)
        EntranceRoom()
    elif playerMoves == 'right':
        if items['Moon Stone'] == 'Dog Statue':
            baseFloorRoomDescription()
            FuggsData['location Name'] = 'Base Floor Staircase Room'
            FuggsData['location'] = 'You are in an empty room. Against the north side of the wall is a staircase leading up.'
            Room = Location(('forward', 'back',  'up', 'down', 'left', 'right'), ('look'), items)
            baseFloorRoom()
        else:
            print("You see a statue of a dog, in the sitting position and it's toungue out  as if it was panting.")
            print("Sitting on it's tongue is a hole in the shape of a crescent moon")
            gameOn()
    elif playerMoves == 'left':
        print("You see a big plain wall")
        gameOn()
    else:
        print("That is not a valid input, please visit the 'Help' option if you need to see the acceptable responses.")
        gameOn()

def baseFloorStaircaseRoomMoves(playerMoves):
    if playerMoves == 'forward' or playerMoves == 'up' or playerMoves == 'staircase':
        print("You climb up the stairs onto the next floor")
        threeStatueRoom1Description()
        FuggsData['location'] = 'You are in the middle of the right rooms, with three statues on your right and 3 empty pillars on the left side of the room'
        FuggsData['location Name'] = 'Three Statue Room Right Side'
        global Room
        Room = Location(('forward','back', 'up', 'down', 'left', 'right'), ('look', 'take', 'carry', 'grab', 'haul', 'place', 'put', 'use', 'set'), items)
        threeStatueRoom1()
    elif playerMoves == 'back' or playerMoves == 'down':
        print("You are met with a plain wall and nothing of interest to see.")
        gameOn()
    elif playerMoves == 'right':
        print("You are met with a plain wall and nothing of interest to see.")
        gameOn()
    elif playerMoves == 'left':
        DogStatueRoomDescription()
        FuggsData['location Name'] = 'Dog Statue Room'
        FuggsData['location'] = "The entrance of the room with small piles of gold, a random assortment of jewels, and a large statue of a dog on the right side of the room"
        Room = Location(('forward', 'back', 'left', 'up', 'down', 'right'), ('look', 'grab', 'take', 'use', 'place', 'put', 'give'), items)
        DogStatueRoom()
    else:
        print("That is not a valid input, please visit the 'Help' option if you need to see the acceptable responses.")
        gameOn()

def threeStatueRoom1Moves(playerMoves):
    if playerMoves == 'forward' or playerMoves == 'up' or playerMoves == 'staircase':
        baseFloorRoomDescription()
        FuggsData['location Name'] = 'Base Floor Staircase Room'
        FuggsData['location'] = 'You are in an empty room. Against the north side of the wall is a staircase leading up.'
        global Room
        Room = Location(('forward', 'back',  'up', 'down', 'left', 'right'), ('look'), items)
        baseFloorRoom()
    elif playerMoves == 'right':
        print("You see three statues on a pedestal. One of a chicken, another of a bag of grain, and the last one of a fox.")
        gameOn()
    elif playerMoves == 'left':
        threeStatueRoom2Description()
        FuggsData['location Name'] = 'Three Statue Room Left Side'
        FuggsData['location'] = 'You are in the left side of the room with three empty pedestals'
        Room = Location(('forward', 'back', 'left',  'up', 'down', 'right'), ('look', 'take','carry', 'grab', 'haul', 'place', 'put', 'use', 'set'), items)
        threeStatueRoom2()
    elif playerMoves == 'back' or playerMoves == 'down':
        print("You are met with a blank wall")
        gameOn()
    else:
        print("That is not a valid input, please visit the 'Help' option if you need to see the acceptable responses.")
        gameOn()

def threeStatueRoom2Moves(playerMoves):
    if playerMoves == 'forward' or playerMoves == 'up' or playerMoves == 'staircase':
        if doors['Second floor stairs door'] == 'closed':
            print("You are met with a wall")
            gameOn()
        elif doors['Second floor stairs door'] == 'open':
            FuggsData['location Name'] = 'Seven Statue Room'
            if items['torch'] == 'inventory':
                SevenStatueRoomDescription()
                FuggsData['location'] = 'You see seven statues on the south side of the wall, each of them holding a lantern'
                global Room
                Room = Location(('forward', 'back',  'up', 'down', 'left', 'right'), ('look', 'light'), items)
                sevenStatueRoom()
            else:
                FuggsData['location'] = 'You are in a pitch black room'
                print(FuggsData['location'])
                gameOn()
    elif playerMoves == 'right':
        threeStatueRoom1Description()
        FuggsData['location Name'] = 'Three Statue Room Right Side'
        FuggsData['location'] = 'You are in the middle of the right room, with three statues on your right and 3 empty pillars on the left side of the room'
        Room = Location(('forward', 'back', 'up', 'down', 'left', 'right'), ('look', 'take','carry', 'grab', 'haul', 'place', 'put', 'use', 'set'), items)
        threeStatueRoom1()
    elif playerMoves == 'left':
        print("You see three statue pedestals")
        gameOn()
    elif playerMoves == 'back' or playerMoves == 'down':
        print("You are met with a blank wall")
        gameOn()
    else:
        print("That is not a valid input, please visit the 'Help' option if you need to see the acceptable responses.")
        gameOn()

def sevenStatueRoomMoves(playerMoves):
    if items['torch'] == 'inventory':
        if playerMoves == 'forward' or playerMoves == 'up':
            if doors['Third floor stairs door'] == 'open':
                stoneRoomDescription()
                FuggsData['location Name'] = 'Stone Room'
                FuggsData['location'] = "You are in the room with an alter and sitting in it's own stand is the Blood Stone"
                global Room
                Room = Location(('forward', 'back', 'up', 'down', 'left', 'right'), ('look', 'take', 'grab'), items)
                stoneRoom()
            else:
                print("You are met with a blank wall")
                gameOn()
        elif playerMoves == 'left':
            print("You see a drawing of three pyramids all within a big circle, where one pyramid is divided into four floors.")
            print("One is divided into 2 floors and the last one is not divided at all.")
            gameOn()
        elif playerMoves == 'back' or playerMoves == 'down':
            print("You see seven identical gargoyle statues each with a lantern in hand. The middle one the biggest of the seven.")
            gameOn()
        elif playerMoves == 'right':
            threeStatueRoom2Description()
            FuggsData['location Name'] = 'Three Statue Room Left Side'
            FuggsData['location'] = 'You are in the left side of the room with three statue pedestals'
            Room = Location(('forward', 'back', 'up', 'down', 'left', 'right'), ('look', 'take', 'carry', 'grab', 'haul', 'place', 'put', 'use', 'set'), items)
            threeStatueRoom2()
        else:
            print("That is not a valid input, please visit the 'Help' option if you need to see the acceptable responses.")
            gameOn()
    else:
        FuggsData['location'] = 'You are in a pitch black room'
        print(FuggsData['location'])
        gameOn()

def stoneRoomMoves(playerMoves):
    if playerMoves == 'forward' or playerMoves == 'up':
        SevenStatueRoomDescription()
        FuggsData['location'] = 'You see seven statues on the south side of the wall, each of them holding a lantern'
        FuggsData['location Name'] = 'Seven Statue Room'
        global Room
        Room = Location(('forward', 'back', 'up', 'down', 'left', 'right'), ('look', 'light'), items)
        sevenStatueRoom()
    elif playerMoves == 'back' or playerMoves == 'down':
        print("You are met with a blank wall that is slanting upward to meet at the vertex of the four walls.")
        gameOn()
    elif playerMoves == 'left':
        print("You are met with a blank wall that is slanting upward to meet at the vertex of the four walls.")
        gameOn()
    elif playerMoves == 'right':
        print("You are met with a blank wall that is slanting upward to meet at the vertex of the four walls.")
        gameOn()
    else:
        print("That is not a valid input, please visit the 'Help' option if you need to see the acceptable responses.")
        gameOn()

"""
Room actions code
"""

def entranceRoomActions(playerAction):
    if playerAction == 'look':
        print(FuggsData['location'])
        gameOn()

def storageRoomActions(playerAction):
    if playerAction == 'look':
        print("You see a lit torch illuminated the storage room in front of you and a figure of a man behind some barrels in the right side of the room.")
        gameOn()
    elif playerAction == 'grab' or playerAction == 'take':
        storageRoomGrabAction = input("What would you like to {}? ".format(playerAction)).lower()
        if storageRoomGrabAction == 'torch':
            items['torch'] = 'inventory'
            items['hands'] = 'not full'
            print("You grab the torch off the wall and hold it in one of your hands.")
            gameOn()
        else:
            print("You can not {} that".format(playerAction))
            gameOn()
    elif playerAction == 'pry':
        if items['Prybar'] == 'inventory':
            storageRoomPryAction = input("What do you want to use the prybar on? ").lower()
            if storageRoomPryAction == 'stone' or storageRoomPryAction == 'moon stone' or storageRoomPryAction == 'statue':
                items['Moon Stone'] = 'inventory'
                print("You successfully pry the stone out of the statues hand and put it in your bag.")
                gameOn()
            else:
                print("You can not use the Pry bar on that")
                gameOn()
        else:
            print("You do not have a pry bar")
            gameOn()
    else:
        print("That is not a valid action for the {}".format(FuggsData['location Name']))
        gameOn()

def DogStatueRoomActions(playerAction):
    if playerAction == 'look':
        print("You see a item covered in cobwebs on the north side of the room and a statue of a dog on the right side of the room.")
        gameOn()
    elif playerAction == 'grab' or playerAction == 'take':
        DogStatueRoomGrabActions = input("What would you like to {}? ".format(playerAction)).lower()
        if DogStatueRoomGrabActions == 'prybar' or DogStatueRoomGrabActions == 'pry bar':
            items['Prybar'] = 'inventory'
            print("You dust off the pry bar and put it in your bag.")
            gameOn()
        else:
            print("You can not {} that".format(playerAction))
            gameOn()
    elif playerAction == 'use' or playerAction == 'give' or playerAction == 'put' or playerAction == 'place':
        if items['Moon Stone'] == 'inventory':
            dogStatueUseAction = input("What do you want to use the Moon Stone on? ").lower()
            if dogStatueUseAction == 'dog statue' or dogStatueUseAction == 'dog' or dogStatueUseAction == 'statue':
                items['Moon Stone'] = 'Dog Statue'
                print("You place the stone on the dog's tongue. The wall to the left of it begins to slide upward, revealing another room.")
                gameOn()
            else:
                print("You can not use the Pry bar on that")
                gameOn()
        else:
            print("You have nothing that you could use in your inventory in this room")
            gameOn()
    else:
        print("That is not a valid action for the {}".format(FuggsData['location Name']))
        gameOn()

def baseFloorStaircaseRoomActions(playerAction):
    if playerAction == 'look':
        print("You see a bland room compared to the others and a staircase on the north side of the wall leading to the next floor.")
        gameOn()
    else:
        print("That is not a valid action for the {}".format(FuggsData['location Name']))
        gameOn()

def threeStatueRoom1Actions(playerAction):
    if playerAction == 'look':
        print("There is a staircase to your north that you first came up. To your left is the doorway to the other part of the room.")
        print("To your right is the statues of the chicken, fox, and bag of grain.")
        gameOn()
    elif playerAction == 'grab' or playerAction == 'take' or playerAction == 'carry' or playerAction == 'grab' or playerAction == 'haul':
        threeStatueRoom1grab = input("What would you like to {}? ".format(playerAction)).lower()
        if secondFloorStatues['Chicken Statue'] == 'Right Side' and secondFloorStatues['Fox Statue'] == 'Right Side' and secondFloorStatues['Grain Statue'] == 'Right Side' and items['hands'] == 'not full':
            if threeStatueRoom1grab == 'chicken' or threeStatueRoom1grab == 'chicken statue':
                secondFloorStatues['Chicken Statue'] = 'carry'
                items['hands'] = 'full'
                print("You pick up the statue of the chicken")
                gameOn()
            elif threeStatueRoom1grab == 'fox' or threeStatueRoom1grab == 'fox statue':
                secondFloorStatues['Fox Statue'] = 'carry'
                items['hands'] = 'full'
                print("You pick up the statue of the fox")
                puzzleLock['Chicken Statue'] = 'lock'
                puzzleLock['Grain Statue'] = 'lock'
                gameOn()
            elif threeStatueRoom1grab == 'grain' or threeStatueRoom1grab == 'grain statue' or threeStatueRoom1grab == 'bag of grain statue':
                secondFloorStatues['Grain Statue'] = 'carry'
                items['hands'] = 'full'
                print("You pick up the statue of the bag of grain")
                puzzleLock['Chicken Statue'] = 'lock'
                puzzleLock['Fox Statue'] = 'lock'
                gameOn()
            else:
                print("Error 1")
                gameOn()
        elif secondFloorStatues['Chicken Statue'] == 'Right Side' and secondFloorStatues['Fox Statue'] == 'Right Side' or secondFloorStatues['Grain Statue'] == 'Right Side' and items['hands'] == 'not full':
            if puzzleLock['Chicken Statue'] == 'lock' or puzzleLock['Grain Statue'] == 'lock' or puzzleLock['Fox Statue'] == 'lock':
                print("The remaining statues are locked in place. Maybe try a different order?")
                gameOn()
            elif puzzleLock['Chicken Statue']
            if threeStatueRoom1grab == 'fox' or threeStatueRoom1grab == 'fox statue':
                secondFloorStatues['Fox Statue'] = 'carry'
                items['hands'] = 'full'
                print("You pick up the statue of the fox")
                gameOn()
            elif threeStatueRoom1grab == 'grain' or threeStatueRoom1grab == 'grain statue' or threeStatueRoom1grab == 'bag of grain statue':
                secondFloorStatues['Grain Statue'] = 'carry'
                items['hands'] = 'full'
                print("You pick up the statue of the bag of grain")
                gameOn()
            else:
                print("Error 2")
                gameOn()
        elif secondFloorStatues['Grain Statue'] == 'Right Side' or secondFloorStatues['Fox Statue'] == 'Right Side' and secondFloorStatues['hands'] == 'full':
            if threeStatueRoom1grab == 'grain' or threeStatueRoom1grab == 'grain statue' or threeStatueRoom1grab == 'bag of grain statue':
                secondFloorStatues['Grain Statue'] = 'carry'
                items['hands'] = 'full'
                print("You pick up the statue of the bag of grain")
                gameOn()
            elif threeStatueRoom1grab == 'fox' or threeStatueRoom1grab == 'fox statue':
                secondFloorStatues['Fox Statue'] = 'carry'
                items['hands'] = 'full'
                print("You pick up the statue of the fox")
                gameOn()
            else:
                print("Error 3")
                gameOn()
        elif secondFloorStatues['Chicken Statue'] == 'Right Side' and
        else:
            print("The statues are on the other side")
            gameOn()
    elif playerAction == 'place' or playerAction == 'put' or playerAction == 'use' or playerAction == 'set':
        if items['hands'] == 'full' and secondFloorStatues['Chicken Statue'] == 'carry':
            print("You place the chicken statue down on the pedestal")
            secondFloorStatues['Chicken Statue'] = 'Right Side'
            items['hands'] = 'not full'
            gameOn()
        elif items['hands'] == 'full' and items['Fox Statue'] == 'carry':
            print("You place the Fox statue down on the pedestal")
            secondFloorStatues['Fox Statue'] = 'Right Side'
            items['hands'] = 'not full'
            gameOn()
        elif items['hands'] == 'full' and items['Grain Statue'] == 'carry':
            print("You place the chicken statue down on the pedestal")
            secondFloorStatues['Grain Statue'] = 'Right Side'
            items['hands'] = 'not full'
            gameOn()
        else:
                print("You have nothing to put down")
                gameOn()
    else:
        print("That is not a valid action for the {}".format(FuggsData['location Name']))
        gameOn()

def threeStatueRoom2Actions(playerAction):
    if playerAction == 'look':
        if doors['Second floor stairs door'] == 'open':
            print("There is a staircase to your north that you first came up. To your left is the doorway to the other part of the room.")
            gameOn()
        else:
            print("To your right is the doorway to the other part of the room. To your left is the three statue pedestals")
            gameOn()
    elif playerAction == 'grab' or playerAction == 'take' or playerAction == 'carry' or playerAction == 'grab' or playerAction == 'haul':
        threeStatueRoom2grab = input("What would you like to {}? ".format(playerAction)).lower()
        if secondFloorStatues['Chicken Statue'] == 'Left Side' and items['hands'] != 'full':
            if threeStatueRoom2grab == 'chicken' or threeStatueRoom2grab == 'chicken statue':
                secondFloorStatues['Chicken Statue'] = 'carry'
                items['hands'] = 'full'
                print("You pick up the statue of the chicken")
                gameOn()
            else:
                print("Either your hands are full or the statue is on the other side.")
                gameOn()
        elif secondFloorStatues['Fox Statue'] == 'Left Side' and items['hands'] != 'full':
            if threeStatueRoom2grab == 'fox' or threeStatueRoom2grab == 'fox statue':
                secondFloorStatues['Fox Statue'] = 'carry'
                items['hands'] = 'full'
                print("You pick up the statue of the fox.")
                gameOn()
            else:
                print("Either your hands are full or the statue is on the other side.")
                gameOn()
        elif secondFloorStatues['Grain Statue'] == 'Left Side' and items['hands'] != 'full':
            if threeStatueRoom2grab == 'grain' or threeStatueRoom2grab == 'grain statue' or threeStatueRoom2grab == 'bag of grain statue':
                secondFloorStatues['Grain Statue'] = 'carry'
                items['hands'] = 'full'
                print("You pick up the statue of the bag of grain.")
                gameOn()
            else:
                print("Either your hands are full or the statue is on the other side.")
                gameOn()
        else:
            print("The statues are on the other side")
            gameOn()
    elif playerAction == 'place' or playerAction == 'put' or playerAction == 'use' or playerAction == 'set':
        if items['hands'] == 'full' and secondFloorStatues['Chicken Statue'] == 'carry':
            print("You place the chicken statue down on the pedestal")
            secondFloorStatues['Chicken Statue'] = 'Left Side'
            items['hands'] = 'not full'
            threeStatueSolutionCheck()
            gameOn()
        elif items['hands'] == 'full' and secondFloorStatues['Fox Statue'] == 'carry':
            print("You place the Fox statue down on the pedestal")
            secondFloorStatues['Fox Statue'] = 'Left Side'
            items['hands'] = 'not full'
            threeStatueSolutionCheck()
            gameOn()
        elif items['hands'] == 'full' and secondFloorStatues['Grain Statue'] == 'carry':
            print("You place the chicken statue down on the pedestal")
            secondFloorStatues['Grain Statue'] = 'Left Side'
            items['hands'] = 'not full'
            threeStatueSolutionCheck()
            gameOn()
        else:
            print("You have nothing to put down")
            gameOn()
    else:
        print("That is not a valid action for the {}".format(FuggsData['location Name']))
        gameOn()

def sevenStatueRoomActions(playerAction):
    if playerAction == 'look':
        print("You see the staircase you came up from, the seven identical gargoyle statues, and the drawing of the three pyramids in a big circle on the far wall")
        gameOn()
    elif playerAction == 'light' or playerAction == 'ignite':
        gargoyleLight = input("Which lantern would you like to light? ").lower()
        if gargoyleLight == '3' or gargoyleLight == 'third':
            print("The latern illuminates extremely bright before fading to a constant dim light")
            lanterns['Lantern 3'] = 'lit'
            sevenStatuesSolutionCheck()
            gameOn()
        elif gargoyleLight == '4' or gargoyleLight == 'fourth':
            print("The latern illuminates extremely bright before fading to a constant dim light")
            lanterns['Lantern 4'] = 'lit'
            sevenStatuesSolutionCheck()
            gameOn()
        elif gargoyleLight == '7' or gargoyleLight == 'seventh':
            print("The lantern illuminates extremely bright before fading to a constant dim light")
            lanterns['Lantern 7'] = 'lit'
            sevenStatuesSolutionCheck()
            gameOn()
        else:
            print("Nothing happens. Lantern doesn't even catch fire.")
            gameOn()
    else:
        print("That is not a valid action for the {}".format(FuggsData['location Name']))
        gameOn()

def stoneRoomActions(playerAction):
    if playerAction == 'look':
       print("You are in the room with an alter and sitting in it's own stand is the Blood Stone")
       gameOn()
    elif playerAction == 'take' or playerAction == 'grab':
        items['Blood Stone'] = 'inventory'
        doors['Desert Door'] = 'open'
        print("You take the Blood Stone and put it in your bag. You also feel a rumble deep beneath you.")
        gameOn()
    else:
        print("That is not a valid action for the {}".format(FuggsData['location Name']))
        gameOn()

"""
Puzzle Solution Check
"""
def threeStatueSolutionCheck():
    if secondFloorStatues['Chicken Statue'] == 'Left Side' and secondFloorStatues['Grain Statue'] == 'Left Side' and secondFloorStatues['Fox Statue'] == 'Left Side':
        doors['Second floor stairs door'] = 'open'
        print("The wall on the north side of the room slides up to reveal another staircase.")
    else:
        pass

def sevenStatuesSolutionCheck():
    if lanterns['Lantern 3'] == 'lit' and lanterns['Lantern 4'] == 'lit' and lanterns['Lantern 7'] == 'lit':
        doors['Third floor stairs door'] = 'open'
        print("The north side of the wall slides up to reveal another staircase")



"""
Room initiate code
"""
def EntranceRoom():
    player_input = input('What would you like to do? ').lower()
    if player_input == '':
        print("Please try another input")
    elif player_input == 'help':
        help()
    elif player_input == 'look':
        entranceRoomActions(player_input)
    else:
        currentLocation = FuggsData['location Name']
        if FuggsData['location Name'] == 'Entrance Room':
            entranceRoom_MoveAndActions(player_input)

def StorageRoom():
    player_input = input('What would you like to do? ').lower()
    if player_input == '':
        print("Please try another input")
    elif player_input == 'help':
        help()
    elif player_input == 'look':
        storageRoomActions(player_input)
    else:
        if FuggsData['location Name'] == 'Storage Room':
            storageRoom_MoveAndActions(player_input)

def DogStatueRoom():
    player_input = input('What would you like to do? ').lower()
    if player_input == '':
        print("Please try another input")
    elif player_input == 'help':
        help()
    elif player_input == 'look':
        DogStatueRoomActions(player_input)
    else:
        if FuggsData['location Name'] == 'Dog Statue Room':
            DogStatueRoom_MoveAndActions(player_input)

def baseFloorRoom():
    player_input = input('What would you like to do? ').lower()
    if player_input == '':
        print("Please try another input")
    elif player_input == 'help':
        help()
    elif player_input == 'look':
        baseFloorStaircaseRoomActions(player_input)
    else:
        if FuggsData['location Name'] == 'Base Floor Staircase Room':
            baseFloorStaircaseRoom_MoveAndActions(player_input)

def threeStatueRoom1():
    player_input = input('What would you like to do? ').lower()
    if player_input == '':
        print("Please try another input")
    elif player_input == 'help':
        help()
    elif player_input == 'look':
        threeStatueRoom1Actions(player_input)
    else:
        if FuggsData['location Name'] == 'Three Statue Room Right Side':
            threeStatueRoom1_MoveAndActions(player_input)

def threeStatueRoom2():
    player_input = input('What would you like to do? ').lower()
    if player_input == '':
        print("Please try another input")
    elif player_input == 'help':
        help()
    elif player_input == 'look':
        threeStatueRoom2Actions(player_input)
    else:
        if FuggsData['location Name'] == 'Three Statue Room Left Side':
            threeStatueRoom2_MoveAndActions(player_input)

def sevenStatueRoom():
    player_input = input('What would you like to do? ').lower()
    if player_input == '':
        print("Please try another input")
    elif player_input == 'help':
        help()
    elif player_input == 'look':
        sevenStatueRoomActions(player_input)
    else:
        if FuggsData['location Name'] == 'Seven Statue Room':
            sevenStatueRoom_MoveAndActions(player_input)

def stoneRoom():
    player_input = input('What would you like to do? ').lower()
    if player_input == '':
        print("Please try another input")
        gameOn()
    elif player_input == 'help':
        help()
        gameOn()
    elif player_input == 'look':
        stoneRoom(player_input)
    else:
        if FuggsData['location Name'] == 'Stone Room':
            stoneRoom_MoveAndActions(player_input)

def startPathA():
    floorPuzzlePt1()

def gameOn():
    player_input = input("What would you like to do now? ").lower()
    if player_input == "help":
        help()
    elif player_input == "":
        print("Please try again.")
    else:
        current_location_name = FuggsData['location Name']
        if current_location_name == 'Entrance Room':
            entranceRoom_MoveAndActions(player_input)
        elif current_location_name == 'Storage Room':
            storageRoom_MoveAndActions(player_input)
        elif current_location_name == 'Dog Statue Room':
            DogStatueRoom_MoveAndActions(player_input)
        elif current_location_name == 'Base Floor Staircase Room':
            baseFloorStaircaseRoom_MoveAndActions(player_input)
        elif current_location_name == 'Three Statue Room Right Side':
            threeStatueRoom1_MoveAndActions(player_input)
        elif current_location_name == "Three Statue Room Left Side":
            threeStatueRoom2_MoveAndActions(player_input)
        elif current_location_name == 'Seven Statue Room':
            sevenStatueRoom_MoveAndActions(player_input)
        elif current_location_name == 'Stone Room':
            stoneRoom_MoveAndActions(player_input)
        else:
            print('error')

    if FuggsData['health'] < 1:
        print("You are dead! Too bad. You seemed like a nice person.")
    else:
        gameOn()

startPathA()
