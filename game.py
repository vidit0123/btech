import random

def game(comp,you):
    if comp==you:
        return None
    elif comp=="r":
        if you=="p" :
            return True
        elif you=="s":
            return False
        
    elif comp=="s":
        if you=="r":
            return True
        elif you=="p":
            return False
        
    elif comp=="p":
        if you=="s":
            return True
        elif you=="r"or"rock":
            return False     


rand_no = random.randint(1,3)
if rand_no==1:
    comp = "r"
elif rand_no==2:
    comp = "p"
elif rand_no==3:
    comp = "s"


print("comp:rock(r), paper(p), scissors(s)")
you = input("your turn :rock(r), paper(p) or  scissors(s): ")
a = (game(comp,you))

print(f"comp had chosen:{comp}")
print(f"you had chosen:{you}")

if a==None:
    print("its a tie")
elif a:
    print("you won")
else:
    print("you lose, better luck next time")

