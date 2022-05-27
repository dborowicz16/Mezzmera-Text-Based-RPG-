import random

class character:
    name = ""
    classChoice = ""
    strength = 0
    health = 0
    stealth = 0
    totalMonsterKilled = 0

class bear:
    name = "bear"
    health = 75
    strength = 20
    stealth = 25

class wolf:
    name = "wolf"
    health = 50
    strength = 15
    stealth = 50

class shark:
    name = "shark"
    health = 75
    strength = 20
    stealth = 25

class perrywinkle:
    name = "perrywinkle"
    health = 100
    strength = 75
    stealth = 75

class monster:
    name = ""
    health = 0
    strength = 0
    stealth = 0

monsters = [bear, wolf, shark, perrywinkle]
    

character = character()

# Prompts user to input a name for their character
def nameSelection():
    character.name = input("What is your character's name?")
    confirmName = input("You said your name is " + str(character.name) + " right?")

    if confirmName == "yes":
        print(str(character.name) + " huh? That's a neat name!")
        classSelection()
    elif confirmName == "no":
        nameSelection()
    else:
        print("Must input 'yes' or 'no'!")
        nameSelection()

def checkCharacterDeath():
    if character.health <= 0:
        print("Your character dies!")
        print("You killed " + str(character.totalMonsterKilled) + " monster(s)!")

        choice = input("Would you like to play again?")
        if choice == "yes":
            nameSelection()
        elif choice == "no":
            print("Thank you for playing!")
            quit()
        else:
            print("Must input 'yes' or 'no'!")
            checkCharacterDeath()
    
    elif character.health > 0:
        attackOrHeal()

def checkMonsterDeath():
    if monster.health <= 0:
        print("You killed the " + str(monster.name) + "!")
        character.totalMonsterKilled = character.totalMonsterKilled + 1
        battleStarts()
    if monster.health > 0:
        monsterAttack()

def monsterAttack():
    if character.classChoice == "paladin":
        randomNumber = random.randrange(0, 4)
        if randomNumber == 1: # Monster attack misses
            print("The " + str(monster.name) + " missed!")
            attackOrHeal()
        else: # Monster attack hits
            character.health = character.health - monster.strength
            print("The " + str(monster.name) + " hit you for " + str(monster.strength) + " HP and you now have " + str(character.health) + " HP left!")
            checkCharacterDeath()

    if character.classChoice == "thief":
        randomNumber = random.randrange(0, 2)
        if randomNumber == 1: # Monster attack misses
            print("The " + str(monster.name) + " missed!")
            attackOrHeal()
        else: # Monster attack misses
            character.health = character.health - monster.strength
            print("The " + str(monster.name) + " hit you for " + str(monster.strength) + " HP and you now have " + str(character.health) + " HP left!")
            checkCharacterDeath()
    
    if character.classChoice == "berzerker":
        randomNumber = random.randrange(0, 10)
        if randomNumber == 1: # Monster attack misses
            print("The " + str(monster.name) + " missed!")
            attackOrHeal()
        else: # Monster attack hits
            character.health = character.health - monster.strength
            print("The " + str(monster.name) + " hit you for " + str(monster.strength) + " HP and you now have " + str(character.health) + " HP left!")
            checkCharacterDeath()

  

# Prompts user to attack or heal and adjusts character/monster stats accordingly
def attackOrHeal():
    choice = input("Do you want to attack the monster or heal?")

    if choice == "attack":
        if monster.stealth == 25:
            randomNumber = random.randrange(0, 4)
            if randomNumber == 1: # Character attack misses
                print("Your attack missed!")
                monsterAttack()
            else:
                monster.health = monster.health - character.strength
                print("You hit the " + str(monster.name) + " for " + str(character.strength) + " HP! It now has " + str(monster.health) + " HP left!")
                checkMonsterDeath()
                monsterAttack()
        
        if monster.stealth == 50:
            randomNumber = random.randrange(0, 2)
            if randomNumber == 1:
                print("Your attack missed!")
                monsterAttack()   
            else:
                monster.health = monster.health - character.strength
                print("You hit the " + str(monster.name) + " for " + str(character.strength) + " HP! It now has " + str(monster.health) + " HP left!")
                checkMonsterDeath()
                monsterAttack()  
        
        if monster.stealth == 75:
            randomNumber = random.randrange(0, 3)
            if randomNumber == 1 or randomNumber == 2:
                print("Your attack missed!")
                monsterAttack()
            else:
                monster.health = monster.health - character.strength
                print("You hit the " + str(monster.name) + " for " + str(character.strength) + " HP! It now has " + str(monster.health) + " HP left!")
                checkMonsterDeath()
                monsterAttack() 

    elif choice == "heal":
        hitPointsGained = random.randrange(5, 25)
        character.health = character.health + hitPointsGained
        print("You gained " + str(hitPointsGained) + " HP and now have " + str(character.health) + " HP total!")
        monsterAttack()
    
    else:
        print("Must input 'attack' or 'heal'!")
        attackOrHeal()

# Selects a random monster from list
def randomMonster():
    randomMonster = random.choice(monsters)

    monster.name = randomMonster.name
    monster.health = randomMonster.health
    monster.strength = randomMonster.strength
    monster.stealth = randomMonster.stealth

# Starts battle
def battleStarts():
    randomMonster()

    print("A " + str(monster.name) + " has appeared!")

    attackOrHeal()

# Prompts user to select a class for character
def classSelection():
    characterClass = input("Are you a paladin, thief, or berzerker?")

    if characterClass != "paladin" and characterClass != "thief" and characterClass != "berzerker":
        print("You must input 'paladin', 'thief', or 'berzerker'!")
        classSelection()
    elif characterClass == "paladin" or characterClass == "thief" or characterClass == "berzerker":
        character.classChoice = characterClass

    confirmClass = input("So your name is " + str(character.name) + " and you are a " + str(character.classChoice) + "?")

    if confirmClass == "yes":
        if character.classChoice == "paladin":
            character.strength = 50
            character.health = 100
            character.stealth = 25
        elif character.classChoice == "thief":
            character.strength = 10
            character.health = 25
            character.stealth = 50
        elif character.classChoice == "berzerker":
            character.strength = 75
            character.health = 75
            character.stealth = 10
        battleStarts()

    elif confirmClass == "no":
        nameSelection()
    
    else:
        print("Must input 'yes' or 'no'!")
        classSelection()


print("Welcome to Mezzmera!")

nameSelection()
