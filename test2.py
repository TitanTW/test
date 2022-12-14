import random
import sys
location = ["witchPlace", "vampireCastle","dragonDen","fairyHouse","monsterJungle","hell","skeletonHideout","walkway","weaponStorage"]

weaponList = ["sword", "bow"]
weaponDamage = [300, 500]
myhealth = 12000
maxhealth = 12000
monsterList = ["vampire", "witch","Dragon's Den","Fairy's house","Monster's Jungle","Hell","Skeletons' Hideout"]
monsterHealth = [1500,2500, 2000,3000,2700,10000,1800]
monsterAttack = [500,700,800,400,600,1000,200]
def foundPotion():
    potionList = [0.1,0.2,0.3,0.5,0.7]
    myhealth += maxhealth * potionList[random.randint(0,4)]
def callMonster(in_location):
    
    global monsterInPlace_name
    global monsterInPlace_health
    global monsterInPlace_attack
    monsterInPlace_name = ""
    monsterInPlace_health = 0
    monsterInPlace_attack= 0
    print(in_location)
    if in_location == "vampireCastle":
        monsterInPlace_name += monsterList[0]
        monsterInPlace_health += monsterHealth[0]
        monsterInPlace_attack += monsterAttack[0]
    elif in_location == "witchPlace":
        monsterInPlace_name += monsterList[1]
        monsterInPlace_health += monsterHealth[1]
        monsterInPlace_attack += monsterAttack[1]
    elif in_location == "dragonDen":
        monsterInPlace_name += monsterList[2]
        monsterInPlace_health += monsterHealth[2]
        monsterInPlace_attack += monsterAttack[2]
    elif in_location == "fairyHouse":
        monsterInPlace_name += monsterList[3]
        monsterInPlace_health += monsterHealth[3]
        monsterInPlace_attack += monsterAttack[3]
    elif in_location == "monsterJungle":
        monsterInPlace_name += monsterList[4]
        monsterInPlace_health += monsterHealth[4]
        monsterInPlace_attack += monsterAttack[4]
    elif in_location == "hell":
        monsterInPlace_name += monsterList[5]
        monsterInPlace_health += monsterHealth[5]
        monsterInPlace_attack += monsterAttack[5]
    elif in_location == "skeletonHideout":
        monsterInPlace_name += monsterList[6]
        monsterInPlace_health += monsterHealth[6]
        monsterInPlace_attack += monsterAttack[6]

def callWeapon():
    weapon = ""
    for i in weaponList:
        weapon += str(weaponList.index(i) + 1) + ". " + i + "\n"
    selectWeapon = input("Choose the weapon: " + "\n" + weapon + "- ")
    if selectWeapon == "1":
        selectWeapon += weaponList[1]
        selectWeapon += weaponDamage[1]
    if selectWeapon == "bow":
        selectWeapon += weaponList[2]
        selectWeapon += weaponDamage[2]
    
    return(selectWeapon)

def fightScene():

    global monsterInPlace_health
    global myhealth
    print(myhealth)
    print(monsterInPlace_health)
    print(monsterInPlace_attack)
    while monsterInPlace_health > 0 and myhealth > 0:

        temp = random.randint(1,2)
        if temp == 1:
            monsterInPlace_health -= 300 #monster's health subtracted by weapon damage
            print("\nYou attacked the monster!")
            
        elif temp == 2:
            myhealth -= monsterInPlace_attack #health decreasing from monster attack
            print("\nThe monster hit you!")
        input("\nENTER ")
        print("\nMy health:" + str(myhealth))
        print("Monster's health: " + str(monsterInPlace_health))
    if myhealth <= 0:
        print("you lost")
        
        
    elif monsterInPlace_health <= 0:
        print("you won")
    

callMonster(location[0])
print(monsterInPlace_name, str(monsterInPlace_health), str(monsterInPlace_attack))