# Q 1

a = int(input("first number\n"))
b = input("your operator\n" )
# "add(+), sub(-), div(% or /), mul(* or ×), power(^)"))
c = int(input("enter number\n"))
if b == "+" :
    print(a+c)
elif b == "-" :
    print(a-c)
elif b == "*" or b == "x" :
    print(a*c)
elif b == "÷" or b == "/" :
    print(a/c)
elif b == "^" :
    print(a**c)
else:
    print("invalid input")

# Q 2

n = [1, 3, 5, 7, "hasban", 9, "malick", 12]
for num in n :
    if type(num) == int:
        print("it is numaric value")
    else:
        print("it is string")


#q3
dic = {5:"has",6:"mal"}
dic[7] = "ick" 
dic["break fast"] = "bread"
print(dic)

# q4
 
total = 0
for item in dic:
    if str(item).isnumeric():
        total += item
print(total)

# q5


        

    


