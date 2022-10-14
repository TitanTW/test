directions = ["left", "right" ,"forward"]

def startPoint():
    choice = ""
    for i in directions:
         choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == directions[0]:
        skeletonHideout()
    elif selected == directions[1]:
        vampireCastle()
    elif selected == directions[2]: 
        walkway()


def skeletonHideout():
    print("You are in the skeleton hideout")
    choice = ""
    for i in directions:
         choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == directions[0]:
        hell()
    elif selected == directions[1]:
        fairyHouse()
    elif selected == directions[2]: 
        walkway()

def vampireCastle():
    print("You are in the vampire castle")
    choice = ""
    directions.append("backward")
    for i in directions:
         choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == directions[0]:
        witchPlace()
    elif selected == directions[1]:
        walkway()
    elif selected == directions[2]: 
        dragonDen()

def walkway():
    print("Keep walking")
    choice = ""
    for i in directions:
         choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == directions[0]:
        weaponStorage()
    elif selected == directions[1]:
        fairyHouse()
    elif selected == directions[2]: 
        monsterJungle()

def dragonDen():
    print("Welcome to the Dragon's Den...")
    choice = ""
    for i in directions:
         choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == directions[0]:
        fairyHouse()
    elif selected == directions[1]:
        monsterJungle()
    elif selected == directions[2]: 
        vampireCastle()
def fairyHouse():
    print("You are in the Fairy House...")
    choice = ""
    for i in directions:
         choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == directions[0]:
        weaponStorage()
    elif selected == directions[1]:
        witchPlace()
    elif selected == directions[2]: 
        skeletonHideout()
def vampireCastle():
    print("Watch out the Monster Jungle!")
    choice = ""
    for i in directions:
         choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == directions[0]:
        hell()
    elif selected == directions[1]:
        weaponStorage()
    elif selected == directions[2]: 
        witchPlace()
def hell():
    print("Welcome to the underworld...")
    print("This is the final boss")

def witchPlace():
    print("Welcome to the Witches' Place")
    choice = ""
    for i in directions:
         choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == directions[0]:
        weaponStorage()
    elif selected == directions[1]:
        fairyHouse()
    elif selected == directions[2]: 
        monsterJungle()


def weaponStorage():
    print("Weapons everywhere!!!")
    choice = ""
    for i in directions:
         choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == directions[0]:
        vampireCastle()
    elif selected == directions[1]:
        skeletonHideout()
    elif selected == directions[2]: 
        monsterJungle()



startPoint()




