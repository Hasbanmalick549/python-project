
while(True):
    age = int(input("what's your age"))
    if age >=18:
        print("your charges is $3 dolar")
    elif age >= 12 and age <= 18:
        print("your charges is $2 dolar")
    elif age >= 5  and age <= 12:
        print("your charges is $1 dolar")
    elif age < 5 :
        print("no charges")

