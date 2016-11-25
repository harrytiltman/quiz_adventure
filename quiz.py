# Our quiz!

score = 0
name = ""
def quiz():
    global score

    print("WELLCOME TO THE TOTALLY RANDOM QUIZ")
    name = input("Enter your name: ")
    print("Hello", name)
    question1()
    question2()
    question3()

    
def question1():
    global score
    global name
    print(" ") 
    print("what is the capital of Pakistan")
    print("A. Islamban")
    print("B. Tundale")
    print("C. Islambad")

    answer = input("Answer: ")

    if answer == "C":
        score = score + 1
        print("Question 1 is correct")
        print("your score is", score)

    else:
        print("Incorrect")
        print("WRONG`")
        
def question2():
    global score
    global name
    print(" ")
    print("who won the devision 1(premier league) in the 1935/36 season")
    print("A. Sunderland AFC")
    print("B. Preston North End")
    print("C. Arsenal")

    answer = input("Answer: ")


    if answer == "A":
        score = score + 1
        print("Question 2 is correct")
        print("your score is", score)

    else:
        print("Incorrect")
        print("WRONG")
              
def question3():
    global score
    global name
    print(" ")
    print("to the nearest million how many people live in london")
    print("A. 5,000,000")
    print("B. 8,000,000")
    print("C. 10,000,000")

    answer = input("Answer: ")

    if answer == "B":
        score = score + 1
        print("Question 2 is correct")
        print("your score is", score)

    else:
        print("Incorrect")
        print("WRONG")


    if score == 3:
        print(" ")
        print("WE HAVE A WINNER")

    elif score < 3:
              print(" ")
              print("WE HAVE A LOSER")
    

        
    





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
