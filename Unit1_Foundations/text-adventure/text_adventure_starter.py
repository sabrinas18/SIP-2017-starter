start = '''
You are an elderly grandmother at a ripe age of 102.
Your computer you've had for 25 years has crashed!
You're frustrated so you...
'''

print(start)

print("Type 'restart' to close and restart computer or 'deep breaths' to go and come back later or 'troubleshoot' to locate the error")
user_input = input()
if user_input == "restart":
    print("Oh no! You restarted the computer but the spinning ball of death appears!")
    print("Type 'call grandson' to ask for help or 'break computer' to give up")
    user_input_two = input()
    if user_input_two == 'call grandson':
        print("Oops! He accidentally installed a virus!")
        print("Type 'cut off all ties w/ grandson' to eliminate the child or 'shop' to take computer into the store")
        user_input_three = input()
        if user_input_three == 'cut off all ties w/ grandson':
            print("Ties have been cut. How lonely!")
            print("Your grandson is angry and seeks revenge. He breaks your computer with a bat!")
            print("GAME OVER")
        if user_input_three == 'shop':
            print("You took it to get it fixed! Congrats!")
            print("GAME OVER")
    if user_input_two == 'break computer':
        print("You broke the computer... You should work on your temper.")
        print("GAME OVER")

elif user_input == "deep breaths":
    print("You go for a nice, peaceful walk to cool your head.")
    print("You log back in later and it works! Congratulations!")
elif user_input == "troubleshoot":
    print("The problem could not be found.")
    print("Type 'browser' to use another browser or 'angry' to punch and destroy the computer")
    user_input_four = input()
    if user_input_four == 'browser':
        print("No! You switched browsers but downloaded a virus!")
        print("Type 'break' to break the computer or 'uninstall' to take 3 hours to fix it or 'shop' to take it in")
        user_input_five = input()
        if user_input_five == 'break':
            print("You broke the computer... You should work on your temper.")
            print("GAME OVER")
        if user_input_five == 'uninstall':
            print("A new virus is instaled!")
            print("Type 'break' to break computer or 'buy new computer' to replace the old one")
            user_input_six = input()
            if user_input_six == 'break':
                print("You broke the computer... You should work on your temper.")
                print("GAME OVER")
            if user_input_six == 'buy new computer':
                print("Sweet! You got a new computer.")
                print("Too bad you had to take the money out of your retirement funds!")
                print("GAME OVER")
        if user_input_five == 'shop':
            print("You took it to get it fixed! Congrats!")
            print("GAME OVER")
    if user_input_four == 'angry':
        print("You punched and destroyed the computer... You should work on your temper.")
        print("GAME OVER")
