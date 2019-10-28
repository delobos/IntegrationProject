#Daniel Lobos
#Text Based adventure game
#Sprint 1
quick_maths = (2+2-1) ** 3 //3 * 10 / 5 % 5
name = input('What is your name? ')
print('\nWelcome '+ name + '!')

#Sprint 2
rows = int(input('Enter a number'))
def sprint2(rows):
    for x in range(1, rows + 1):
        rows -= 1
        for x in range(1, rows + 2):
            print(x, end=' ')
        print()

sprint2(8)
sprint2(rows)

InventoryPathC = ""
AllyPathC = ""
LocationPathC = ""

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
    print('Desert')
def choice3b():
    print('Old Forest of Wynn')
def choice3c():
    print("\nAs you make your way down the path on the side of the hill towards McDollini's farm, You are momentarily caught in the shadow of some of the biggest birds you have seen. With feathers as dark as the shadows they are casting.")

def mdFarm():
    print("You reach the eastern edge of the wheat fields, which sits slightly elevated.")
    print("Towards the center you see old McDollini's home. A one story wooden cottage with a connecting watermill sitting right on the edge of D'awnqui Khong river.")
    print("Upon further inspection you notice the dark figure on the roof of the home was not a wind vane but one of the birds from earlier.")
    print("\nPast the home in southern direction you see a two matching stone grail silos, where another bird circles above")
    print("You see one more bird perched on the leftmost silo's window")
    print("\nYou are interrupted by a scream in the direction of the home.")

def mdHome():
    print('\nYou rush over to the home, and as you get closer you look up and see this bird that you now realize is a crow, staring at you with eyes like daggers')
    print("As you almost reach the front of the home you realize that the yelling has stopped from this direction and has changed to the direction of the silos.")

def mdhome1():
    print("\nYou open the door to reveal a mess of a home. Furniture is knocked over, silverware and various dishes and cups are strewn about.")

def mdhome1a():
    print("\nUpon further inspection notice what looks like three long scratch marks in various location always paired with torn fabric or blood")
    print("You hear a rustling in the back of the home")
    print("You investigate only to be startled by this crow, much larger than you standing over the body of McDollini. \nBut thats not what catches your eye, no it's the red stone glimmering in between its beak. ")
    print("It looks at you momentarily before flying out of the open window behind it and taking off into flight.")

def mdhome1b():
    print("\nYou call out but to no answer. You ready your shortsword as you clear the home room by room.")
    print("You approach the last room, sword in hand and kick the door open to reveal a crow, much larger than you, standing over the body of McDollini.")
    print("The sight of your sword, makes the crow stumble back dropping a red stone that it was holding in between its beak.")
    print("You rush over to grab it the stone as the crow jumps out of the open window behind it")



def mdSilo():
    print("\nYou make your way over to the silo, pushing past rows of grain. As you approach the left most silo you realize the screaming has stopped and the bird that was flying above is now perched on the roof staring at you intently.")
    print("You also notice that these birds you saw earlier are crows, and the one that was on the window has disappeared inside.")
    print("Staring back at this crow you are knocked out of the trance by screaming now coming from the direction of the cottage.")

def mdSilo1():
    print("\nYou step into the silo. Inside is another cylinder where you presume the grain would be stored and inbetween the inner and outer cylinder of the cylinder is a staricase that leads to the top of the silo.")
    print("You notice at the foot of the staircase is the body of McDollini")

def mdSilo1a():
    print("\nAs you approach his body you notice that he has long and wide scratches all over him, appearing in streaks of three.")
    print("You notice his body is cold to the touch")
    print("Then you are interrupted by the sound of rustling echoing above you.")
    print("You make your way up the staircase to an  office area at the top of the silo, with the open window being the only light source in the room")
    print("The crow from earlier turns to see you standing at the top of the staircase as it turns and flies out of the window.")

def mdSilo1b():
    print("\nYou draw your short sword and carefully step of McDollini's body as you make your way up the staircase.")
    print("You reach the top of the staircase onto what looks like a office area with the only light being the open window.")
    print("The crow from earlier turns to looks at you, and surprised by the presence of another person in the room, and your sword in hand. It opens its mouth to caw, dropping a red stone to the ground.")
    print("It turns and flies out of the window")

