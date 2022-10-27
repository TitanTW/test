
import test2

previous_location = ""
holding_weapon = ""
def startPoint():
    print("The game has started, please grab a weapon...")
    print("-----------------------------------------------")
    global first_weapon_choices
    global holding_weapon

    first_weapon_choices = test2.weaponList #weapon list
    choice = ""
    for i in first_weapon_choices: 
         choice += str(first_weapon_choices.index(i)) + "." + i + " " #weapon choices
    selected = int(input("Choose the weapon (pick a number): " + choice + " - ")) # input number
    holding_weapon += first_weapon_choices[selected]
    print("you are holding a "+ holding_weapon) 
   
 
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
    test2.callMonster(skeletonHideout)
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
    test2.callMonster(vampireCastle)
    test2.fightScene()
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
    direction_choices = ["left"]
    print("-----------------------------------------------")
    choice = ""
    for i in direction_choices:
        choice += i + " "
    selected = input("Choose the direction: " + choice + " - ")
    if selected == direction_choices[0]:
        hell()
    previous_location = chest3()

def final():
    print("You are about to enter the final zone")
    print("-----------------------------------------------")
    ready = input("Are you sure to continue,  yes/no: " )
    print("-----------------------------------------------")
    if ready == yes:
        hell()
    elif ready == no:
        previous_location
    print("-----------------------------------------------")

        

def hell():
    print("Welcome to the underworld...")
    print("This is the final boss")
    print("-----------------------------------------------")

startPoint()




