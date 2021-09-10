#Mastermind
import random
p = 1
def gamelevel(a):
    redpin = 0
    whitepin = 0
    n = 0
    trials = 0
    guessedcode = []
    code = list()
    colours = ["red","blue","yellow","green","white","black","pink","purple"]
    while len(code) < a:
        code.append(random.choice(colours))
        colours.remove(code[n])
        n = n + 1
    #print(code)
    print(" Welcome young lad.")
    print(" I am Mastermind. To beat me, you need to guess my code.")
    print(" Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
    print(" No colours in my code are repeated. I have kept it easy for you.")
    print(" Choose wisely ;)")
    while redpin != a:
        redpin = 0
        whitepin = 0
        guessedcode = []
        for hello in range(1,a + 1):
            whileloopvar1 = 0
            while whileloopvar1 < 1:
                print("Type colour",hello,":",end = "")
                userguess = input()
                if userguess not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                else:
                    guessedcode.append(userguess)
                    if len(guessedcode) != len(set(guessedcode)):
                        print("No colours in my code are repeated. Guess again")
                        guessedcode.pop(hello - 1)
                        continue
                    else:
                        if userguess in code:
                            if userguess == code[hello - 1]:
                                redpin = redpin + 1
                            else:
                                whitepin = whitepin + 1
                        whileloopvar1 = 1
        print("redpin(s): ",redpin)
        print("whitepin(s): ",whitepin)
        trials = trials + 1
        print("Number of trials remaining: ", 10 - trials)
        if trials > 9 and redpin != a:
            print("You have exceeded the number of trials. Better luck next time.")
            print("The colour code was: ",code)
            break
    if redpin == a:
        print("Congratulations, you have defeated me!")
    r = 0

while p == 1:
    q = 1
    r = 1
    s = 1
    while q == 1:
        instruct = input("Would you like to read the instructions for the game?(y/n)\n")
        if instruct == 'y':
            print("\nINSTRUCTIONS:")
            print("             Mastermind is a code breaking game. The computer will make a hidden code consisting of a number of colours in a random order. Your job is to guess the colours and in the correct order in the given number of trials.Based on your guess, the computer will give you hints. The computer will give you some whitepins and some redpins after each turn. The number of whitepins you get represents the number of colours in your guess that are present in the hidden colour code, but in a different position. The number of redpins you get represents the number of colours in your guess that are present in the hidden colour code, and are in the same position. So, in other words, in order to win, you need to get all redpins, because that would mean all the colours in your guess are present in the hidden colour code and are in the same position.")
            print("\n\n\n")
            q = 0
        elif instruct == 'n':
            q = 0
        else:
            print("Please enter a valid response.\n")
    while r == 1:
        level = input("Which level do you want to play in?\n1 colour in the hidden code\n2 colours in the hidden code\n3 colours in the hidden code\n4 colours in the hidden code\n5 colours in the hidden code\n6 colours in the hidden code\n7 colours in the hidden code\n8 colours in the hidden code\n(1/2/3/4/5/6/7/8)\n")
        if level == "0":
            print("Please enter a valid response.\n")
            continue
        else:
            try:
                gamelevel(int(level))
                r = 0
            except:
                print("Please enter a valid response.\n")
    while s == 1:
        again = input("Would you like to play again?(y/n)\n")
        if again == 'y':
            s = 0
        elif again == 'n':
            print("\nFarewell.")
            p = 0
            s = 0
        else:
            print("Please enter a valid response.\n")
