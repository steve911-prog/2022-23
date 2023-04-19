from random import *


def guess():
    num = randint(1, 1000001)
    print("Hi! I came up with a number between 1 and 1000 000.", 
          "\nYou have 20 attempts. Good luck!")
    #print(num)
    
    def guess_try(attempt = 1):
        attempt_ = int(attempt)
        try:
            user_num = input(f"Attempt {attempt}: ").replace(" ", "")
            if user_num.lower()  == "restart":
                guess()
            user_num = int(user_num)
        except ValueError:
            print("Hey, that 's not a number!")
            guess_try(attempt_)


        if user_num > num:
            print("Too big, man!")
            attempt_ += 1
            #attempt_ = str(attempt_)
            
            if attempt != 21:
                guess_try(attempt_)
            else:
                a = input(f"Sorry, the number was {num}. Wanna try more? (y/n)")
                if a.lower == "y" or "yes":
                    guess()
                elif a.lower == "n" or "nope":
                    print("Bye!") 
            
        elif user_num < num:
            print("Too small, man!")
            attempt_ += 1
            #attempt_ = str(attempt_)
            if attempt != 21:
                guess_try(attempt_)
            else:
                a = input(f"Sorry, the number was {num}. Wanna try more? (y/n)")
                if a.lower == "y" or "yes":
                    guess()
                elif a.lower == "n" or "nope":
                    print("Bye!") 
                
        else:
            a = input("Congratulations! You guessed it! Wanna try more? (y/n) ")
            if a.lower() == "y" or "yes":
                guess()
            elif a.lower() == "n" or "nope":
                print("Bye!")
                exit()

    guess_try()

guess()




























        
