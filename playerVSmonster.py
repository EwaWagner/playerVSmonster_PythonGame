import time
import random

time.sleep(1)
print("State what is your name \n")
username = input()
time.sleep(1)
print("\n" + username + ", you will be now fighting monsters\n")
time.sleep(1)
print("\nLets see how long you will last.")

#player's stats
playerHP = 100
playerATK = 20
playerSMASH = 75
playerSMASHcooldown = 2 

#monster's name, HP, and Attack
monsters = [
    ["Bronia", 100,  5], 
    ["Teresa", 150, 20], 
    ["Kiara",  200, 10]
]

while playerHP>0:
    enemy = random.choice(monsters)
    print("\nYou are now fighting, " + enemy[0])
    time.sleep(1)
    while playerHP>0 and enemy[1]>0:
        print("\n" + username + " HP: " + str(playerHP))
        print(enemy[0] + " HP: " + str(enemy[1]) + "\n")
        print("you have two movesets, ATK or smash")
        choice = input()
        if choice == "ATK" or choice == "atk" or choice == "attack":
            enemy[1] = enemy[1] - playerATK
            time.sleep(1)
            print("\nyou successful hit the monster.")
            playerHP = playerHP - enemy[2]
            time.sleep(1)
            print("the monster struck you back")

        

    playerHP = 0