def StepOut():
    print("\nYou run out side, weapon in hand. As you step out you see the fleeing crow above flying away from you with a crow on either side of it.")
    print("You then hear the scream from earlier turn into a bird-like screech above you")

def SoLore1a():
    print("You take off in a sprint towards the escaping crow. After a few moments of running, you feel this pressure followed by three sharp stabs on both sides of your chest.")
    print("Your legs and body begin to feel weightless as you come to realize you were grabbed by one of the crows and are being lifted off the ground. ")

def SoLore1b():
    print("Your eyes dart around searching for the source of the caw-ing, and a moment before being grabbed\nyou take sight of the crow who is diving towards you and roll out of the way, feeling a strong breeze blow past you")

def SoPathcLore():
    print("You are able to position yourself to stab the crow in the thigh, who gives out an ear piercing screech as he lets go of you with the injured claw.")
    print("You wiggle free of the grasp of the remaining claw, falling 30 feet into McDollini's wheat field that softens the landing.")
    print("You see the injured crow flying sporadically in the direction of the crows from earlier. You begin the chase")
def SoPathcLore2():
    print("You begin to thrash about trying to get the crow to loosen its grip around your chest. The shaking is enough for the crow to begin to screech with anger and you notice the sudden shifts in altitude.")
    print("For a moment you are released and begin to free fall before being caught again by the crow but not without loosing to much speed and the both of you falling quickly to the ground.")
    print("You are able to position yourself last minute above the crow, who when you both collide with the ground, lets out a cry of pain as you simultaneously feel and hear a loud crunch beneath you.")
    print("The crow screeching in agony begins to repeat a noise, that eventually you make out as 'Help!'. Your eyes widen and the crow must realize you understood it and begins to speak in common language used by many races.")
    print("'Please help me! Leg broke! Leg broke! Help!")
def SoHelpLore():
    print("You grab two sturdy sticks and break them to the length of the crow's broken leg and make a splint")
    print("'You help! You help! Me help! Want red shiny?!' \nYou get that the crow is thankful for your actions and wants to help you get the stone back from it's fellow crows who abandoned him.")

def NoStoneEndLore():
    print("Empty-handed you return home, and as you approach the mouth of the cave you hear the sound of metal clashing. You sprint inside to see another human attacking Chief Rammi surrounded by dozens of your dead tribesman")
    print("Chief Rammi is struck down and the human turns to you and declares 'I, {} need to kill one more goblin so I can truly start my journey to being an adventurer".format(name))
    print("You are easily overpowered and as you are stabbed, you feel yourself getting really tired and your breaths become shallow. Everything fades to black")
    print("\nYou wake up to the sound of someone yelling 'INTRUDER!'")

def SoKillLore():
    print("You walk over to the body of the crow, wiggling around in pain and screeching out in fear.")
    print("You grab your shortsword with both of your hands on the hilt, and tha blade pointing down towards the cowering crow.")
    print("As you bring the sword down, there is an initial resistance than it goes through and stops abruptly. You feel the warm blood splatter on your hands as the crow lets out a final screech before slumping over lifeless.")
    print("A moment passes before you remember your mission. You look around but with vision slightly obscured by grain you make your way to a tree where you climb and try to get a sight on the fleeing crows, but to no avail.")

def SoKillLore2():
    print("With sword in hand you lock onto the crow and ready yourself to attack. The crow taking a long arc turns to face you as it begins to dive back down towards you.")
    print("You grip the sword tightly with both hands and right before you are attacked you side step with a hard wide swing. You hear a wet cut as the sword is pulled out of your hands.")
    print("The crow screeches out in agony. You turn to look seeing your sword sticking out of its side. Attempting to retrieve your sword, to finish the job, the crow pecks at you stabbing you in the shoulder.")
    print("You pull your sword from the creatures side as it lets our another loud screech. You raise the sword over your head and bring it down diagonally on its shoulder, where the crow begins to let our a gurglling sound before falling over lifeless.")
    print("You stand there momentarily looking at your defeated foe before snapping back into the moment and realizing you have lost sight of the fleeing crows. You climg a stack of boxes near the porch and get on the roof but to no avail. You can no longer see the fleeing crows.")

