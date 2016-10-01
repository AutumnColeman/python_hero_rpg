"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        if enemy.health == 0:
            if enemy.name == "goblin":
                self.coins += 5
            elif enemy.name == "wizard":
                self.coins += 6
            elif enemy.name == "shadow":
                self.coins += 5
            else:
                self.coins += 4

        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Shadow(Character):
    def __init__(self):
        self.name = "shadow"
        self.health = 1
        self.power = 2

    def receive_damage(self, points):
        damage_power = random.random() < 0.1
        if damage_power:
            self.health -= points
            print "%s received %d damage." % (self.name, points)
            if self.health <= 0:
                print "%s is dead." % self.name

class Zombie(Character):
    def __init__(self):
        self.name = "zombie"
        self.health = 10
        self.power = 3

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)

    def alive(self):
        return True


class Medic(Character):
    def __init__(self):
        self.name ='medic'
        self.health = 7
        self.power = 3

        # self.is_attacked = False
    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name
        health_hp = random.random() > 0.2
        if health_hp:
            self.health += 2
            print "Medic's heath is restored to %d!" % self.health
            time.sleep(1)

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 2
        self.coins = 20
        self.attack_counts = 0
        self.armour = 0
        self.evade = 0
        self.evade_prob = 0
        self.tonic = 0

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

    def receive_damage(self, points):
        is_flee = random.random() * self.evade_prob
        if is_flee:
            return
        else:
            pass
        points = points - self.armour
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name
        # else:
        #      raw_input("Do you want to use a tonic? ")
        #      print "Do you want to use tonic now or save for later?"
        #      print "1. Use now"
        #      print "2. Save for later"
        #      tonic_now = int(raw_input("> "))
        #      if tonic_now == 1:
        #          self.health += 2
        #          print "%s's health increased to %d." % (self.name, self.health)

    # def receive_damage(self, enemy):
    #     super(Hero, self).receive_damage(enemy)
    #     print "Points: %r" % enemy.power


    def double_damage(self, enemy):
        damage_power = random.random() < 0.2
        if damage_power:
            self.power = 10
            print "%s gives double damage!" % self.name

    def attack(self, enemy):
        if not self.alive():
            return
        self.double_damage(enemy)
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        self.power = 5
        time.sleep(1.5)


class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Demogorgon(Character):
    def __init__(self):
        self.name = 'demogorgon'
        self.health = 20
        self.power = 6




class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            return True
        else:
            print "YOU LOSE!"
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def use_tonic(self, character):
        print "Do you want to use tonic now or save for later?"
        print "1. Use now"
        print "2. Save for later"
        tonic_now = int(raw_input("> "))
        if tonic_now == 2:
            return
        else:
            pass
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)
        # print "Do you want to use tonic now or save for later?"
        # print "1. Use now"
        # print "2. Save for later"
        # tonic_now = int(raw_input("> "))
        # if tonic_now == 1:
        #
        # else:
        #     hero.tonic

class Sword(object):
    cost = 10
    name = 'sword'
    # print "Power Before: %r" % hero.power
    def apply(self, hero):
        # print "Power Before: %r" % hero.power
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)
        # print "Power After: %r" % hero.power

    # print "Power After: %r" % hero.power

class SuperTonic(Tonic):
    cost = 9
    name = "supertonic"
    def apply(self, character):
        character.health += 10
        print "%s's health increased to %d." % (character.name, character.health)

class Armour(Sword):
    cost = 7
    name = "armour"
    def apply(self, hero):
        hero.armour += 2
        print "%s's armour increased to %d." % (hero.name, hero.armour)

class Evade(object):
    cost = 7
    name = "evade"
    def apply(self, hero):
        if hero.evade == 95:
            hero.evade = 95
        else:
            hero.evade += 2
        hero.evade_prob += 0.05
        print "%s's armour increased to %d." % (hero.name, hero.evade)



class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    # def __init__(self):
    #     is_shopping = self.do_shopping(hero)

    items = [Tonic, Sword, Armour, Evade]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins

            lowest_cost = 10
            for i in xrange(len(Store.items)):
                if Store.items[i].cost <= lowest_cost:
                    lowest_cost = Store.items[i].cost

            if hero.coins < lowest_cost:
                print "You do not have enough to purchase an item."
                return

            print "Lowest Cost: %r" % lowest_cost
            # print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)

            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)



hero = Hero()
# enemies = [Shadow(), Zombie(), Medic(), Goblin(), Wizard()]
enemies = [Goblin()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
