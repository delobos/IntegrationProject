#Daniel Lobos
#Text Based adventure game

quick_maths = (2+2-1) ** 3 //3 * 10 / 5 % 5
name = input('What is your name? ')
print('\nWelcome '+ name + '!')

def chapter1():
    print('\nYou meet eyes with Chieftain Rammi, and immediately know this is not another one of his drills but in fact your home is under  attack')
    print("\n'Let's go Fuggs!' Chieftain says \n'I was informed of an armored intruder near the main entrance.'")
    print("\nYou stop for a moment realizing that your brother Noz was scheduled for guard duty today. \nYou take off in a full sprint past Chieftain Rammi towards the entrance, and more importantly towards the sound of weapons colliding.")
    print("\nYou arrive to the main room that connects to the entrance, a metallic smell hovers in the air as you see the frightened faces of your tribesman in the outer edges of the room.")
    print("Your eyes fix to the center of the room to see your bloodied brother laying on the floor and work your over to see the back of this crouched figure in leather padded armor and sword stained red, rummaging through your brother's remains")

def chapter1rest():
    print("\nYou stare in disbelief as this human falls over dead.\n.\n.\nYou are startled by the cheering of your fellow tribesman. You spin around as you feel this hand on your shoulder. \n'Fuggs, I am sorry about your brother, I know he..'")
    print("\nYou drown out Chieftain Rammi's words as you stare at this fallen man and notice the book labeled the 'The Mystical Arts of Alchemy' and pick it up to see a bookmarked page with the title 'Endless Wine' with a grocery list of items marked off except a Sapphire, but what really catches your attention is the neighboring page labeled 'Cure for the Eternal Slumber'")
    print("\n'Fuggs!' Chieftain says, You turn to see he is standing besides you looking at the book. \n'You have to go. If this is a way to bring back your brother than take this man's weapons and some supplies and go.' Chieftain says. \nYou nod your head in agreement and gather a small sack of supplies, and arm yourself with the mans sword and bow, slinging the quiver over your sholder. This man's armor was a little too big except for the fur boots he wore, you figure that's better than nothing.")
    print("\nYou step outside of the cave, light blinding you momentarily as your eyes adjust to the outdoors. You take out the book back to the bookmarked page and you notice that the pages of the 'Cure For Eternal Slumber' and 'Anything to Gold' seem to be stuck together, you carefully pull them apart to see an ingredient list on the left and two lines on the right. ")
    print("Most of the ingredients seem fairly simple to gather with a few exceptions, but what really catches your eye is the last item on the list, 'Heart of the blood rock'")
    print("Confused by the item you look at the other page that reads \n\nIn the sea of blazing gold, \nLies the heart of the rock so old \n\nYou look up from the book to see the Morgaric Desert to your left, in the middle you see he old forest of Wynn that was struck by a wilfire many generations ago, and to your right is Mcdollini wheat farm covered hundreds of acres of land.")

def choice2a():
    print("\n\nYou quietly pick up a rock nearly the size of your head, as you fix your gaze on the motionless intruder. \nAs you are within attacking distance you raise the rock above your head and bring it down with as much force as you can muster.")
    print("\nCRACK! \n\nYou feel the resistance of the rock making contact with the top of their head, quickly subside as they fall over dead.")

def choice2b():
    print("\nYou dart across the room up the intruder, who is now motionless in a crouched position. You bend your knees and jump, with arms stretched wide. For just a moment you look like an eagle diving towards a field mouse, as you come crashing down on this armored figure.")
    print("You hear a wet crack as you and the intruder topple over. You stand up to see the face of this man, with clear fluid seeping from his nose and ears, and the blood stained rock next to where he lay.")

def choice2c():
    print("\n'Hey!' you yell out, with no response. \nYou approach the intruder who just seems to be staring off into the distance. \nA minute passes of you trying to get the attention of the armored man before finally the man's eyes turn to meet yours and he stands up quickly, readying for battle.")
    print("You put your hands up showing that you are unarmed and ask \n'What do you want from us?' \n'This cave was supposed to be empty. I was just looking for the Sapphire before I was attacked' responded the intruder.")
    print("You stare at him in bewilderment, having never spoken this long to a human before. You then glance down at Noz, and tears begin to swell up your eyes. \n'I'm sorry about that. I didn't want to fight but he didn't want to talk and continued to attack me so I needed to defend myself.' said the man. \nYour sadness turns to hope as you hear him say, \n'Look I read of the legend of the Red Stone of Ressurection, and what it says is true. We may be able to bring your friend back.'")
    print("You both discuss the possibility before deciding to venture off together to bring the Red Stone and ressurect Noz. \nAs you guys begin your exit, \nCRACK! \nyour conversation is cut short as you feel a warm liquid splatter on you. You see Chieftain Rami holding a now bloodied rock in his hands.")
    print("\n'Good job distracting him, I knew you had a plan!' Chieftain Rammi said. \nYou look at down at your arms and chest and then towards the floor.")

def choice3a():
    print('choice 3a')
def choice3b():
    print('Choice 3b')
def choice3c():
    print('choice 3c')



start_game = ''
while start_game != 'Y':
    start_game = input('Would you like to begin? Y/N ').upper()

print("\nYou wake up to the sound of someone yelling 'INTRUDER!'")

choiceloop1 = 0
choice1 = ''
while choiceloop1 <= 0:
    choice1 = input('\nWhat would you like to? \na) Investigate \nor \nb) Go back to sleep?').lower()
    if choice1 == 'b':
        print("\n\nYou start to drift back to sleep, going back into that sweet dream of all you can eat meat pies \nzZzZ \nZz \nYour eyes open as you feel a strong kick to your side, that immediately curls you into a fetal postiion")
        print("'GET UP FUGGS!' \n'DONT YOU HEAR WE HAVE AN INTRUDER IN OUR BASE!'")
        choiceloop1 += 2
    elif choice1 == 'a':
        print("\n\nYou stand up, rubbing the crust off your eyes, you take a deep breath, letting the damp air of the cave fill your lungs and mutter to yourself '\nChief really should figure out why it smells like metal around here' \nYour door swings open")
        choiceloop1 +=1
chapter1()

choiceloop2 = 0
while choiceloop2 <= 0:
    choice2 = input("What would you like to do? \na) Pick up a nearby rock and sneak attack \nb) Try to surprise him \nc) Attempt to persuade him to stop and leave ").lower()
    if choice2 == 'b':
        choice2b()
        choiceloop2 +=1
    elif choice2 == 'c':
        choice2c()
        choiceloop2 += 1
    elif choice2 == 'a':
        choice2a()
        choiceloop2 += 1
chapter1rest()

choiceloop3 = 0
while choiceloop3 != 1:
    choice3 = input("Where would you like to go? \na) Morgaric Desert \nb) The old Forest of Wynn \nc) Mcdollini's Farm ").lower()
    if choice3 == 'a':
        choice3a()
        choiceloop3 += 1
    elif choice3 == 'b':
        choice3b()
        choiceloop3 +=1
    if choice3 == 'c':
        choice3c()
        choiceloop3 += 1