import random

class Robot:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.stunned = False
    
    # Metode untuk menyerang musuh, namun ada chance untuk meleset saat menyerang
    def attack_enemy(self, enemy):
        if self.stunned:
            print(f"{self.name} terkena stun dan tidak bisa menyerang di ronde ini!")
            self.stunned = False
            return
        if random.random() < 0.8:  # 80% sukses menyerang
            damage = self.attack
            enemy.hp -= damage
            print(f"{self.name} menyerang {enemy.name} dan memberikan {damage} damage!")
        else:
            print(f"{self.name} gagal menyerang {enemy.name}!")
    
    # Metode untuk memberi efek stun kepada musuh dan ada resiko tidak berhasil memberikan efek stun
    def stun_enemy(self, enemy):
        if random.random() < 0.7:  # 70% sukses memberi efek stun 
            enemy.stunned = True
            print(f"{self.name} berhasil memberikan stun pada {enemy.name}!")
        else:
            print(f"{self.name} gagal memberikan stun pada {enemy.name}!")

   # Metode untuk robot bisa menambah kembali HP nya 
    def heal(self):
        heal_amount = 40
        self.hp += heal_amount
        print(f"{self.name} menyembuhkan dirinya sendiri sebanyak {heal_amount} HP!")
    
    def is_defeated(self):
        return self.hp <= 0

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
    
    # Metode memulai game
    def start(self):
        round_number = 1
        while not self.robot1.is_defeated() and not self.robot2.is_defeated():
            print(f"\nRound-{round_number}")
            print(f"{self.robot1.name} HP : [{self.robot1.hp}]")
            print(f"{self.robot2.name} HP : [{self.robot2.hp}]")
            
            for robot, enemy in [(self.robot1, self.robot2), (self.robot2, self.robot1)]:
                if robot.is_defeated() or enemy.is_defeated():
                    break

                #user memilih opsi yang akan dilakukan robot pilihan
                print("\nPilih opsi : \n1. Attack \n2. Stun \n3. Heal \n4. Give up")
                action = int(input(f"{robot.name}, pilih aksi: "))
                
                if action == 1:
                    robot.attack_enemy(enemy)
                elif action == 2:
                    robot.stun_enemy(enemy)
                elif action == 3:
                    robot.heal()
                elif action == 4:
                    print(f"{robot.name} menyerah!")
                    return
            
            round_number += 1
        
        winner = self.robot1 if not self.robot1.is_defeated() else self.robot2
        print(f"\n{winner.name} menang!")

# User memilih karakter robot
robot_choices = {
    "1": Robot("Bumblebee", 500, 75),
    "2": Robot("Optimus Prime", 750, 50),
    "3": Robot("Megatron", 600, 60)
}

print("Pilih robot:")
for key, robot in robot_choices.items():
    print(f"{key}. {robot.name} (HP: {robot.hp}, Attack: {robot.attack})")

robot1_choice = input("Pilih robot pertama: ")
robot2_choice = input("Pilih robot kedua: ")

robot1 = robot_choices.get(robot1_choice, robot_choices["1"])
robot2 = robot_choices.get(robot2_choice, robot_choices["2"])

game = Game(robot1, robot2)
game.start()