def SoTalkLore():
    print("With the crow flying overhead you call out to the crow and lower your weapon. You see the crow pull its wings forward, making itself wide as it floats down towards you. It lands a few feet in front of you" )
    print("'What you want?' the crow screeches at you in common.")

def SoTalkLoreInti():
    print("The crow eyeing you carefully seeing you switch back to an aggressive stance, and screeches out. \n'You better take me to your friends or I will have no choice but to hurt you!' you yell out.")
    print("The crow mimics a human like laugh before charging at you. You quickly sidestep as you stab. The sword's hilt slips out of your hands as the blade goes through the thigh of the crow.")
    print("Screeching in pain it takes flights in the direction of the other fleeing crows, with your sword sticking out of its leg.")
    print("You take off in chase of this crow and its lair.")

def SoTalkLorePers():
    print("You begin to tell the crow what happened to your brother and how you are on a mission to try and save him. You jump back as this crow lets out a screech before saying \n'Humans kill family! Humans bad! I help you!'")
    print("You partner up with your new friend as he takes flight in the direction of his fleeing friends and motions for you to follow. You both begin your journey towards the crow's lair")

def EsLore2():
    print("EsLore 2 here*****")

def EsLoreLast():
    print("ESLore Last here ****")

def EsLoreGrab():
    print("Es Lore Grab here ****")

def EsLore1():
    print("Es Lore 1 here *****")

def EsLore1a():
    print("Es Lore 1a here *****")

def EsLore1aa():
    print("Es Lore 1aa here *****")

def EsLore1b():
    print("Es Lore 1b here ****")

def EsLore1bb():
    print("EsLore1bb here ****")

def EsLoreBed():
    print("EsLoreBEd here *****")

def EsLoreCloset():
    print("EsLoreCloset here *****")

def EsLoreHide():
    print("EsLoreHide here ****")

def EsLoreLever():
    print("EsLoreLever here ****")

def EsLoreSilo():
    print("EsLoreSilo here*****")

def continueLore():
    print("Continue Lore ***")

def ReturnLore():
    print("ReturnLore here*****")

def RitualLore():
    print("RitualLore here *****")

def HeroLore():
    print("HeroLore here *****")

def EscortLore():
    print("EscortLore here ****")

def ChaseLore():
    print("ChaseLore here ****")

def ConFightLore():
    print("FightLore here *****")

def ConTalkFailLore():
    print("ConTalkFailLore here ****")

def ConTalkSuccessLore():
    print("ConTalkSuccessLore here ****")

def RushInLore():
    print("RushInLore here *****")






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
    else:
        choice1 = input('\nWhat would you like to? \na) Investigate \nor \nb) Go back to sleep?').lower()
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
    else:
        choice2 = input("What would you like to do? \na) Pick up a nearby rock and sneak attack \nb) Try to surprise him \nc) Attempt to persuade him to stop and leave ").lower()
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
    elif choice3 == 'c':
        choice3c()
        choiceloop3 += 1
    else:
        choice3 = input(
            "Where would you like to go? \na) Morgaric Desert \nb) The old Forest of Wynn \nc) Mcdollini's Farm ").lower()

mcDfarmloop = 0
while mcDfarmloop == 0:
    mFarmChoice1 = input("Where would you like to investigate? \na)McDollini's home \nor \nb) The grain silos? ").lower()
    if mFarmChoice1 == 'a':
        mdHome()
        mcDfarmloop +=1
    elif mFarmChoice1 == 'b':
        mdSilo()
        mcDfarmloop += 1
    else:
        mFarmChoice1 =  input("Where would you like to investigate? \na)McDollini's home \nor \nb) The grain silos? ").lower()

