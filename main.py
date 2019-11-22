# Daniel Lobos
# Text Based adventure game


import PathC
import PathB
import PathBLore
import PathALore
import PathA

InventoryPathC = ""
AllyPathC = ""
LocationPathC = ""
PathABCchoice = ""

# This starts the game and its the same here until you have to
# choose which of the 3 locations to visit
# one keeps it as a text based adventure game
# one turns into a turn based combat game
# and the last one is more of an escape room type game



start_game = ''
while start_game != 'Y':
    start_game = input('Would you like to begin? Y/N ').upper()
    print("\nYou wake up to the sound of someone yelling 'INTRUDER!'")

choiceloop1 = 0
choice1 = ''
while choiceloop1 <= 0:
    choice1 = input('\nWhat would you like to? '
                    '\na) Investigate '
                    '\nb) Go back to sleep?').lower()
    if choice1 == 'b':
        print("\n\nYou start to drift back to sleep, "
              "going back into that sweet dream of all"
              " you can eat meat pies \nzZzZ \nZz \n")

        print("Your eyes open as you feel a"
              " strong kick to your side, that"
              " immediately curls you into a fetal postiion")

        print("'GET UP FUGGS!' \n'DONT YOU HEAR WE HAVE AN INTRUDER IN OUR BASE!'")
        choiceloop1 += 2
    elif choice1 == 'a':
        print("\n\nYou stand up, rubbing the crust off your"
              " eyes, you take a deep breath,"
              " letting the damp air of the cave fill "
              "your lungs and mutter to yourself '")

        print("Chief really should figure out why it smells like metal around here'"
              "Your door swings open")
        choiceloop1 += 1
    else:
        choice1 = input('\nWhat would you like to?'
                        '\na) Investigate'
                        '\nb) Go back to sleep?').lower()
PathC.chapter1()

choiceloop2 = 0
while choiceloop2 <= 0:
    choice2 = input("What would you like to do?"
                    "\na) Pick up a nearby rock and sneak attack"
                    "\nb) Try to surprise him"
                    "\nc) Attempt to persuade him to stop and leave ").lower()
    if choice2 == 'b':
        PathC.choice2b()
        choiceloop2 += 1
    elif choice2 == 'c':
        PathC.choice2c()
        choiceloop2 += 1
    elif choice2 == 'a':
        PathC.choice2a()
        choiceloop2 += 1
    else:
        choice2 = input("What would you like to do?"
                        "\na) Pick up a nearby rock and sneak attack"
                        "\nb) Try to surprise him"
                        "\nc) Attempt to persuade him to stop and leave ").lower()
PathC.chapter1rest()

choiceloop3 = 0
while choiceloop3 != 1:
    choice3 = input("Where would you like to go?"
                    "\na) Morgaric Desert"
                    "\nb) The old Forest of Wynn"
                    "\nc) Mcdollini's Farm ").lower()
    if choice3 == 'a':
        PathA.startPathA()
        choiceloop3 += 1
    elif choice3 == 'b':
        PathBLore.chapter1()
        PathB.PathBSkeletonBattle()
        PathB.PathBZombieBattle()
        PathB.PathBZombieBear()
        PathB.PathBEnd()
        PathB.PathBFinalBattle()
        choiceloop3 += 1
    elif choice3 == 'c':
        PathABCchoice += 'c'
        PathC.choice3c()
        PathC.mdFarm()
        choiceloop3 += 1
    else:
        choice3 = input("Where would you like to go?"
                        "\na) Morgaric Desert"
                        "\nb) The old Forest of Wynn"
                        "\nc) Mcdollini's Farm ").lower()


