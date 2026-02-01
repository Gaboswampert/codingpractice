import random
#print(random.randrange(0,11))

print("gambliiiiing Ver1.1")
chips=int(1000)
stringchips=str(chips)
thespirit=input("\n \t I love gambling, do you wanna gamble???? (y/n):")
if thespirit == "y":
    print("Then LETS GO GAMBLING!!!!!!")
    while True:
        print("\n \t WE LOVE GAMBLING!")
        gamblestring=input("How much do you wanna gamble? You have " + stringchips +" chips!:")
        if gamblestring.isnumeric() is False:
            print("That ain't a valid number. Try again.")
            continue
        gambleamount=int(gamblestring)
        if gambleamount >= chips:
            print("You don't have that many chips, unfotunately.")
            continue
        chips=(chips-gambleamount)
        stringchips=str(chips)
        print("Okay then, you are now left with " + stringchips + " chips!")
        game=input("Okay then, do you want to Coinflip (0), Dice Roll (1), or go to the Slots (2)?: ")
        if game == "0":
            print("In the coinflip, whatever you gambled gets multiplied by three times!")
            print("That is, if you win the game.")
            coinflip=input("So then... Heads or Tails?:" )
            if coinflip == "heads":
                coinflip="Heads"
            if coinflip == "tails":
                coinflip="Tails"
            coinbool=False
            if coinflip == "Heads":
                coinbool=True
            if coinflip == "Tails":
                coinbool=True
            if coinbool == False:
                print("That isn't a valid side of the coin. Try again")
                chips=(chips+gambleamount)
                continue
            coinwin=str(random.randrange(1,3))
            if coinwin == "1":
                coinwin=("Heads")
            else:
                coinwin=("Tails")
            print("... And the coin lands at " + coinwin + " !")
            if coinflip == coinwin:
                chips=(gambleamount*3+chips)
                stringchips=str(chips)
                print("You've won! You now have " + stringchips + " chips!")
                coinagain=input("You REALLY should keep gambling, wanna go again? (y/n): ")
                if coinagain == "y":
                    continue
                else:
                    print("boriiiiing")
                    stop10=input("You cashed out with " + stringchips + " chips.")
                    break
            else:
                 print("Sorry, seems you've lost...")
                 coinlosagain=input("But you know ahat they say abot gambling. 99% Quit before they hit it big! Wanna give it another shot? (y/n): ")
                 if coinlosagain == "y":
                     continue
                 else:
                     print("boriiiiing")
                     stop9=input("You cashed out with " + stringchips + " chips.")
                     break
                
        elif game == "1":
            print("On Dice Rolls, you can bet whether the the resulting number will be higher or lower than 6.")
            print("OR you can bet on a specific number!")
            print("Winning a higher or lower bet multiplies your money by 2")
            print("Winning a specific number bet though, awards you with 4 times your bet! And if \n you bet for 2 or 12 and win, you're awarded with 8 times your bet!")
            dicechoice=input("So what are you gonna choose? Higher or Lower(0), or Specific Number?(1): ")
            if dicechoice == "0":
                highorlow=input("Okay then, what's it gonna be? Higher or Lower?: ")
                if highorlow == "higher":
                    highorlow="Higher"
                if highorlow == "lower":
                    highorlow="Lower"
                highorbool=False
                if highorlow == "Higher":
                    highorbool=True
                if highorlow == "Lower":
                    highorbool=True
                if highorbool == False:
                    print("That isn't a valid option. Try again!")
                    chips=(chips+gambleamount)
                    stringchips=str(chips)
                    continue

                dicewintring=str(random.randrange(1,13))
                print("... And the dice land at " + dicewintring + "!")
                dicewin=int(dicewintring)
                if dicewin == int(6):
                    print("You could've bet on 6 alone, and have recieved twice of what you're getting now!")
                if highorlow == "Higher":
                    if dicewin >= int(6):
                        chips=(gambleamount*2+chips)
                        stringchips=str(chips)
                        print("You've won! You now have " + stringchips + " chips!")
                        highoragain=input("You REALLY should keep gambling, wanna go again? (y/n): ")
                        if highoragain == "y":
                            continue
                        else:
                            print("boriiiiing")
                            stop8=input("You cashed out with " + stringchips + " chips.")
                            break
                    elif int(6) > dicewin:
                        print("Sorry, seems you've lost...")
                        highorlogain=input("But you know ahat they say abot gambling. 99% Quit before they hit it big! Wanna give it another shot? (y/n): ") 
                        if highorlogain == "y":
                            continue
                        else:
                            print("boriiiiing")
                            stop7=input("You cashed out with " + stringchips + " chips.")
                            break

                elif highorlow == "Lower":
                    if int(6) >= dicewin:
                        chips=(gambleamount*2+chips)
                        stringchips=str(chips)
                        print("You've won! You now have " + stringchips + " chips!")
                        loworagain=input("You REALLY should keep gambling, wanna go again? (y/n): ")
                        if loworagain == "y":
                            continue
                        else:
                            print("boriiiiing")
                            stop6=input("You cashed out with " + stringchips + " chips.")
                            break
                    else:
                        print("Sorry, seems you've lost...")
                        lowlogain=input("But you know ahat they say abot gambling. 99% Quit before they hit it big! Wanna give it another shot? (y/n): ")
                        if lowlogain == "y":
                            continue
                        else:
                            print("boriiiiing")
                            stop5=input("You cashed out with " + stringchips + " chips.")
                            break


            elif dicechoice == "1":
                dicenumbstr=input("Okay then, pick a number between 2 and 12!: ")
                dicenumbool=False
                if dicenumbstr.isnumeric() == True:
                    dicenumbool=True
                else:
                    print("Sorry, but that isn't a number. Try again!")
                    chips=(chips+gambleamount)
                    stringchips=str(chips)
                    continue
                dicenumbet=int(dicenumbstr)
                if dicenumbet > int(12):
                    print("Sorry, but that number isn't valid. Try again!")
                    chips=(chips+gambleamount)
                    stringchips=str(chips)
                    continue
                elif dicenumbet <= int(1):
                    print("Sorry, but that number isn't valid. Try again!")
                    chips=(chips+gambleamount)
                    stringchips=str(chips)
                    continue
                dicenumb1=int(random.randrange(1,7))
                dicenumb2=int(random.randrange(1,7))
                dicenumbwin=(dicenumb1+dicenumb2)
                dicenumbwstr=str(dicenumbwin)
                print("And the dice rolls " + dicenumbwstr + "!")

                if dicenumbet == dicenumbwin and dicenumbet == int(2):
                    chips=(gambleamount*8+chips)
                    stringchips=str(chips)
                    print("INCREDIBLE!!! You've won! You now have " + stringchips + " chips!")
                    if gambleamount < int(300):
                        print("You should stop playing safe though. I'm telling you to go wild! All in or nothing! Who knows, maybe you keep getting real lucky!") 
                    dicebetgain1=input("Wanna go again? (y/n): ")
                    if dicebetgain1 == "y":
                        continue
                    else:
                        print("boriiiiing")
                        stop3=input("You cashed out with " + stringchips + " chips.")
                        break
                elif dicenumbet == dicenumbwin and dicenumbet == int(12):
                    chips=(gambleamount*8+chips)
                    stringchips=str(chips)
                    print("INCREDIBLE!!! You've won! You now have " + stringchips + " chips!")
                    if gambleamount < int(300):
                        print("You should stop playing safe though. I'm telling you to go wild! All in or nothing! Who knows, maybe you keep getting real lucky!") 
                    dicebetgain2=input("Wanna go again? (y/n): ")
                    if dicebetgain2 == "y":
                        continue
                    else:
                        print("boriiiiing")
                        stop2=input("You cashed out with " + stringchips + " chips.")
                        break
                elif dicenumbet == dicenumbwin:
                    chips=(gambleamount*4+chips)
                    stringchips=str(chips)
                    print("WHOA!!! You've won! You now have " + stringchips + " chips!")
                    if gambleamount < int(300):
                        print("You should stop playing safe though. I'm telling you to go wild! All in or nothing! Who knows, maybe you keep getting real lucky!") 
                    dicebetgain=input("Wanna go again? (y/n): ")
                    if dicebetgain == "y":
                        continue
                    else:
                        print("boriiiiing")
                        stop4=input("You cashed out with " + stringchips + " chips.")
                        break
                
                else:
                    print("Seems you've lost, but who knows, maybe you will be getting more lucky next time!")
                    dicebetgain3=input("Wanna go again? (y/n): ")
                    if dicebetgain3 == "y":
                        continue
                    else:
                        print("boriiiiing")
                        stop1=input("You cashed out with " + stringchips + " chips.")
                        break
                
            else:
                print("That isn't a valid pick. Try again!")
                chips=(chips+gambleamount)
                stringchips=str(chips)
                continue
        elif game == "2":
            print("On the slots, you can bet for one (middle), two (middle, upper), or three (all) lines of the slot having the same number!")
            print("Of course, the riskier the bet, the bigger reward!")
            print("Betting on three lines gives you eight times your bet, two is twelve times, and on one, you get TWENTY TIMES your bet!")
            lineamountstr=input("So how many lines would you like to bet on? 1, 2, or 3?: ")
            if lineamountstr.isnumeric() == False:
                print("Sorry, but that isn't a number. Try again!")
                chips=(chips+gambleamount)
                stringchips=str(chips)
                continue
            lineamount=int(lineamountstr)
            if lineamount > int(3):
                print("Sorry, but there aren't that many lines. Try again!")
                chips=(chips+gambleamount)
                stringchips=str(chips)
                continue
            if lineamount < int(1):
                print("Sorry, but that isnt a valid number. Try again!")
                chips=(chips+gambleamount)
                stringchips=str(chips)
                continue
            linenumberstr=input("And in what number 1-9 are you betting?: ")
            if linenumberstr.isnumeric() == False:
                print("Sorry, but that isn't a number. Try again!")
                chips=(chips+gambleamount)
                stringchips=str(chips)
                continue
            linenumber=int(linenumberstr)
            if linenumber > int(9):
                print("Sorry, but that isn't a valid number. Try again!")
                chips=(chips+gambleamount)
                stringchips=str(chips)
                continue
            if linenumber < int(1):
                print("Sorry, but that isn't a valid number. Try again!")
                chips=(chips+gambleamount)
                stringchips=str(chips)
                continue
            print("Okay then! Let's SPIN. THOSE. SLOTS!")
            slot1=int(random.randrange(1,10))
            slot2=int(random.randrange(1,10))
            slot3=int(random.randrange(1,10))
            slot4=int(random.randrange(1,10))
            slot5=int(random.randrange(1,10))
            slot6=int(random.randrange(1,10))
            slot7=int(random.randrange(1,10))
            slot8=int(random.randrange(1,10))
            slot9=int(random.randrange(1,10))
            print(slot1, slot2, slot3)
            print(slot4, slot5, slot6)
            print(slot7, slot8, slot9)
            linenumbrr=int(linenumberstr)
            if lineamount == int(3):
                  if linenumbrr == slot1 == slot2 == slot3 or linenumbrr == slot4 == slot5 == slot6 or linenumbrr == slot7 == slot8 == slot9:
                      chips=(gambleamount*8+chips)
                      stringchips=str(chips)
                      print("You've won! You now have " + stringchips + " chips!")
                      if gambleamount < int(300):
                          print("You should stop playing safe though. I'm telling you to go wild! All in or nothing! Who knows, maybe you keep getting real lucky!") 
                      slotsagain1=input("Wanna go again? (y/n): ")
                      if slotsagain1 == "y":
                          continue
                      else:
                          print("boriiiiing")
                          stop12=input("You cashed out with " + stringchips + " chips.")
                          break
                  else:
                      print("Seems you've lost, but who knows, maybe you will be getting more lucky next time!")
                      slotsagain2=input("Wanna go again? (y/n): ")
                      if slotsagain2 == "y":
                          continue
                      else:
                          print("boriiiiing")
                          stop1=input("You cashed out with " + stringchips + " chips.")
                          break
            elif lineamount == int(2):
                if linenumbrr == slot1 == slot2 == slot3 or linenumbrr == slot4 == slot5 == slot6:
                    chips=(gambleamount*12+chips)
                    stringchips=str(chips)
                    print("AMAZING!!! You've won! You now have " + stringchips + " chips!")
                    if gambleamount < int(300):
                        print("You should stop playing safe though. I'm telling you to go wild! All in or nothing! Who knows, maybe you keep getting real lucky!") 
                    slotsagain3=input("Wanna go again? (y/n): ")
                    if slotsagain3 == "y":
                        continue
                    else:
                        print("boriiiiing")
                        stop15=input("You cashed out with " + stringchips + " chips.")
                        break
                else:
                    print("Seems you've lost, but who knows, maybe you will be getting more lucky next time!")
                    slotsagain4=input("Wanna go again? (y/n): ")
                    if slotsagain4 == "y":
                        continue
                    else:
                        print("boriiiiing")
                        stop16=input("You cashed out with " + stringchips + " chips.")
                        break
            elif lineamount == int(1):
                if linenumbrr == slot4 == slot5 == slot6:
                    chips=(gambleamount*20+chips)
                    stringchips=str(chips)
                    print("AMAZING, UNBELIEVABLE, INCREDIBLE!!! You've won! You now have " + stringchips + " chips!")
                    if gambleamount < int(300):
                        print("You should stop playing safe though. I'm telling you to go wild! All in or nothing! Who knows, maybe you keep getting real lucky!") 
                    slotsagain5=input("Wanna go again? (y/n): ")
                    if slotsagain5 == "y":
                        continue
                    else:
                        print("boriiiiing")
                        stop17=input("You cashed out with " + stringchips + " chips.")
                        break
                else:
                    print("Seems you've lost, but who knows, maybe you will be getting more lucky next time!")
                    slotsagain6=input("Wanna go again? (y/n): ")
                    if slotsagain6 == "y":
                        continue
                    else:
                        print("boriiiiing")
                        stop18=input("You cashed out with " + stringchips + " chips.")
                        break
        else:
            print("That is not a valid game.")
            chips=(chips+gambleamount)
            stringchips=str(chips)
            continue
else:
    print("boriiiiing")