mcDfarmloop2 = 0
while mcDfarmloop2 == 0:
    mFarmChoice2 = input("Would you like to continue towards \na)The cottage \nor \nb)The grain silos? ").lower()
    if mFarmChoice2 == 'a':
        print("You continue on towards the home and to your surprise when you turn the handle ot the door, it opens right up.")
        mdhome1()
        mcDfarmloop2 +=1
        mFarmLoop2a = 0
        while mFarmLoop2a == 0:
            mFarmChoice2a = input(
                "Would you like to \na)Investigate what happened? \nor \nb)Call out to McDollini?").lower()
            if mFarmChoice2a == 'a':
                mdhome1a()
                mFarmLoop2a += 1
            elif mFarmChoice2a == 'b':
                mdhome1b()
                InventoryPathC += "Stone"
                LocationPathC += "Farm"
                mFarmLoop2a += 1
            else:
                mFarmChoice2a = input(
                    "Would you like to \na)Investigate what happened? \nor \nb)Call out to McDollini?").lower()
    elif mFarmChoice2 == 'b':
        print("You continue towards the silo, the one on the right is locked but the silo with the crow perched on top has the door wide open.")
        mdSilo1()
        mcDfarmloop2 += 1
        mcDfarmloop2b = 0
        while mcDfarmloop2b == 0:
            mFarmChoice2b = input("Would you like to \na)Investigate McDollini's body? \nor \nb)Continue up the staircase?")
            if mFarmChoice2b == 'a':
                mdSilo1a()
                mcDfarmloop2b += 1
            elif mFarmChoice2b == 'b':
                mdSilo1b()
                InventoryPathC += "Stone"
                LocationPathC += "Silo"
                mcDfarmloop2b += 1
            else:
                mFarmChoice2b = input("Would you like to \na)Investigate McDollini's body? \nor \nb)Continue up the staircase?").lower()

if InventoryPathC == "":
    mcDfarmloop3 = 0
    while mcDfarmloop3 == 0:
        stepOutMainChoice = input("Would you like to \na) Chase after the fleeing crows \nor \nb) Look for the source of the screech").lower()
        if stepOutMainChoice == 'a':
            SoLore1a()
            mcDfarmloop3 += 1
            SoChoiceloop1 = 0
            while SoChoiceloop1 == 0:
                SoChoice1 = input("Would you like attempt to \na) Stab the crow with your sword \nor \nb) Try to break free from its grasp?").lower()
                if SoChoice1 == 'a':
                    SoPathcLore()
                    SoChoiceloop1 += 1
                elif SoChoice1 == 'b':
                    SoPathcLore2()
                    SoChoiceloop1 += 1
                    SoChoiceloop1a = 0
                    while SoChoiceloop1a == 0:
                        SoChoice1a = input("Would you like to \na) Help the crow \nor \nb) Put it out of its misery").lower()
                        if SoChoice1a == 'a':
                            SoHelpLore()
                            AllyPathC += "Yes"
                            SoChoiceloop1a += 1
                        elif SoChoice1a == 'b':
                            SoKillLore()
                            NoStoneEndLore()
                            SoChoiceloop1a += 1
                        else:
                            SoChoicela = input("Would you like to \na) Help the crow \nor \nb) Put it out of its misery").lower()
                else:
                    SoChoice1 = input("Would you like attempt to \na) Stab the crow with your sword \nor \nb) Try to break free from its grasp?").lower()
        elif stepOutMainChoice == 'b':
            SoLore1b()
            mcDfarmloop3 += 1
            SoChoice2Loop = 0
            while SoChoice2Loop == 0:
                SoChoice2 = input("Would you like to \na) Ready an attack \nor \nb) Attempt to talk to the crow").lower()
                if SoChoice2 == 'a':
                    SoKillLore2()
                    NoStoneEndLore()
                    SoChoice2Loop += 1
                elif SoChoice2 =='b':
                    SoTalkLore()
                    SoChoice2Loop += 1
                    SoTalkLoop = 0
                    while SoTalkLoop == 0:
                        SoTalkChoice = input("Would you like to attempt to \na) Persuade the crow to help you \nor \nb) Intimidate the crow for information").lower()
                        if SoTalkChoice == 'a':
                            SoTalkLorePers()
                            AllyPathC += "Yes"
                            SoHelpLore()
                            SoTalkLoop += 1
                        elif SoTalkChoice == 'b':
                            SoTalkLoreInti()
                            SoPathcLore()
                            SoTalkLoop += 1
                        else:
                            SoTalkChoice = input("Would you like to attempt to \na) Persuade the crow to help you \nor \nb) Intimidate the crow for information")
                else:
                    SoChoice2 = input("Would you like to \na) Ready an attack \nor \nb) Attempt to talk to the crow").lower()
        else:
            stepOutMainChoice = input(
                "Would you like to \na) Chase after the fleeing crows \nor \nb) Look for the source of the screech").lower()