if PathABCchoice == "c":
    mcDfarmloop = 0
    while mcDfarmloop == 0:
        mFarmChoice1 = input("Where would you like to investigate?"
                             "\na)McDollini's home "
                             "\nb) The grain silos? ").lower()
        if mFarmChoice1 == 'a':
            PathC.mdHome()
            mcDfarmloop += 1
        elif mFarmChoice1 == 'b':
            PathC.mdSilo()
            mcDfarmloop += 1
        else:
            mFarmChoice1 =  input("Where would you like to investigate?"
                                  "\na)McDollini's home"
                                  "\nb) The grain silos? ").lower()

    mcDfarmloop2 = 0
    while mcDfarmloop2 == 0:
        mFarmChoice2 = input("Would you like to continue towards"
                             "\na)The cottage"
                             "\nb)The grain silos? ").lower()
        if mFarmChoice2 == 'a':
            print("You continue on towards the home.")
            print("To your surprise when you turn the handle of the door, it opens right up.")
            PathC.mdhome1()
            mcDfarmloop2 += 1
            mFarmLoop2a = 0
            while mFarmLoop2a == 0:
                mFarmChoice2a = input(
                    "Would you like to "
                    "\na)Investigate what happened?"
                    "\nb)Call out to McDollini?").lower()
                if mFarmChoice2a == 'a':
                    PathC.mdhome1a()
                    mFarmLoop2a += 1
                elif mFarmChoice2a == 'b':
                    PathC.mdhome1b()
                    InventoryPathC += "Stone"
                    LocationPathC += "Farm"
                    mFarmLoop2a += 1
                else:
                    mFarmChoice2a = input("Would you like to"
                                          "\na)Investigate what happened?"
                                          "\nb)Call out to McDollini?").lower()
        elif mFarmChoice2 == 'b':
            print("You continue towards the silo.")
            print("The one on the right is locked")
            print("the silo with the crow perched on top has the door wide open.")
            PathC.mdSilo1()
            mcDfarmloop2 += 1
            mcDfarmloop2b = 0
            while mcDfarmloop2b == 0:
                mFarmChoice2b = input("Would you like to"
                                      "\na)Investigate McDollini's body?"
                                      "\nb)Continue up the staircase?")
                if mFarmChoice2b == 'a':
                    PathC.mdSilo1a()
                    mcDfarmloop2b += 1
                elif mFarmChoice2b == 'b':
                    PathC.mdSilo1b()
                    InventoryPathC += "Stone"
                    LocationPathC += "Silo"
                    mcDfarmloop2b += 1
                else:
                    mFarmChoice2b = input("Would you like to"
                                          "\na)Investigate McDollini's body?"
                                          "\nb)Continue up the staircase?").lower()
else:
    pass

if InventoryPathC == "" and PathABCchoice == 'c':
    mcDfarmloop3 = 0
    while mcDfarmloop3 == 0:
        stepOutMainChoice = input("Would you like to"
                                  "\na) Chase after the fleeing crows"
                                  "\nb) Look for the source of the screech").lower()
        if stepOutMainChoice == 'a':
            PathC.SoLore1a()
            mcDfarmloop3 += 1
            SoChoiceloop1 = 0
            while SoChoiceloop1 == 0:
                SoChoice1 = input("Would you like attempt to"
                                  "\na) Stab the crow with your sword"
                                  "\nb) Try to break free from its grasp?").lower()
                if SoChoice1 == 'a':
                    PathC.SoPathcLore()
                    SoChoiceloop1 += 1
                elif SoChoice1 == 'b':
                    PathC.SoPathcLore2()
                    SoChoiceloop1 += 1
                    SoChoiceloop1a = 0
                    while SoChoiceloop1a == 0:
                        SoChoice1a = input("Would you like to"
                                           "\na) Help the crow"
                                           "\nb) Put it out of its misery").lower()
                        if SoChoice1a == 'a':
                            PathC.SoHelpLore()
                            AllyPathC += "Yes"
                            SoChoiceloop1a += 1
                        elif SoChoice1a == 'b':
                            PathC.SoKillLore()
                            PathC.NoStoneEndLore()
                            SoChoiceloop1a += 1
                        else:
                            SoChoicela = input("Would you like to"
                                               "\na) Help the crow"
                                               "\nb) Put it out of its misery").lower()
                else:
                    SoChoice1 = input("Would you like attempt to"
                                      "\na) Stab the crow with your sword"
                                      "\nb) Try to break free from its grasp?").lower()
        elif stepOutMainChoice == 'b':
            PathC.SoLore1b()
            mcDfarmloop3 += 1
            SoChoice2Loop = 0
            while SoChoice2Loop == 0:
                SoChoice2 = input("Would you like to"
                                  "\na) Ready an attack"
                                  "\nb) Attempt to talk to the crow").lower()
                if SoChoice2 == 'a':
                    PathC.SoKillLore2()
                    PathC.NoStoneEndLore()
                    SoChoice2Loop += 1
                elif SoChoice2 == 'b':
                    PathC.SoTalkLore()
                    SoChoice2Loop += 1
                    SoTalkLoop = 0
                    while SoTalkLoop == 0:
                        SoTalkChoice = input("Would you like to attempt to"
                                             "\na) Persuade the crow to help you"
                                             "\nb) Intimidate the crow for information").lower()
                        if SoTalkChoice == 'a':
                            PathC.SoTalkLorePers()
                            AllyPathC += "Yes"
                            PathC.SoHelpLore()
                            SoTalkLoop += 1
                        elif SoTalkChoice == 'b':
                            PathC.SoTalkLoreInti()
                            PathC.SoPathcLore()
                            SoTalkLoop += 1
                        else:
                            SoTalkChoice = input("Would you like to attempt to"
                                                 "\na) Persuade the crow to help you"
                                                 "\nb) Intimidate the crow for information")
                else:
                    SoChoice2 = input("Would you like to"
                                      "\na) Ready an attack"
                                      "\nb) Attempt to talk to the crow").lower()
        else:
            stepOutMainChoice = input("Would you like to"
                                      "\na) Chase after the fleeing crows"
                                      "\nb) Look for the source of the screech").lower()
