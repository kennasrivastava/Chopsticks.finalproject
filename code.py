import random

#greet the user and start game
name = input("What is your name? ")
if str.lower(name) == "presentation":
  learn = input("What did I learn? What did I struggle with? What am I proud of?")
  if learn == " ":
    print("Flowcharts are very useful and it may be easier to code a game if you make a basic flowchart first")
    print("I struggled with having to recode my game after people refused to use common sense when playing the game")
    print("I am proud of how quickly I was able to code the game because the flowchart took over three classes and two pages to make.")
  else:
    print("Game over") 
else:
  welcome_message  = input(f"Hi {name}, would you like to play chopsticks, a digitized hand game? Please only respond with yes or no, else you will suffer. ")
  #start game
  if str.lower(welcome_message) == "yes" or str.lower(welcome_message) == "y":
    #display rules
    show_rules = input("Would you like to see the rules? ")
    if str.lower(show_rules) == "yes" or str.lower(show_rules) == "y":
      print("Hi! Chopsticks is usually a hand game, but today we will be playing on a computer. You will start with a finger on each hand. When you get 5 fingers on one hand, the hand is out. You cannot transfer fingers between your own hands. You can give someone more fingers. For example, if you have 2 fingers on one hand and you strike your opponent's hand with 2 fingers, your opponent would then have 4 fingers on the hand. L stands for left and R stands for right. 3L 4R means a player has 3 fingers on their left hand and 4 on their right. RL means right hand to the opponent's left hand and so on for RR, LR, LL.  ")
      #show initial values on each hand
      print(f"{name}: 1L 1R and Computer: 1L 1R")
      #present user with their first choice
      choice_1 = input(f"{name} is up first. Choose LR, RL, LL, RR: ")
      if str.upper(choice_1) == "LR" or str.upper(choice_1) == "RR":
        print(f"Computer has taken its turn. {name}: 1L 3R and Computer: 1L 2R" )
        #let player take second turn 
        choice_2 = input(f"It is {name}'s turn. Choose LR, RL, LL, RR: ")
        if str.upper(choice_2) == "LR":
          print("Computer has taken its turn." f"{name}: 1L and Computer: 1L 3R" ) 
        #let player take third turn
        choice_3 = input("Choose. What will it be? LR or LL ")
        if str.upper(choice_3) == "LR":
          print("Computer has taken its turn." f"{name}: lost and Computer: 1L 3R" )
          #end game
          print("Good effort! Run the program to play again")
        #let player take third turn
        elif str.upper(choice_3) == "LL":
          print("Computer has taken its turn." f"{name}: 1L and Computer: 2L 3R" )
          #let player take 4th turn
          choice_4 = input("Choose. What will it be? LR or LL ")
          if str.upper(choice_4) == "LR":
            print("Computer has taken its turn." f"{name}: lost and Computer: 1L 3R" )
            print("Good effort! Run the program to play again") 
          #player's 4th turn
          elif str.upper(choice_4) == "LL":
            print("Computer has taken its turn." f"{name}: 1L and Computer: 1L 4R" )
          #exit game bc player didn't put in valid input on 4th turn
          else:
            print("I feel like you aren't taking this relationship seriously enough. Go tell your jokes to somebody else. Adios.")
        
        #2nd turn     
        elif str.upper(choice_2) == "RR":
          print("Computer has taken its turn." f"{name}: 1L 4R and Computer: 1L" )
          #3rd turn
          choice_3_1 = input("You're up. LL or RL? ")
          if str.upper(choice_3_1) == "LL":
            print("Computer has taken its turn." f"{name}: 3L 4R and Computer: 2L" )
            #4th turn
            choice_4_1 = input("No more formalities. LL or RL? ")
            if str.upper(choice_4_1) == "LL" or str.upper(choice_4_1) == "RL":
              print("YAYYYYY! You won. Be proud")
            else:
              print("c'mon dude you had one job and you still managed to mess up. tsk tsk. game over.")
          elif choice_3_1 =="RL":
            print("Computer has taken its turn." f"{name}: 1L and Computer: lost" )
            print("Wow, congratulations! Future cyborgs could learn a thing or two from you")
          else:
            print("This isn't working out. We should break up. OK bye.")
          
        #2nd turn
        elif str.upper(choice_2) == "RL":
          print("Computer has taken its turn." f"{name}: 4R and Computer: 4L 2R" )
          #3rd turn
          choice_3_2 = input("You're up. RL or RR? ")
          if str.upper(choice_3_2) == "RL":
            print("Computer has taken its turn." f"{name}: lost and Computer: 2R" )
            print("Better luck next time!")
          elif str.upper(choice_3_2) == "RR":
            print("Computer has taken its turn." f"{name}: lost and Computer: 4L" )
            print("Better luck next time!")
          else:
              print("c'mon dude you had one job and you still managed to mess up. tsk tsk. game over.")
        
        #2nd turn
        elif str.upper(choice_2) == "LL":
          print("Computer has taken its turn." f"{name}: 1L and Computer: 2L 2R" )
          #3rd turn
          choice_3_3 = input("You're up. LL or LR? ")
          if str.upper(choice_3_3) == "LL":
            print("Computer has taken its turn." f"{name}: 4L and Computer: 3L 2R" )
            #4th turn
            choice_4_2 = input("Will it be LR or LL?")
            if str.upper(choice_4_2) == "LR" or str.upper(choice_4_2) == "LL":
              print("Computer has taken its turn. Unfortunately, you lost. Better luck next time!")
            else:
              print("Really? You had one job. I can't do this anymore. Game over. ")
          elif str.upper(choice_3_3) == "LR":
            print("Computer has taken its turn." f"{name}: 4L and Computer: 3L 2R" )
            #4th turn
            choice_4_3 = input("Will it be LR or LL?")
            if str.upper(choice_4_3) == "LR" or str.upper(choice_4_2) == "LL":
              print("Computer has taken its turn. Unfortunately, you lost. Better luck next time!")
            else:
              print("Really? You had one job. I can't do this anymore. Game over. ")

        #2nd turn
        else:
          print("invalid input game over")  

      #1st turn 
      elif str.upper(choice_1) == "LL" or str.upper(choice_1) == "RL":
        print("Computer has taken its turn." f"{name}: 1L 3R and Computer: 2L 1R")
        #2nd turn
        choice_2_1 = input("You're up. Choose between LR, RR, RL, anf LL: ")
        if str.upper(choice_2_1) == "LR":
          print("Computer has taken its turn." f"{name}: 1L and Computer: 2L 2R")
          #3rd turn
          choice_3_4 = input("You're up. LL or LR? ")
          if str.upper(choice_3_4) == "LL":
            print("Computer has taken its turn." f"{name}: 4L and Computer: 3L 2R" )
            #4th turn
            choice_4_4 = input("Will it be LR or LL?")
            if str.upper(choice_4_4) == "LR" or str.upper(choice_4_4) == "LL":
              print("Computer has taken its turn. Unfortunately, you lost. Better luck next time!")
            else:
              print("Really? You had one job. I can't do this anymore. Game over. ")
          #3rd turn
          elif str.upper(choice_3_4) == "LR":
            print("Computer has taken its turn." f"{name}: 4L and Computer: 3L 2R" )
            #4th turn
            choice_4_5 = input("Will it be LR or LL?")
            if str.upper(choice_4_5) == "LR" or str.upper(choice_4_2) == "LL":
              print("Computer has taken its turn. Unfortunately, you lost. Better luck next time!")
            else:
              print("Really? You had one job. I can't do this anymore. Game over. ")
          #3rd turn
          else:
            print("c'mon dude. you had one job. game over.")

        #2nd turn
        elif str.upper(choice_2_1) == "RR":
          print("Computer has taken its turn." f"{name}: 4L and Computer: 3L 2R")
          choice_3_5 = input("Will it be RL or RR")
          #3rd turn
          if str.upper(choice_3_5) == "RL":
            print("Computer has taken its turn." f"{name}: lost and Computer: 4L 2R")
            print("Better luck next time!")
          #3rd turn
          elif str.upper(choice_3_5) == "RR":
            print("Computer has taken its turn." f"{name}: lost and Computer: 2L")
            print("Better luck next time!")
          #3rd turn
          else: 
            print("c'mon dude. you had ONE job. game over.")

        #2nd turn
        elif str.upper(choice_2_1) == "RL":
          print("Computer has taken its turn." f"{name}: 2L 3R and Computer: 1R")
          #3rd turn
          choice_3_6 = input("Choose. LR or RR? ")
          if str.upper(choice_3_6) == "LR":
            print("Computer has taken its turn." f"{name}: 3R and Computer: 3R")
            input("Type RR or literally anything else to proceed: ")
            print("CONGRATS! you won")
          #3rd turn
          elif str.upper(choice_3_6) == "RR":
            print("Computer has taken its turn." f"{name}: 3R and Computer: 4R")
            input("Type RR or literally anything else to proceed: ")
            print("CONGRATS! you won")
          #3rd turhn
          else:
            print("c'mon dude. you had ONE job. game over")

        #2nd turn
        elif str.upper(choice_2_1) == "LL":
          print("Computer has taken its turn." f"{name}: 1L and Computer: 3L 1R")
          #third turn
          choice_3_7 = input("You're up. LR or LL? ")
          if str.upper(choice_3_7) == "LR":
            print("Computer has taken its turn." f"{name}: 4L and Computer: 3L 2R")
            #4th turn
            choice_4_6 = input("What will it be? LR or LL?")
            if str.upper(choice_4_6) == "LR":
              print("Computer has taken its turn." f"{name}: lost and Computer: 3L")
              print("Better luck next time!")
            #4th turn
            elif str.upper(choice_4_6) == "LL":
              print("Computer has taken its turn." f"{name}: lost and Computer: 2L")
              print("Better luck next time!")
            else:
              print("c'mon dude. you had ONE job. game over")
          #3rd turn
          elif str.upper(choice_3_7) == "LL":
            print("Computer has taken its turn." f"{name}: 3R and Computer: 4R")
            input("Type RR or literally anything else to proceed: ")
            print("CONGRATS! you won")
          #3rd turn
          else:
            print("c'mon dude. you had ONE job. game over.")


      #break out of game if other input is entered
      else: 
        print("WOW ok. I see how it is. It's fine, we're chill. But... you're not taking this game seriously enough. This relationship feels a little toxic. I think it's best if I leave. Sound good? Nope, you don't get to answer that. ok bye.")
  
    #exit game if the user does not want to see rules
    else:
      print("Sorry for your loss! This is a great game.")

  #exit game is the user does not want to play game or wants to suffer
  elif str.lower(welcome_message) == "no" or str.lower(welcome_message) == "n":
    print("Sorry for your loss! This is a great game.")

  else: 
    print("You chose to suffer? Bold choice. You are sentenced to starvation in the dungeons. Tips for survival, you ask? Eat the dragons before they eat you. Even then, you'll only last so long. Butlers? Take 'em away.")
