#Daniel Lobos
#Text Based adventure game

import random
import PathBLore
import PathC


class Character:
    def __init__(self, name='Fuggs', weapon='Shortsword'):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.BaseDmg = 9
        self.weapon = weapon
        self.potions = 6

    def attack(self):
        Dmg = self.BaseDmg
        if self.weapon == "Shortsword":
            Dmg += 6
        elif self.weapon == "":
            Dmg = self.BaseDmg

        return Dmg


class Baddie:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.baseDmg = 5

    def attack(self):
        Dmg = self.baseDmg
        if self.name == "Zombie":
            bite = random.randint(0, 1)
            if bite == 1:
                print("Zombie tries to bite!")
                Dmg += 5
            else:
                pass
            return Dmg
        elif self.name == "Skeleton":
            Dmg += 2
        elif self.name == "Undead Lou":
            Chomp = random.randint(0, 1)
            if Chomp == 1:
                print("Undead Lou tries to Chomp!")
                Dmg += 8
            else:
                pass
            return Dmg
        return Dmg


class Hero:
    def __init__(self, name=PathC.name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.baseDmg = 20

    def attack(self):
        Dmg = self.baseDmg
        PowerStrike = random.randint(0, 5)
        if PowerStrike == 5:
            print("The intruder rears back as he unleashes a powerful blow")
            Dmg = self.baseDmg * 4
        else:
            print('You attempt to block the hit but only reduce the damage')
        return Dmg


def whosTurn():
    if random.randint(0, 1) == 0:
        return "Fuggs"
    else:
        return enemy.name


def deathCheck():
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
    FightChoiceLoop = 0
    while FightChoiceLoop == 0:
        try:
            FightChoice = int(input("1) Attack \nor \n2) Drink Potion"))
            if FightChoice == 1:
                attackOption()
                FightChoiceLoop += 1
            elif FightChoice == 2:
                DrinkPotion()
                FightChoiceLoop += 1
        except ValueError:
            print("\nThat was not one of the options, try again.")


def DrinkPotion():
    if player.potions < 1:
        print("\nYou do not have any potions left!")
    else:
        player.health += 25
        player.potions -= 1
        print("\nYou have {} health points".format(player.health))
        if player.health > 100:
            print("With", (player.health - 100) , "as temporary health points.")
        else:
            pass


def attackOption():
    selectedMove = int(input("\n1) Slash \nor \n2) Stab"))
    if selectedMove == 1:
        slashAttack()
    elif selectedMove == 2:
        stabAttack()
    else:
        selectedMove = int(input("\n1) Slash \t 2) Stab \n3) Dodge"))


def stabAttack():
    HorC = random.randint(1, 21)
    if HorC <= 19:
        print("\nYou hit!")
        enemy.health -= player.attack()
        print("\n{}'s health is: {}".format(enemy.name, enemy.health))
    else:
        print("\nCritical stab!")
        enemy.health -= player.attack() * 2
        print("\n{}'s health is: {}".format(enemy.name, enemy.health))


def slashAttack():
    HorC = random.randint(1, 21)
    if HorC <= 5:
        print("\nYou miss!")
    elif 5 < HorC < 20:
        enemy.health -= player.attack() + 5
        print("\nYou hit!")
        print("\n{}'s health is: {}".format(enemy.name, enemy.health))
    else:
        enemy.health -= player.attack() * 2
        print("\nCritical slash!")
        print("\n{}'s health is: {}".format(enemy.name, enemy.health))


def enemyattack():
    HorC = random.randint(1, 21)
    if HorC <= 5:
        print("\n{}'s attack misses!".format(enemy.name))
    elif 5 < HorC < 20:
        player.health -= enemy.attack()
        print("\n{}'s attack lands!".format(enemy.name))
        print("\n{}'s health is: {}".format(player.name, player.health))
    else:
        player.health -= enemy.attack() * 2
        print("\n{} lands a Critical attack!".format(enemy.name))
        print("\n{}'s health is: {}".format(player.name, player.health))


def fightOn():
    turn = whosTurn()
    print("\n{} vs {}".format(player.name, enemy.name))
    print("{} goes first!".format(turn))

    while player.health > 0 and enemy.health > 0:
        if turn == 'Fuggs':
            print("\n~~~{}'s Turn~~~".format(player.name))
            combat()
            if deathCheck():
                pass
            else:
                turn = enemy.name

        else:
            print("\n~~~{}'s turn!~~~".format(enemy.name))
            enemyattack()
            if deathCheck():
                pass
            else:
                turn = "Fuggs"

player = Character()
enemy = Baddie("Skeleton")


def PathBSkeletonBattle():
    while player.health > 1:
        PathBLore.SkeletonFight()
        fightOn()
        PathBLore.SkeletonDefeat()
        break


def PathBZombieBattle():
    while player.health > 1:
        global enemy
        enemy = Baddie("Zombie")
        fightOn()
        PathBLore.ZombieDefeat()
        PathBLore.AfterFirstFight()
        PathBLore.ZombieBearFight()
        break


def PathBZombieBear():
    while player.health > 1:
        global enemy
        enemy = Baddie("Undead Lou")
        fightOn()
        break


def PathBEnd():
    PathBLore.afterAllFights()
    PathC.continueLore()
    PathC.ReturnLore()
    PathC.RitualLore()
    PathBLore.PathBHeroLore()


def PathBFinalBattle():
    global enemy
    enemy = Hero()
    fightOn()

