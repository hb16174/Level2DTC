import random

# Text Format
HEADER = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
BYellow = '\033[93m'
BRed = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
Red = '\033[31m'
Reverse = "\x1b[7m"
Reset_Reverse = "\x1b[27m"

print(Red+"=================================================")
print(Red+"                                                 ")
print(BOLD+BRed+"                Welcome to Escape!               ")
print(Red+"                                                 ")
print("=================================================")
print(RESET+"\nYou have stolen a camel to make your way across the great Mobi Dick desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and outrun the natives.")

print("\nChoose your next steps carefully...")


distance = 1000
thirst = 10
energy = 10
ndis = 1100


while 0 <= distance <= ndis:
    print(BOLD+Red+"\n1."+RESET+" Drink from your canteen.\n"+BOLD+Red+"2."+RESET+" Ahead moderate speed.")
    print(BOLD+Red+"3. "+RESET+"Ahead full speed.\n"+BOLD+Red+"4."+RESET+" Slow down and rest.")
    print(BOLD+Red+"5. "+RESET+"Status check.\n"+BOLD+Red+"6."+RESET+" Quit.")

    choice = int(input(BOLD+BYellow+"Choose: "))

    if choice == 1:
        print("\n"+GREEN+BOLD+"You slow down a bit to take a drink from your canteen"+RESET)
        thirst += random.randint(4, 10)
        if thirst > 10:
            thirst = 10
        energy += random.randint(0, 1)
        ndis -= random.randint(10, 35)

    elif choice == 2:
        print("\n"+GREEN+BOLD+"You run for a while at a moderate speed"+RESET)
        distance -= random.randint(50, 100)
        ndis -= random.randint(10, 35)
        thirst -= random.randint(1, 3)
        energy -= random.randint(1, 3)

        if 0 > distance > ndis:
            distance = 0
            break
        print(GREEN+BOLD+"You're now "+Red, distance, GREEN+" meters away from safety")
        print("The natives are "+Red, ndis - distance, GREEN+" away from you")

    elif choice == 3:
        print("\n"+GREEN+BOLD+"You run as fast as you can"+RESET)
        distance -= random.randint(90, 130)
        ndis -= random.randint(10, 35)
        thirst -= random.randint(4, 6)
        energy -= random.randint(3, 5)

        if 0 > distance > ndis:
            distance = 0
            break
        print(GREEN+BOLD+"You're now "+Red, distance, GREEN+" meters away from safety")
        print("The natives are "+Red, ndis-distance, GREEN+" away from you")
    elif choice == 4:
        print("\n"+GREEN+BOLD+"You take a break"+RESET)
        energy += random.randint(4, 7)
        ndis -= random.randint(10, 35)
    elif choice == 5:
        print("\n"+GREEN+BOLD+"Status:")
        print(GREEN+"Distance to go:"+Red, distance)
        print(GREEN+"Thirst:"+Red, thirst)
        print(GREEN+"Energy:"+Red, energy, RESET)
        print(GREEN+BOLD+"The natives are"+Red, ndis-distance, GREEN+"meters away from you")

    elif choice == 6:
        print("\n"+GREEN+BOLD+"You give up"+RESET)
        ndis = 0

    else:
        print(Red+"That isn't an option, try again"+RESET)

    if thirst < 5:
        print(RESET+Red+"Your throat is getting dry")
    if thirst < 0:
        print(RESET+Red+"You are too dehydrated")
        ndis = distance-1
        break
    if energy < 4:
        print(RESET+Red+"You are getting tired")
    if energy <= 0:
        print(RESET+Red+"Your legs feel weak, you should probably take a break.")


if ndis > distance:
    print("\n"+BLUE+"You outran the natives")
    print("\n"+BOLD+CYAN+"You Won")
else:
    print("\n"+Red+"The natives caught up to you")
    print("\n"+BOLD+BRed+"You Lost."+RESET+Red+"You were"+BOLD+BRed, distance, RESET+Red+"meters away from safety")
