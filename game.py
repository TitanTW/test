
import test2
import sys
previous_location = ""
holding_weapon = []
holding_weapon_damage = []
def startPoint():
    print("The game has started, please grab a weapon...")
    print("-----------------------------------------------")
    global first_weapon
    global holding_weapon
    global holding_weapon_damage   
    first_weapon = test2.weaponList #weapon list
    choice = ""
    for i in first_weapon: 
        choice += str(first_weapon.index(i)) + "." + i + " " #weapon choices
    selected = int(input("Choose the weapon (pick a number): " + choice + " - ")) # input number
    holding_weapon.append(test2.weaponList[selected])
    holding_weapon_damage.append(test2.weaponDamage[selected])
    print("you are holding a "+ holding_weapon[0]) 
    

    direction_choices = ["left","right","forward"]
    choice = ""
    for i in direction_choices:
        choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == direction_choices[0]:
        skeletonHideout()
    elif selected == direction_choices[1]:
        vampireCastle()
    elif selected == direction_choices[2]: 
        walkway()
def skeletonHideout():
    test2.callMonster("skeletonHideout")
    test2.fightScene()
    if  test2.myhealth <= 0:

        print("GAME OVER...")
        restart = input("hit 1 to Restart/hit 2 to End: ")
        if restart == "1":
            startPoint()
        elif restart == "2":
            sys.exit()
    print("You are in the skeleton hideout")
    print("-----------------------------------------------")
    print("-----------------------------------------------")
    direction_choices = ["left","right","forward"]

    choice = ""
    for i in direction_choices:
        choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == direction_choices[0]:
        chest2()
    elif selected == direction_choices[1]:
        walkway()
    elif selected == direction_choices[2]: 
        monsterJungle()
    previous_location = skeletonHideout()
def vampireCastle():
    test2.callMonster("vampireCastle")
    test2.fightScene()
    if  test2.myhealth <= 0:

        print("GAME OVER...")
        restart = input("hit 1 to Restart/hit 2 to End: ")
        if restart == "1":
            startPoint()
        elif restart == "2":
            sys.exit()
    print("You are in the vampire castle")
    print("-----------------------------------------------")
    direction_choices = ["left","right","forward"]
    print("-----------------------------------------------")
    choice = ""
    direction_choices.append("backward")
    for i in direction_choices:
        choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == direction_choices[0]:
        walkway()
    elif selected == direction_choices[1]:
        chest2()
    elif selected == direction_choices[2]: 
        dragonDen()
    previous_location = vampireCastle()
def walkway():
    print("Keep walking")
    print("-----------------------------------------------")
    direction_choices = ["left","right","forward"]
    print("-----------------------------------------------")
    choice = ""
    for i in direction_choices:
        choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == direction_choices[0]:
        monsterJungle()
    elif selected == direction_choices[1]:
        dragonDen()
    elif selected == direction_choices[2]: 
        witchPlace()
    previous_location = walkway()
def dragonDen():
    test2.callMonster("dragonDen")
    test2.fightScene()
    if  test2.myhealth <= 0:

        print("GAME OVER...")
        restart = input("hit 1 to Restart/hit 2 to End: ")
        if restart == "1":
            startPoint()
        elif restart == "2":
            sys.exit()
    print("Welcome to the Dragon's Den...")
    print("-----------------------------------------------")
    direction_choices = ["left","right","forward"]
    print("-----------------------------------------------")
    choice = ""
    for i in direction_choices:
        choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == direction_choices[0]:
        walkway()
    elif selected == direction_choices[1]:
        fairyHouse()
    elif selected == direction_choices[2]: 
        chest3()
    previous_location = dragonDen()
def fairyHouse():
    test2.callMonster("fairyHouse")
    test2.fightScene()
    if  test2.myhealth <= 0:

        print("GAME OVER...")
        restart = input("hit 1 to Restart/hit 2 to End: ")
        if restart == "1":
            startPoint()
        elif restart == "2":
            sys.exit()
    print("You are in the Fairy House...")
    print("-----------------------------------------------")
    direction_choices = ["left", "right","forward"]
    print("-----------------------------------------------")
    choice = ""
    for i in direction_choices:
        choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == direction_choices[0]:
        monsterJungle()
    elif selected == direction_choices[1]:
        hell()
    elif selected == direction_choices[2]:
        dragonDen()
    previous_location = fairyHouse()
def monsterJungle():
    test2.callMonster("monsterJungle")
    test2.fightScene()
    if  test2.myhealth <= 0:

        print("GAME OVER...")
        restart = input("hit 1 to Restart/hit 2 to End: ")
        if restart == "1":
            startPoint()
        elif restart == "2":
            sys.exit()
    print("Watch out the Monster Jungle!")
    print("-----------------------------------------------")
    direction_choices = ["left", "right","forward"]
    print("-----------------------------------------------")
    choice = ""
    for i in direction_choices:
        choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == direction_choices[0]:
        fairyHouse()
    elif selected == direction_choices[1]:
        walkway()
    elif selected == direction_choices[2]: 
        hell()
    previous_location = monsterJungle()
def witchPlace():
    test2.callMonster("witchPlace")
    test2.fightScene()
    if  test2.myhealth <= 0:

        print("GAME OVER...")
        restart = input("hit 1 to Restart/hit 2 to End: ")
        if restart == "1":
            startPoint()
        elif restart == "2":
            sys.exit()
    direction_choices = ["left", "right","forward"]
    print("-----------------------------------------------")
    print("Welcome to the Witches' Place")
    print("-----------------------------------------------")
    choice = ""
    for i in direction_choices:
        choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == direction_choices[0]:
        hell()
    elif selected == direction_choices[1]:
        chest3()
    previous_location = witchPlace()

def chest2():
    print("You found chest(2)")
    print("-----------------------------------------------")
    confirmPotion = input("Do you want to use a health potion- 1.Yes 2.No :")
    if confirmPotion == "1":
        test2.myhealth += 3000
    elif confirmPotion =="2":
        None
    direction_choices = ["left", "right","forward"]
    print("-----------------------------------------------")
    choice = ""
    for i in direction_choices:
        choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == direction_choices[0]:
        vampireCastle()
    elif selected == direction_choices[1]:
        skeletonHideout()
    elif selected == direction_choices[2]: 
        monsterJungle()
    previous_location = chest2()

def chest3():
    print("You found chest(3)")
    print("-----------------------------------------------")
    confirmPotion = input("Do you want to use a health potion- 1.Yes 2.No :")
    if confirmPotion == "1":
        test2.myhealth += 5000
    elif confirmPotion =="2":
        None
    direction_choices = ["left"]
    print("-----------------------------------------------")
    choice = ""
    for i in direction_choices:
        choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == direction_choices[0]:
        final()
    previous_location = chest3()
def final():
    print("You are about to enter the final zone")
    print("-----------------------------------------------")
    ready = input("Are you sure to continue,  yes/no: " )
    print("-----------------------------------------------")
    if ready == "yes":
        hell()
    elif ready == "no":
        previous_location
    print("-----------------------------------------------")
        
def hell():
    test2.callMonster("hell")
    test2.fightScene()
    if  test2.myhealth <= 0:
    
        print("GAME OVER...")
        restart = input("hit 1 to Restart/hit 2 to End: ")
        if restart == "1":
            startPoint()
        elif restart == "2":
            sys.exit()
    print("Welcome to the underworld...")
    print("This is the final boss")
    print("-----------------------------------------------")
startPoint()