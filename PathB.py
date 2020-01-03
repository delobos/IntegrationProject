# Daniel Lobos
# Text Based adventure game

import random
import PathBLore
import PathC


class Character:
    def __init__(self, name='Fuggs', weapon='Shortsword'):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.Basedmg = 9
        self.weapon = weapon
        self.potions = 6

    def attack(self):
        dmg = self.Basedmg
        if self.weapon == "Shortsword":
            dmg += 6
        elif self.weapon == "":
            dmg = self.Basedmg

        return dmg


class Baddie:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_dmg = 5

    def attack(self):
        dmg = self.base_dmg
        if self.name == "Zombie":
            bite = random.randint(0, 1)
            if bite == 1:
                print("Zombie tries to bite!")
                dmg += 5
            else:
                pass
            return dmg
        elif self.name == "Skeleton":
            dmg += 2
        elif self.name == "Undead Lou":
            chomp = random.randint(0, 1)
            if chomp == 1:
                print("Undead Lou tries to chomp!")
                dmg += 8
            else:
                pass
            return dmg
        return dmg


class Hero:
    def __init__(self, name=PathC.name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_dmg = 20

    def attack(self):
        dmg = self.base_dmg
        power_strike = random.randint(0, 5)
        if power_strike == 5:
            print("The intruder rears back as he unleashes a powerful blow")
            dmg = self.base_dmg * 4
        else:
            print('You attempt to block the hit but only reduce the damage')
        return dmg


def whos_turn():
    if random.randint(0, 1) == 0:
        return "Fuggs"
    else:
        return enemy.name


def death_check():
    if player.health < 1:
        print("Too badly inured you fall over dead.")
        print("Maybe next time will be better")
        print("But then, you wake up to the sound of someone yelling 'INTRUDER!'")
    elif enemy.health < 1:
        print("You have killed the {}".format(enemy.name))
        if enemy.name == PathC.name:
            print("WAIT! WHAT?! NO! That was not supposed to happen! This was a scripted death!")
        else:
            pass
    else:
        pass


def combat():
    fight_choice_loop = 0
    while fight_choice_loop == 0:
        try:
            fight_choice = int(input("1) Attack \nor \n2) Drink Potion"))
            if fight_choice == 1:
                attack_option()
                fight_choice_loop += 1
            elif fight_choice == 2:
                drink_potion()
                fight_choice_loop += 1
        except ValueError:
            print("\nThat was not one of the options, try again.")


def drink_potion():
    if player.potions < 1:
        print("\nYou do not have any potions left!")
    else:
        player.health += 25
        player.potions -= 1
        print("\nYou have {} health points".format(player.health))
        if player.health > 100:
            print("With", (player.health - 100), "as temporary health points.")
        else:
            pass


def attack_option():
    selected_move = int(input("\n1) Slash \nor \n2) Stab"))
    if selected_move == 1:
        slash_attack()
    elif selected_move == 2:
        stab_attack()
    else:
        selected_move = int(input("\n1) Slash \t 2) Stab \n3) Dodge"))


def stab_attack():
    hit_or_crit = random.randint(1, 21)
    if hit_or_crit <= 19:
        print("\nYou hit!")
        enemy.health -= player.attack()
        print("\n{}'s health is: {}".format(enemy.name, enemy.health))
    else:
        print("\nCritical stab!")
        enemy.health -= player.attack() * 2
        print("\n{}'s health is: {}".format(enemy.name, enemy.health))


def slash_attack():
    hit_or_crit = random.randint(1, 21)
    if hit_or_crit <= 5:
        print("\nYou miss!")
    elif 5 < hit_or_crit < 20:
        enemy.health -= player.attack() + 5
        print("\nYou hit!")
        print("\n{}'s health is: {}".format(enemy.name, enemy.health))
    else:
        enemy.health -= player.attack() * 2
        print("\nCritical slash!")
        print("\n{}'s health is: {}".format(enemy.name, enemy.health))


def enemy_attack():
    hit_or_crit = random.randint(1, 21)
    if hit_or_crit <= 5:
        print("\n{}'s attack misses!".format(enemy.name))
    elif 5 < hit_or_crit < 20:
        player.health -= enemy.attack()
        print("\n{}'s attack lands!".format(enemy.name))
        print("\n{}'s health is: {}".format(player.name, player.health))
    else:
        player.health -= enemy.attack() * 2
        print("\n{} lands a Critical attack!".format(enemy.name))
        print("\n{}'s health is: {}".format(player.name, player.health))


def fight_on():
    turn = whos_turn()
    print("\n{} vs {}".format(player.name, enemy.name))
    print("{} goes first!".format(turn))

    while player.health > 0 and enemy.health > 0:
        if turn == 'Fuggs':
            print("\n~~~{}'s Turn~~~".format(player.name))
            combat()
            if death_check():
                pass
            else:
                turn = enemy.name

        else:
            print("\n~~~{}'s turn!~~~".format(enemy.name))
            enemy_attack()
            if death_check():
                pass
            else:
                turn = "Fuggs"


player = Character()


enemy = Baddie("Skeleton")


def path_b_skeleton_battle():
    while player.health > 1:
        PathBLore.skeleton_fight()
        fight_on()
        PathBLore.skeleton_defeat()
        break


def path_b_zombie_battle():
    while player.health > 1:
        global enemy
        enemy = Baddie("Zombie")
        fight_on()
        PathBLore.zombie_defeat()
        PathBLore.after_first_fight()
        PathBLore.zombie_bear_fight()
        break


def path_b_zombie_bear():
    while player.health > 1:
        global enemy
        enemy = Baddie("Undead Lou")
        fight_on()
        break


def path_b_end():
    PathBLore.after_all_fight()
    PathC.continue_lore()
    PathC.return_lore()
    PathC.ritual_lore()
    PathBLore.path_b_hero_lore()


def path_b_final_battle():
    global enemy
    enemy = Hero()
    fight_on()