elif InventoryPathC == "Stone" and LocationPathC == "Farm" and PathABCchoice == 'c':
    EsMainChoiceLoop1 = 0
    while EsMainChoiceLoop1 == 0:
        EsMainChoice1 = input("Would you like to"
                              "\na) Run away"
                              "\nb) Investigate the room").lower()
        if EsMainChoice1 == 'a':
            PathC.EsLore2()
            EsMainChoiceLoop1 += 1
            EsChoiceLoop2 = 0
            while EsChoiceLoop2 == 0:
                EsChoice2 = input("Would you like to attempt to"
                                  "\na) Fight off the crows in a last stand"
                                  "\nb) Pick the stone up and keep running").lower()
                if EsChoice2 == 'a':
                    PathC.EsLoreLast()
                    EsChoiceLoop2 += 1
                elif EsChoice2 == 'b':
                    PathC.EsLoreGrab()
                    EsChoiceLoop2 += 1
                else:
                    EsChoice2 = input("Would you like to attempt to"
                                      "\na) Fight off the crows in a last stand"
                                      "\nb) Pick the stone up and keep running").lower()
        elif EsMainChoice1 == 'b':
            PathC.EsLore1()
            EsMainChoiceLoop1 += 1
            EsChoiceLoop1 = 0
            while EsChoiceLoop1 == 0:
                EsChoice1 = input("Would you like to"
                                  "\na) Jump in the boat and go"
                                  "\nb) Make a decoy in the boat and release it").lower()
                if EsChoice1 == 'a':
                    PathC.EsLore1a()
                    EsChoiceLoop1 += 1
                    EsChoiceLoop1a = 0
                    while EsChoiceLoop1a == 0:
                        EsChoice1a = input("Would you like to"
                                           "\na) Throw the stone"
                                           "\nb) Fight on the boat").lower()
                        if EsChoice1a == 'a':
                            PathC.EsLore1aa()
                            PathC.NoStoneEndLore()
                            EsChoiceLoop1a += 1
                        elif EsChoice1a == 'b':
                            PathC.EsLore1ab()
                            EsChoiceLoop1a += 1
                        else:
                            EsChoice1a = input("Would you like to"
                                               "\na) Throw the stone"
                                               "\nb) Fight on the boat").lower()
                elif EsChoice1 == 'b':
                    PathC.EsLore1b()
                    EsChoiceLoop1 += 1
                    EsChoiceLoop1b = 0
                    while EsChoiceLoop1b == 0:
                        EsChoice1b = input("Would you like to"
                                           "\na) Take advantage of the decoy and make a run for it"
                                           "\nb) Hide in the house until they lose interest").lower()
                        if EsChoice1b == 'a':
                            PathC.EsLore1bb()
                            PathC.NoStoneEndLore()
                            EsChoiceLoop1b += 1
                        elif EsChoice1b == 'b':
                            EsChoiceLoop1b += 1
                            EsChoiceLoop1bb = 0
                            while EsChoiceLoop1bb == 0:
                                EsChoice1bb = input("Would you like to"
                                                    "\na) Hide under the bed"
                                                    "\nb) Hide in the closet").lower()
                                if EsChoice1bb == 'a':
                                    PathC.EsLoreBed()
                                    EsChoiceLoop1bb += 1
                                elif EsChoice1bb == 'b':
                                    PathC.EsLoreCloset()
                                    PathC.NoStoneEndLore()
                                    EsChoiceLoop1bb += 1
                                else:
                                    EsChoice1bb = input("Would you like to"
                                                        "\na) Hide under the bed"
                                                        "\nb) Hide in the closet").lower()
        else:
            EsMainChoice1 = input("Would you like to"
                                  "\na) Run away"
                                  "\nb) Investigate the room").lower()
