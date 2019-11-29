#q5
secrate_word = 16
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess= False
print("number is b/w 5 to 20")
while guess != secrate_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess= int(input("enter true number\n"))
        guess_count += 1
    else:
        out_of_guess= True
    
  
 
if out_of_guess:
    print("you are wrong")
else:
    print("you are right")
