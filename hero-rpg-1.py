"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character(object):
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        return enemy.health - self.power

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        #Or use return self.health > 0
    def print_health_status(self):
        return self.health

class Zombie(Character):
    def __init__(self):
        self.health = 100
        self.power = 4

    def regenerate(self):
        self.health = 100

hercules = Character(10, 5)
tok = Character(6, 2)
ghouler_undead = Zombie()


while tok.alive() and hercules.alive():
    print "You have %d health and %d power." % (hercules.print_health_status(), hercules.power)
    print "The goblin has %d health and %d power." % (tok.print_health_status(), tok.power)
    print
    print "What do you want to do?"
    print "1. fight goblin"
    print "2. do nothing"
    print "3. flee"
    print "> ",
    input = raw_input()
    if input == "1":
        # Hero attacks goblin
        #hercules.attack(tok)
        tok.health = hercules.attack(tok)
        print "You do %d damage to the goblin." % hercules.power
        if tok.health <= 0:
            print "The goblin is dead."
    elif input == "2":
        pass
    elif input == "3":
        print "Goodbye."
        break
    else:
        print "Invalid input %r" % input

    if tok.health > 0:
        # Goblin attacks hero
        #tok.attack(hercules)
        hercules.health = tok.attack(hercules)
        print "The goblin does %d damage to you." % tok.power
        if hercules.health <= 0:
            print "You are dead."

    print "What do you want to do?"
    print "1. fight zombie"
    print "2. do nothing"
    print "3. flee"
    print "> ",
    input = raw_input()
    if input == "1":
        # Hero attacks goblin
        #hercules.attack(tok)
        # ghouler_undead.health = hercules.attack(tok)
        print "You do %d damage to the zombie." % hercules.power
        print "The zombie has %d health and %d power." % (ghouler_undead.health, ghouler_undead.power)
            # print "The zombie is dead."
    elif input == "2":
        pass
    elif input == "3":
        print "Goodbye."
        break
    else:
        print "Invalid input %r" % input

    if ghouler_undead.health > 0:
        # Goblin attacks hero
        #tok.attack(hercules)
        hercules.health = ghouler_undead.attack(hercules)
        print "The zombie does %d damage to you." % ghouler_undead.power
        if hercules.health <= 0:
            print "You are dead."