elif InventoryPathC == "Stone" and LocationPathC == "Farm":
    EsMainChoiceLoop1 = 0
    while EsMainChoiceLoop1 == 0:
        EsMainChoice1 = input("Would you like to \na) Run away \nor \nb) Investigate the room").lower()
        if EsMainChoice1 == 'a':
            EsLore2()
            EsMainChoiceLoop1 += 1
            EsChoiceLoop2 = 0
            while EsChoiceLoop2 == 0:
                EsChoice2 = input("Would you like to attempt to \na) Fight off the crows in a last stand \nor \nb) Pick the stone up and keep running").lower()
                if EsChoice2 == 'a':
                    EsLoreLast()
                    EsChoiceLoop2 += 1
                elif EsChoice2 == 'b':
                    EsLoreGrab()
                    #Follow#^^^^
                    EsChoiceLoop2 += 1
                else:
                    EsChoice2 = input(
                        "Would you like to attempt to \na) Fight off the crows in a last stand \nor \nb) Pick the stone up and keep running").lower()
        elif EsMainChoice1 == 'b':
            EsLore1()
            EsMainChoiceLoop1 += 1
            EsChoiceLoop1 = 0
            while EsChoiceLoop1 == 0:
                EsChoice1 = input("Would you like to \na) Jump in the boat and go \nor \nb) Make a decoy in the boat and release it").lower()
                if EsChoice1 == 'a':
                    EsLore1a()
                    EsChoiceLoop1 += 1
                    EsChoiceLoop1a = 0
                    while EsChoiceLoop1a == 0:
                        EsChoice1a = input("Would you like to \na) Throw the stone \nor \nb) Fight on the boat").lower()
                        if EsChoice1a == 'a':
                            EsLore1aa()
                            NoStoneEndLore()
                            EsChoiceLoop1a += 1
                        elif EsChoice1a == 'b':
                            EsLore1b()
                            EsChoiceLoop1a += 1
                        else:
                            EsChoice1a = input(
                                "Would you like to \na) Throw the stone \nor \nb) Fight on the boat").lower()
                elif EsChoice1 == 'b':
                    EsLore1b()
                    EsChoiceLoop1 += 1
                    EsChoiceLoop1b = 0
                    while EsChoiceLoop1b == 0:
                        EsChoice1b = input("Would you like to \na) Take advantage of the decoy and make a run for it \nor \nb) Hide in the house until they lose interest").lower()
                        if EsChoice1b == 'a':
                            EsLore1bb()
                            NoStoneEndLore()
                            EsChoiceLoop1b += 1
                        elif EsChoice1b == 'b':
                            EsChoiceLoop1b += 1
                            EsChoiceLoop1bb = 0
                            while EsChoiceLoop1bb == 0:
                                EsChoice1bb = input("Would you like to \na) Hide under the bed \nor \nb) Hide in the closet").lower()
                                if EsChoice1bb == 'a':
                                    EsLoreBed()
                                    EsChoiceLoop1bb += 1
                                elif EsChoice1bb == 'b':
                                    EsLoreCloset()
                                    NoStoneEndLore()
                                    EsChoiceLoop1bb += 1
                                else:
                                    EsChoice1bb = input("Would you like to \na) Hide under the bed \nor \nb) Hide in the closet").lower()
        else:
            EsMainChoice1 = input("Would you like to \na) Run away \nor \nb) Investigate the room").lower()
