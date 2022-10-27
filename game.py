
import test2

previous_location = ""

def startPoint():
    print("The game has started, please grab a weapon...")
    global first_weapon_choices
    first_weapon_choices = ["sword", "bow"]
    choice = ""
    for i in first_weapon_choices:
         choice += i + " "
    selected = input("Choose the weapon: " + choice + " - ")
    if selected == first_weapon_choices[0]:
        skeletonHideout()
    elif selected == first_weapon_choices[1]:
        vampireCastle()
   
    direction_choices = ["left","right","front"]
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
    print("You are in the skeleton hideout")
    direction_choices = ["left","right","front"]
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
    print("You are in the vampire castle")
    direction_choices = ["left","right","front"]
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
    direction_choices = ["left","right","front"]
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
    print("Welcome to the Dragon's Den...")
    direction_choices = ["left","right","front"]
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
    print("You are in the Fairy House...")
    direction_choices = ["left", "right","forward"]
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
    print("Watch out the Monster Jungle!")
    direction_choices = ["left", "right","forward"]
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
    direction_choices = ["left", "right","forward"]
    print("Welcome to the Witches' Place")
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
    direction_choices = ["left", "right","forward"]
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
    direction_choices = ["left"]
    choice = ""
    for i in direction_choices:
        choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == direction_choices[0]:
        hell()
    previous_location = chest3()

def final():
    print("You are about to enter the final zone")
    ready = input("Are you sure to continue,  yes/no: " )
    if ready == yes:
        hell()
    elif ready == no:
        previous_location

        

def hell():
    print("Welcome to the underworld...")
    print("This is the final boss")

startPoint()




