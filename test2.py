import random

location = ["skeletonHideout", "vampireCastle", "dragonDen" , "fairyHouse", "monsterJungle", "hell", "witchPlace", "weaponStorage"]

weaponList = ["sword", "rifle"]
weaponDamage = [300, 500]
myhealth = 3500

monsterList = ["vampire", "witch"]
monsterHealth = [1500, 2500]
monsterAttack = [500,700]


def callMonster(in_location):

    global monsterInPlace_name
    global monsterInPlace_health
    global monsterInPlace_attack
    
    monsterInPlace_name = ""
    monsterInPlace_health = 0
    monsterInPlace_attack = 0


    if in_location == "witchPlace":
        monsterInPlace_name += monsterList[1]
        monsterInPlace_health += monsterHealth[1]
        monsterInPlace_attack += monsterAttack[1]
        
    elif in_location == "vampireCastle":
        monsterInPlace_name += monsterList[0]
        monsterInPlace_health += monsterHealth[0]
        monsterInPlace_attack += monsterAttack[0]


def callWeapon():
    weapon = ""
    for i in weaponList:
        weapon += str(weaponList.index(i) + 1) + ". " + i + "\n"
    selectWeapon = input("Choose the weapon: " + "\n" + weapon + "- ")
    if selectWeapon == "1":
        selectWeapon += weaponList[0]
        selectWeapon += weaponDamage[0]
    if selectWeapon == "rifle":
        selectWeapon += weaponList[1]
        selectWeapon += weaponDamage[1]
    
    return(selectWeapon)

def fightScene():
    while monsterHealth > 0:

        temp = random.randint(1,2)
        if temp == 1:
            monsterHealth -= weaponDamage #monster's health subtracted by weapon damage
            
        elif temp == 2:
            myhealth -= monsterAttack #health decreasing from monster attack
    
callMonster(location[0])
print(monsterInPlace_name, str(monsterInPlace_health), str(monsterInPlace_attack))