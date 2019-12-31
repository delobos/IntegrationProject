#Daniel Lobos
#Text Based adventure game


import PathC


def chapter1():
    print("\nYou make your way down the hill"
          " and towards The old Forest of Wynn."
          " As you approach you realize that"
          " while most of the trees are "
          "burned and lacking branches"
          " and leaves, they are still"
          " tall and wide.")

    print("Walking through the forest,"
          " you are hit with the faint "
          "odor of death. Along with the"
          " smell, you hear a light chanting"
          " off in the distance. Making your"
          "way deeper and deeper into the forest"
          " the chanting grows louder.")

    print("You get to the edge of a circular"
          " clearing and see a large tent"
          " set up with strange drawings"
          " of red figures in various states"
          " of dismemberment, along with"
          " different body parts from all"
          " kids of beast strewn along "
          "the camp.")

    print("Then you spot a hooded figure "
          "walking out of the tent with a"
          " human in a state of deep state "
          "of decay, but it seems to be"
          " following all of the hooded"
          " figures orders.")

    print("The hooded figure approaches a cauldron"
          " outside of the tent and begins "
          "to do the chant you heard earlier"
          " and begins to put ingredients into"
          " the pot. Then you spot a book "
          "lying on a stand next to the"
          " figure similar to your "
          "own alchemy book.")

    print("A skeleton with a rusty sword"
          " in a scabbard on its back, "
          "walking out of the tent but "
          "what really catches your eye"
          " is the shiny red stone in "
          "between its cream colored fingers")

    print("\nYou step out from behind the tree"
          " and shout out 'Hey you! give me "
          "that stone!' and everyone turns"
          " to look at you as the skeleton"
          " draws its sword. \n'Now who "
          "might you be?' the hooded figure"
          " said with an intrigued tone.")

    print("'Fuggs, and I'm here to try"
          " and save my brother' you "
          "reply. \n'You want this stone"
          " to resurrect your brother don't"
          " you?' it asked curiously. 'Yes!"
          " how did you know he was dead?' you say.")

    print("'Well no one wants the blood "
          "stone if not for the resurrection"
          " of someone, and lucky for "
          "you I love to bring things "
          "back from the dead' it replies "
          "cheerfully, pulling down its"
          " hood you see a gray old human man.")

    print("'But unlucky for you I have not had"
          " one of your kind and I think"
          " I want to add you tuo my"
          " collection' says the old man.")

def zombie_fight():
    print("\nThe Zombie drops the items in"
          " its hands and begins to make"
          " it's way over to feast on you!")


def skeleton_fight():
    print("\nThe Skeleton with a rusted "
          "longsword in hand, lowers it's "
          "body in a stance you know from "
          "sparing is one ready for a fight.")

def skeleton_defeat():
    print("\n'Sizrio! Nooo! He was my "
          "favorite soldier, we were"
          " just truly becoming friends!")
    zombie_fight()

def zombie_defeat():
    print("\n'Joseph! Nooo! He was my favorite"
          " zombie, and he was just "
          "getting good at juggling"
          " for me!")

def after_first_fight():
    print("\n'Okay, okay, I was mistaken "
          "you are strong. Let me gather"
          " my things and we can leave.' "
          "says the old man as he walks "
          "into his tent. You hear a "
          "rustling in the tent and call out")

    print("'Everything okay in there?!' but to no response.")

def zombie_bear_fight():
    print("You hear the clattering of chains as"
          " they hit the forest floor followed"
          " by a tremendous roar as the floor "
          "beneath you shakes. Out comes the biggest"
          " brown bear you have every seen,")

    print("but that's not what catches you "
          "eye, its the fact that you can see "
          "his sharp teeth through a hole in the "
          "side of his cheek where rotting "
          "flesh hangs. His ribs exposed "
          "but not from malnourishment")

    print("'HAHAHA! meet my boy, Lou!'"
          " says the old man, as bear "
          "stands up on its two feet"
          " before letting out a roar"
          " and charging you.")


def after_all_fight():
    print("'I'm sorry! Please don't kill"
          " me! Here have the stone I don't need it!'")
    necromancer_decision_loop = 0
    while necromancer_decision_loop == 0:
        path_b_decision_choice = input("Would you like to \na) Kill the necromancer and take the stone \nor \nb) Take the stone and leave").lower()
        if path_b_decision_choice == 'a':
            print("\nYou raise your sword and bring it down hard, instantly killing the old man. You take the stone from his possession as you take your leave.")
            necromancer_decision_loop += 1
        elif path_b_decision_choice == 'b':
            print("\nYou walk over to the old man and take the stone from him. 'Thank you for your mercy! Sorry for the trouble I have caused!' he shouts as you take your leave.")
            necromancer_decision_loop += 1
        else:
            path_b_decision_choice = input("Would you like to \na) Kill the necromancer and take the stone \nor \nb) Take the stone and leave").lower()


def path_b_hero_lore():
    print("\nYou wake up to the sound of someone yelling 'INTRUDER!'")

    choice_loop_hero = 0
    while choice_loop_hero <= 0:
        choice_hero = input('\nWhat would you like to? \na) Investigate \nor \nb) Go back to sleep?').lower()
        if choice_hero == 'b':
            print("\n\nYou start to drift back to sleep, "
                  "going back into that sweet dream of all you"
                  " can eat meat pies \nzZzZ \nZz \nYour eyes"
                  " open as you feel a strong kick to your"
                  " side, that immediately curls you into a fetal position")

            print("'GET UP FUGGS!' \n'DONT YOU HEAR WE "
                  "HAVE AN INTRUDER IN OUR BASE!'")
            choice_loop_hero += 1
        elif choice_hero == 'a':
            print("\n\nYou stand up, rubbing the crust off your eyes"
                  ", you take a deep breath, letting the damp"
                  " air of the cave fill your lungs and "
                  "mutter to yourself '\nChief really should"
                  " figure out why it smells like "
                  "metal around here' \nYour door"
                  " swings open")
            choice_loop_hero += 1
        else:
            choice_hero = input('\nWhat would you like to?'
                               '\na) Investigate'
                               '\nb) Go back to sleep?').lower()
    print('\nYou meet eyes with Chieftain Rammi,'
          ' and immediately know this is not'
          ' another one of his drills but'
          ' in fact your home is under  attack')

    print("\n'Let's go Fuggs!' Chieftain"
          " says \n'I was informed of an"
          " armored intruder near the"
          " main entrance.'")

    print("\nYou stop for a moment having "
          "a strong feeling of de ja vu,"
          "you shake the feeling and run "
          "towards the sound of weapons"
          " colliding.")
    print("\nYou sprint to the mouth of "
          "the cave entrance to see a human"
          " attacking your brother Noz, you"
          " are stunned for a second definitely"
          " knowing that this has happened"
          " before.")
    print("Noz is struck down and the"
          " human turns to you and declares"
          " 'I, {} need to kill one more goblin"
          " so I can truly start my journey"
          " to being an adventurer".format(PathC.name))
