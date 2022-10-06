import random
print(random,randint(1,3))

location = ["witchPlace", "vampireCastle", "weaponStorage"]

weaponList = ["sword", "rifle"]
weaponDamage = [300, 500]
myhealth = 3500
monsterList = ["vampire", "witch"]
monsterHealth = [1500, 2500]
monsterAttack = [500,700]
def callMonster(in_location):
    monsterInPlace = {}
    if in_location == "witchPlace":
        monsterInPlace += monsterList[2]
        monsterInPlace += monsterHealth[2]
        monsterInPlace += monsterAttack[2]
    elif in_location == "vampireCastle":
        monsterInPlace += monsterList[1]
        monsterInPlace += monsterHealth[1]
        monsterInPlace += monsterAttack[1]


def callWeapon():
    weapon = ""
    for i in weaponList:
        weapon += i + " "
    selectWeapon = input("Choose the weapon: " + weapon + "- ")
    if selectWeapon == "sword":
        selectWeapon += weaponList[1]
        selectWeapon += weaponDamage[1]
    if selectWeapon == "rifle":
        selectWeapon += weaponList[2]
        selectWeapon += weaponDamage[2]
    
    return(selectWeapon)

def fightScene():
    while monsterHealth > 0:
        monsterHealth - weaponDamage
        myhealth - monsterAttack
        
 







