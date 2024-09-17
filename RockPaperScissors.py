#ROCK, PAPER, SCISSORS
import random
print("Welcome to Rock,paper,scissors Game")
p=["Rock","paper","scissors"]
sysgen=random.choice(p)
print("1.Rock 2.paper 3. scissors")
u=input("You choose(name):")
print("system choose:",sysgen)
if sysgen==u:
    print("Tie match")
elif u=="Rock" and sysgen=="paper":          
    print(" You lose")
elif u=="Rock" and sysgen=="scissors":
    print(" Congratulations!,You win")
elif u=="paper" and sysgen=="Rock":
    print("You Win! ")
elif u=="paper" and sysgen=="scissors": 
    print("You lose!")                                                                       
elif u=="scissors" and sysgen=="paper": 
    print(" Congratulations!,You win")
elif u=="scissors" and sysgen=="Rock": 
    print("You lose!")