elif InventoryPathC == "Stone" and LocationPathC == "Silo" and PathABCchoice == 'c':
    EsMainChoiceLoop2 = 0
    while EsMainChoiceLoop2 == 0:
        EsMainChoice2 = input("Would you like to"
                              "\na) Stay and make a plan"
                              "\nb) Make a run for it").lower()
        if EsMainChoice2 == 'a':
            EsMainChoiceLoop2 += 1
            EsChoiceLoop3 = 0
            while EsChoiceLoop3 == 0:
                EsChoice3 = input("Would you like to"
                                  "\na) Hide"
                                  "\nb) Look for a way to make a diversion").lower()
                if EsChoice3 == 'a':
                    PathC.EsLoreHide()
                    PathC.NoStoneEndLore()
                    EsChoiceLoop3 += 1
                elif EsChoice3 == 'b':
                    PathC.EsLoreLever()
                    EsChoiceLoop3 += 1
                    EsChoiceLoop3a = 0
                    while EsChoiceLoop3a == 0:
                        EsChoice3a = input("Would you like to"
                                           "\na) Make a run for it"
                                           "\nb) Jump into neighboring silo window").lower()
                        if EsChoice3a == 'a':
                            PathC.EsLore1bb()
                            PathC.NoStoneEndLore()
                            EsChoiceLoop3a += 1
                        elif EsChoice3a == 'b':
                            PathC.EsLoreSilo()
                            EsChoiceLoop3a += 1
                        else:
                            EsChoice3a = input("Would you like to"
                                               "\na) Make a run for it"
                                               "\nb) Jump into neighboring silo window").lower()
                else:
                    EsChoice3 = input("Would you like to"
                                      "\na) Hide"
                                      "\nb) Look for a way to make a diversion").lower()
        elif EsMainChoice2 == 'b':
            PathC.EsLore2()
            EsMainChoiceLoop2 += 1
            EsChoiceLoop2 = 0
            while EsChoiceLoop2 == 0:
                EsChoice2 = input("Would you like to attempt to"
                                  "\na) Fight off the crows in a last stand"
                                  "\nb) Pick the stone up and keep running").lower()
                if EsChoice2 == 'a':
                    PathC.EsLoreLast()
                    EsChoiceLoop2 += 1
                elif EsChoice2 == 'b':
                    PathC.EsLoreGrab()
                    InventoryPathC = ""
                    EsChoiceLoop2 += 1
                else:
                    EsChoice2 = input("Would you like to attempt to"
                                      "\na) Fight off the crows in a last stand"
                                      "\nb) Pick the stone up and keep running").lower()
        else:
            EsMainChoice2 = input("Would you like to"
                                  "\na) Stay and make a plan"
                                  "\nb) Make a run for it").lower()
else:
    pass


if InventoryPathC == "Stone" and PathABCchoice == 'c':
    PathC.continueLore()
    PathC.ReturnLore()
    PathC.RitualLore()
    PathC.HeroLore()
elif InventoryPathC == "" and PathABCchoice == 'c':
    PathC.ChaseLore()
    if AllyPathC == "Yes":
        PathC.EscortLore()
        ConChoiceLoop = 0
        while ConChoiceLoop == 0:
            ConChoice1 = input("Would you like to"
                               "\na) Prepare to fight"
                               "\nb) Try to convince King Brandon").lower()
            if ConChoice1 == 'a':
                PathC.ConFightLore()
                PathC.continueLore()
                PathC.ReturnLore()
                PathC.RitualLore()
                PathC.HeroLore()
                ConChoiceLoop += 1
            elif ConChoice1 == 'b':
                ConChoiceLoop += 1
                ConTalkLoop = 0
                while ConTalkLoop == 0:
                    ConTalk = input("Would you like to use"
                                    "\na) Persuasion"
                                    "\nb) Intimidation").lower()
                    if ConTalk == 'a':
                        PathC.ConTalkFailLore()
                        PathC.ConFightLore()
                        PathC.continueLore()
                        PathC.ReturnLore()
                        PathC.RitualLore()
                        PathC.HeroLore()
                        ConTalkLoop += 1
                    elif ConTalk == 'b':
                        PathC.ConTalkSuccessLore()
                        PathC.continueLore()
                        PathC.ReturnLore()
                        PathC.RitualLore()
                        PathC.HeroLore()
                        ConTalkLoop += 1
                    else:
                        ConTalk = input("Would you like to use"
                                        "\na) Persuasion"
                                        "\nb) Intimidation").lower()
    elif AllyPathC == "":
        PathC.RushInLore()
        PathC.ConFightLore()
        PathC.continueLore()
        PathC.ReturnLore()
        PathC.RitualLore()
        PathC.HeroLore()

    else:
        print("Error in final phase")
else:
    pass

print("\nTHANK YOU FOR PLAYING!")
