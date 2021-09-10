#mastermind
import random
p = 1
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
        level = input("Which level do you want to play in?\nBeginner: 3 colours in the hidden code\nIntermediate: 4 colours in the hidden code\nAdvanced: 5 colours in the hidden code\nGod Level: 6 colours in the hidden code\n(b/i/a/g)\n")
        if level == 'b':
            redpin = 0
            whitepin = 0
            n = 0
            trials = 0
            code = list()
            colours = ["red","blue","yellow","green","white","black","pink","purple"]
            while len(code) < 3:
                code.append(random.choice(colours))
                colours.remove(code[n])
                n = n + 1
            #print(code)
            print(" Welcome young lad.")
            print(" I am Mastermind. To beat me, you need to guess my code.")
            print(" Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
            print(" No colours in my code are repeated. I have kept it easy for you.")
            print(" Choose wisely ;)")
            while redpin != 3:
                redpin = 0
                whitepin = 0
                guess1 = input("Type the first colour: ")
                if guess1 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess1 in code:
                    if guess1 == code[0]:
                        redpin = redpin + 1
                    else:
                        whitepin = whitepin + 1
                guess2 = input("Type the second colour: ")
                if guess2 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess2 == guess1:
                    print("No colours in my code are repeated. Guess again")
                    continue
                else:
                    if guess2 in code:
                        if guess2 == code[1]:
                            redpin = redpin + 1
                        else:
                            whitepin = whitepin + 1
                guess3 = input("Type the third colour: ")
                if guess3 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess3 == guess1:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess3 == guess2:
                    print("No colours in my code are repeated. Guess again")
                    continue
                else:
                    if guess3 in code:
                        if guess3 == code[2]:
                            redpin = redpin + 1
                        else:
                            whitepin = whitepin + 1
                print("redpin(s): ",redpin)
                print("whitepin(s): ",whitepin)
                trials = trials + 1
                print("Number of trials remaining: ", 10 - trials)
                if trials > 9 and redpin != 3:
                    print("You have exceeded the number of trials. Better luck next time.")
                    print("The colour code was: ",code)
                    break
            if redpin == 3:
                print("Congratulations, you have defeated me!")
            r = 0
        elif level == 'i':
            redpin = 0
            whitepin = 0
            n = 0
            trials = 0
            code = list()
            colours = ["red","blue","yellow","green","white","black","pink","purple"]
            while len(code) < 4:
                code.append(random.choice(colours))
                colours.remove(code[n])
                n = n + 1
            #print(code)
            print(" Welcome young lad.")
            print(" I am Mastermind. To beat me, you need to guess my code.")
            print(" Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
            print(" No colours in my code are repeated. I have kept it easy for you.")
            print(" Choose wisely ;)")
            while redpin != 4:
                redpin = 0
                whitepin = 0
                guess1 = input("Type the first colour: ")
                if guess1 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess1 in code:
                    if guess1 == code[0]:
                        redpin = redpin + 1
                    else:
                        whitepin = whitepin + 1
                guess2 = input("Type the second colour: ")
                if guess2 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess2 == guess1:
                    print("No colours in my code are repeated. Guess again")
                    continue
                else:
                    if guess2 in code:
                        if guess2 == code[1]:
                            redpin = redpin + 1
                        else:
                            whitepin = whitepin + 1
                guess3 = input("Type the third colour: ")
                if guess3 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess3 == guess1:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess3 == guess2:
                    print("No colours in my code are repeated. Guess again")
                    continue
                else:
                    if guess3 in code:
                        if guess3 == code[2]:
                            redpin = redpin + 1
                        else:
                            whitepin = whitepin + 1
                guess4 = input("Type the fourth colour: ")
                if guess4 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess4 == guess1:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess4 == guess2:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess4 == guess3:
                    print("No colours in my code are repeated. Guess again")
                    continue
                else:
                    if guess4 in code:
                        if guess4 == code[3]:
                            redpin = redpin + 1
                        else:
                            whitepin = whitepin + 1
                print("redpin(s): ",redpin)
                print("whitepin(s): ",whitepin)
                trials = trials + 1
                print("Number of trials remaining: ", 10 - trials)
                if trials > 9 and redpin != 4:
                    print("You have exceeded the number of trials. Better luck next time.")
                    print("The colour code was: ",code)
                    break
            if redpin == 4:
                print("Congratulations, you have defeated me!")
            r = 0
        elif level == 'a':
            redpin = 0
            whitepin = 0
            n = 0
            trials = 0
            code = list()
            colours = ["red","blue","yellow","green","white","black","pink","purple"]
            while len(code) < 5:
                code.append(random.choice(colours))
                colours.remove(code[n])
                n = n + 1
            #print(code)
            print(" Welcome young lad.")
            print(" I am Mastermind. To beat me, you need to guess my code.")
            print(" Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
            print(" No colours in my code are repeated. I have kept it easy for you.")
            print(" Choose wisely ;)")
            while redpin != 5:
                redpin = 0
                whitepin = 0
                guess1 = input("Type the first colour: ")
                if guess1 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess1 in code:
                    if guess1 == code[0]:
                        redpin = redpin + 1
                    else:
                        whitepin = whitepin + 1
                guess2 = input("Type the second colour: ")
                if guess2 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess2 == guess1:
                    print("No colours in my code are repeated. Guess again")
                    continue
                else:
                    if guess2 in code:
                        if guess2 == code[1]:
                            redpin = redpin + 1
                        else:
                            whitepin = whitepin + 1
                guess3 = input("Type the third colour: ")
                if guess3 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess3 == guess1:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess3 == guess2:
                    print("No colours in my code are repeated. Guess again")
                    continue
                else:
                    if guess3 in code:
                        if guess3 == code[2]:
                            redpin = redpin + 1
                        else:
                            whitepin = whitepin + 1
                guess4 = input("Type the fourth colour: ")
                if guess4 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess4 == guess1:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess4 == guess2:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess4 == guess3:
                    print("No colours in my code are repeated. Guess again")
                    continue
                else:
                    if guess4 in code:
                        if guess4 == code[3]:
                            redpin = redpin + 1
                        else:
                            whitepin = whitepin + 1
                guess5 = input("Type the fifth colour: ")
                if guess5 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess5 == guess1:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess5 == guess2:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess5 == guess3:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess5 == guess4:
                    print("No colours in my code are repeated. Guess again")
                    continue
                else:
                    if guess5 in code:
                        if guess5 == code[4]:
                            redpin = redpin + 1
                        else:
                            whitepin = whitepin + 1
                print("redpin(s): ",redpin)
                print("whitepin(s): ",whitepin)
                trials = trials + 1
                print("Number of trials remaining: ", 10 - trials)
                if trials > 9 and redpin != 5:
                    print("You have exceeded the number of trials. Better luck next time.")
                    print("The colour code was: ",code)
                    break
            if redpin == 5:
                print("Congratulations, you have defeated me!")
            r = 0
        elif level == 'g':
            redpin = 0
            whitepin = 0
            n = 0
            trials = 0
            code = list()
            colours = ["red","blue","yellow","green","white","black","pink","purple"]
            while len(code) < 6:
                code.append(random.choice(colours))
                colours.remove(code[n])
                n = n + 1
            #print(code)
            print(" Welcome young lad.")
            print(" I am Mastermind. To beat me, you need to guess my code.")
            print(" Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
            print(" No colours in my code are repeated. I have kept it easy for you.")
            print(" Choose wisely ;)")
            while redpin != 6:
                redpin = 0
                whitepin = 0
                guess1 = input("Type the first colour: ")
                if guess1 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess1 in code:
                    if guess1 == code[0]:
                        redpin = redpin + 1
                    else:
                        whitepin = whitepin + 1
                guess2 = input("Type the second colour: ")
                if guess2 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess2 == guess1:
                    print("No colours in my code are repeated. Guess again")
                    continue
                else:
                    if guess2 in code:
                        if guess2 == code[1]:
                            redpin = redpin + 1
                        else:
                            whitepin = whitepin + 1
                guess3 = input("Type the third colour: ")
                if guess3 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess3 == guess1:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess3 == guess2:
                    print("No colours in my code are repeated. Guess again")
                    continue
                else:
                    if guess3 in code:
                        if guess3 == code[2]:
                            redpin = redpin + 1
                        else:
                            whitepin = whitepin + 1
                guess4 = input("Type the fourth colour: ")
                if guess4 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess4 == guess1:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess4 == guess2:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess4 == guess3:
                    print("No colours in my code are repeated. Guess again")
                    continue
                else:
                    if guess4 in code:
                        if guess4 == code[3]:
                            redpin = redpin + 1
                        else:
                            whitepin = whitepin + 1
                guess5 = input("Type the fifth colour: ")
                if guess5 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess5 == guess1:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess5 == guess2:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess5 == guess3:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess5 == guess4:
                    print("No colours in my code are repeated. Guess again")
                    continue
                else:
                    if guess5 in code:
                        if guess5 == code[4]:
                            redpin = redpin + 1
                        else:
                            whitepin = whitepin + 1
                guess6 = input("Type the fifth colour: ")
                if guess6 not in ["red","blue","yellow","green","white","black","pink","purple"]:
                    print("Choose between the colours red, blue, yellow, green, white, black, pink and purple.")
                    continue
                if guess6 == guess1:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess6 == guess2:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess6 == guess3:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess6 == guess4:
                    print("No colours in my code are repeated. Guess again")
                    continue
                elif guess6 == guess5:
                    print("No colours in my code are repeated. Guess again")
                    continue
                else:
                    if guess6 in code:
                        if guess6 == code[4]:
                            redpin = redpin + 1
                        else:
                            whitepin = whitepin + 1
                print("redpin(s): ",redpin)
                print("whitepin(s): ",whitepin)
                trials = trials + 1
                print("Number of trials remaining: ", 10 - trials)
                if trials > 9 and redpin != 6:
                    print("You have exceeded the number of trials. Better luck next time.")
                    print("The colour code was: ",code)
                    break
            if redpin == 6:
                print("Congratulations, you have defeated me!")
            r = 0
        else:
            print("Please enter a valid response.\n")
    while s == 1:
        again = input("Would you like to play again?(y/n)\n")
        if again == 'y':
            s = 0
        elif again == 'n':
            p = 0
            s = 0
        else:
            print("Please enter a valid response.\n")
