import random
import json




playerHp = 100
enemyHp = 100

def save(quit,playerHp,enemyHp):
    save_data = {
        "playerHp": playerHp,
        "enemyHp": enemyHp
    }
    try:
        with open("data.json", "w") as file:
            json.dump(save_data, file, indent=4)
            print("Saved")
            quit = True
            return quit
    except:
        print("Failed")
        quit = False
        return quit
def load():
    global playerHp, enemyHp  
    
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            

            playerHp = data["playerHp"]
            enemyHp = data["enemyHp"]
            print("Game Loaded!")

            print(f"Players Hp {playerHp}")
            print(f"Enemys Hp {enemyHp}")
            game(playerHp,enemyHp)
            
    except FileNotFoundError:
        print("No save file found. Starting fresh.")





def game(playerHp,enemyHp):

    def view():
        print(f"Players Hp {playerHp}")
        print(f"Enemys Hp {enemyHp}")

    def HPUP(playey):
        if playey > 100:
            return 100
        else:
            return playey
    def HPDOWN(player):
        if player < 0:
            return 0
        else:
            return player



    while True:
        print("""
        1. Attack
        2. Heal
        3. Save And Quit
        """)
        
        i = input(">> ")
        if i == "1":
            attack = random.randrange(30,40)
            enemyHp -= attack
            enemyHp = HPDOWN(enemyHp)
            print(f"You Attcked The enemy they lost {attack}HP")
            view()
        elif i == "2":
            heal = random.randrange(20,40)
            playerHp += heal
            playerHp = HPUP(playerHp)
            print(f"Healed {heal}HP")
            view()
        elif i == "3":
            quit = False
            quit = save(quit,playerHp,enemyHp)
            if quit:
                break
            else:
                print("There was an Error We will not close")

        if enemyHp == 0:
            print("You Won")
            break


        choice = random.choices([1, 2], weights=[70, 30])[0]

        if choice == 1:
            attack = random.randrange(30,40)
            playerHp -= attack
            playerHp = HPDOWN(playerHp)
            print(f"Enemy Attcked You you lost {attack}HP")
            view()
        elif choice == 2:
            heal = random.randrange(20,40)
            enemyHp += heal
            enemyHp = HPUP(enemyHp)
            print(f"Enemy Healed {heal}HP")
            view()
        if playerHp == 0:
            print("You Lost")
            break

while True:

    print("""
    1. Start new game
    2. Load game
    3. Exit""")
    m = input(">>")
    if m == "1":
        game(playerHp,enemyHp)
    if m == "2":
        load()
    if m == "3":
        break

