#q1
print("q1")
hasban_family = {
    1 :{
        "first name":"hasban",
        "last name":"malick",
        "age":"19",
        "relation":"me" 
    },
    2 :{
        "first name":"rukhsana",
        "last name":"parven",
        "age":"45",
        "relation":"mother of hasban"
    },
    3 :{
        "first name":"ejaz",
        "last name":"malick",
        "age":"50",
        "relation":"father of hasban" 
    },
    4 :{
        "first name":"ahtesham",
        "last name":"malick",
        "age":"28",
        "relation":"brother"
    }
}
print(hasban_family)
print(hasban_family[1])
hasban_family[1]["qualification"]="enter pass"
hasban_family[1]["high qualification"]="doing civil engineering"
hasban_family[4]["qualification"]="b-teach in civil"
print(hasban_family[1])
print(hasban_family[1]["qualification"])
del hasban_family[1]["high qualification"]
print(hasban_family[1])



#q2
print("q2")
cities = {
    "karachi":{
        "country":"pakistan",
        "provinse":"sindh",
        "gdp":"123$ billion",
        "population":"20 million",
        "capital of":"sindh",
        "speciality":"karachi is finacial hub of pakistan "
        
    },
    "lohore":{
        "country":"pakistan",
        "provinse":"panjab",
        "gdp":"12$ billion",
        "population":"1.5 million",
        "capital of":"panjab",
        "speciality":"too much place like badshahi masjid and etc"
    },
    "pishawar":{
        "country":"pakistan",
        "provinse":"khyber paktun khaw",
        "gdp":"4$ billion",
        "population":"0.5 million",
        "capital of":"kpk",
        "speciality":"it is too beautifull"
    }
}
print(cities["karachi"])
print(" ")
print(cities["lohore"])
print(" ")
print(cities["pishawar"])



#q3
print("q3")

while(True):
    age = int(input("what's your age"))
    if age >=18:
        print("your charges is $3 dolar")
    elif age >= 12 and age <= 18:
        print("your charges is $2 dolar")
    elif age >= 5  and age <= 12:
        print("your charges is $1 dolar")
    elif age < 5 and age>=1 :
        print("no charges")
    elif age ==0:
    	print("")
    	break

#q4
print("q4")
def favirot_book():
    name = input("enter your name")
    title = "dear hasban"+"\n"+"your favirot book is phyaics"
    if name == "hasban":
        print(title)
    

favirot_book()



#q5
print("q5")
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
