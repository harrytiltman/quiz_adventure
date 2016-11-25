# An adventure game
from random import randint
from time import sleep

health = 5
ammo = 6


def title():
    print("--- - - ---")
    print("| | | | | |")
    print("--- | | | |")
    print("| \ --- | |")
    answer = input("press a to start: ")
    room1()

def status():
    print("==========================================")
    print("   Ammo:",ammo)
    print("==========================================")

def room1():
    global health,ammo
    status()
    print(" o    -YOU!")
    print("-|-")
    print("/ \ ")
    print("You are being chased by the police")
    print("What do you do")
    print("A. Run in front of them")
    print("B. Hide")
    answer = input("Choose an option: ")
  
    if answer.lower() == "a":
        print("You are going to jail")
        jail()

    elif answer.lower() == "b":
        print("You escaped")
        ammo = ammo + 1

    else:
        print("that is not an option")
        room1()
        return

    room2()

def room2():
    global health,ammo
    status()
    print(" o    -YOU!")
    print("-|-")
    print("/ \ ")
    print("you have been spoted on the metro")
    print("What do you do")
    print("A. Discuise yourself")
    print("B. Blow the train up")
    answer = input("Choose an option: ")
    if answer.lower() == "a":
        print("You escaped")
        ammo = ammo + 1

    elif answer.lower() == "b":
        print("You are going to jail")
        jail()

    else:
        print("that is not and option")
        room2()
        return

    room3()

def room3():
    global health,ammo
    status()
    print(" o    -YOU!")
    print("-|-")
    print("/ \ ")
    print("You are running throgh the countyside on an open feild")
    print("What do you do")
    print("A. Sprint harder")
    print("B. Lie there")
    answer = input("Choose an option: ")

    if answer.lower() == "a":
        print("You escaped")
        ammo = ammo + 2
        print("You have found 2 more ammo")
    
    elif answer.lower() == "b":
        print("You are going to jail")
        jail()


    else:
        ("that is not and option")
        room3()
        return

    room4()

def room4():
    global health,ammo
    status()
    print(" o    -YOU!")
    print("-|-")
    print("/ \ ")
    print("You have hijacked a car but the police can see you")
    print("What do you do")
    print("A. Dont drive at all")
    print("B. Crash into them")
    print("C. Drive the other way")
    answer = input("insert your answer: ")

    if answer.lower() == "a":
        print("you are going to jail")
        jail()

    elif answer.lower() == "b":
        print("you are going to jail")
        jail()

    elif answer.lower() == "c":
        print("you have escaped")
        ammo = ammo + 2

    else:
        print("that is not an answer")
        room4()
        return

    room5()

    

def room5():
    global health,ammo
    status()
    print(" o    -YOU!")
    print("-|-")
    print("/ \ ")
    print("You have found your self at an airport about to bord a plane but there is an officer who recognises you")
    print("What do you do")
    print("A. Punch him")
    print("B. Dont make contact with him but he could still get you")
    print("C. Blow the place up")
    answer = input("insert your answer: ")

    if answer.lower() == "a":
        print("you are going to jail")
        jail()

    elif answer.lower() == "b":
        print("you have escaped")
        ammo = ammo + 2

    elif answer.lower() == "c":
        print("you are going to jail")
        jail()

    else:
        print("that is not an answer")
        room5()
        return

    room6()

def room6():
    global health,ammo
    status()
    print(" o    -YOU!")
    print("-|-")
    print("/ \ ")
    print("You are on a plane and the hostes is an ex prison guard at your old jail and she knows all about you")
    print("What do you do")
    print("A. Fall asleep with your hood up the whole flight")
    print("B. If she asks say im the twin")
    print("C. Go to the back of the plane and stab her")
    answer = input("insert your answer: ")

    if answer.lower() == "a":

        if ammo >= 6:
            print("Hurray your free")


        else:
            print("Jail for life")
            jail()

            



        

    elif answer.lower() == "b":
        print("you are going to jail")
        jail()

    elif answer.lower() == "c":
        print("you are going to jail")
        jail()

    else:
        print("that is not an answer")
        room6()
        return

   
    

def jail():
    global health, ammo

    ammo = 0
    health = health - 1
    print("-------")
    print("| | | |    -Your cell")
    print("| | | |")
    print("| | | |")
    print("-------")
    print("You were caught and now you are in jail")
    print("Will you escape or not...")
    sleep(3)
    print("")

    if health <= 0:
        print("You're dead sucka!")
        quit()

    
    escape = randint(1, 3)
    if escape > 1:
        print("You've escaped!")
    else:
        print("You're stuck in jail to rot...")
        print("Game over")
        quit()


    
    
 

      

    
    








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    title()