elif InventoryPathC == "Stone" and LocationPathC == "Silo":
    EsMainChoiceLoop2 = 0
    while EsMainChoiceLoop2 == 0:
        EsMainChoice2 = input("Would you like to \na) Stay and make a plan \nor \nb) Make a run for it").lower()
        if EsMainChoice2 == 'a':
            EsMainChoiceLoop2 += 1
            EsChoiceLoop3 = 0
            while EsChoiceLoop3 == 0:
                EsChoice3 = input("Would you like to \na) Hide \nor \nb) Look for a way to make a diversion").lower()
                if EsChoice3 == 'a':
                    EsLoreHide()
                    NoStoneEndLore()
                    EsChoiceLoop3 += 1
                elif EsChoice3 == 'b':
                    EsLoreLever()
                    EsChoiceLoop3 += 1
                    EsChoiceLoop3a = 0
                    while EsChoiceLoop3a == 0:
                        EsChoice3a = input("Would you like to \na) Make a run for it \nor \nb) Jump into neighboring silo window").lower()
                        if EsChoice3a == 'a':
                            EsLore1bb()
                            NoStoneEndLore()
                            EsChoiceLoop3a += 1
                        elif EsChoice3a =='b':
                            EsLoreSilo()
                            EsChoiceLoop3a += 1
                        else:
                            EsChoice3a = input("Would you like to \na) Make a run for it \nor \nb) Jump into neighboring silo window").lower()
                else:
                    EsChoice3 = input("Would you like to \na) Hide \nor \nb) Look for a way to make a diversion").lower()
        elif EsMainChoice2 == 'b':
            EsLore2()
            EsMainChoiceLoop2 += 1
            EsChoiceLoop2 = 0
            while EsChoiceLoop2 == 0:
                EsChoice2 = input(
                    "Would you like to attempt to \na) Fight off the crows in a last stand \nor \nb) Pick the stone up and keep running").lower()
                if EsChoice2 == 'a':
                    EsLoreLast()
                    EsChoiceLoop2 += 1
                elif EsChoice2 == 'b':
                    EsLoreGrab()
                    # Follow#^^^^
                    InventoryPathC = ""
                    EsChoiceLoop2 += 1
                else:
                    EsChoice2 = input("Would you like to attempt to \na) Fight off the crows in a last stand \nor \nb) Pick the stone up and keep running").lower()
        else:
            EsMainChoice2 = input("Would you like to \na) Stay and make a plan \nor \nb) Make a run for it").lower()
else:
    print("Rare error")


if InventoryPathC == "Stone":
    continueLore()
    ReturnLore()
    RitualLore()
    HeroLore()
elif InventoryPathC == "":
    ChaseLore()
    if AllyPathC == "Yes":
        EscortLore()
        ConChoiceLoop = 0
        while ConChoiceLoop == 0:
            ConChoice1 = input("Would you like to \na) Prepare to fight \nor \nb) Try to convince King Brandon").lower()
            if ConChoice1 == 'a':
                ConFightLore()
                continueLore()
                ReturnLore()
                RitualLore()
                HeroLore()
                ConChoiceLoop += 1
            elif ConChoice1 == 'b':
                ConChoiceLoop += 1
                ConTalkLoop = 0
                while ConTalkLoop == 0:
                    ConTalk = input("Would you like to use \na) Persuasion \nor \nb) Intimidation").lower()
                    if ConTalk == 'a':
                        ConTalkFailLore()
                        ConFightLore()
                        continueLore()
                        ReturnLore()
                        RitualLore()
                        HeroLore()
                        ConTalkLoop += 1
                    elif ConTalk == 'b':
                        ConTalkSuccessLore()
                        continueLore()
                        ReturnLore()
                        RitualLore()
                        HeroLore()
                        ConTalkLoop += 1
                    else:
                        ConTalk = input("Would you like to use \na) Persuasion \nor \nb) Intimidation").lower()
    elif AllyPathC == "":
        RushInLore()
        ConFightLore()
        continueLore()
        ReturnLore()
        RitualLore()
        HeroLore()

    else:
        print("Error in final phase")
else:
    print("Big Bad Error")