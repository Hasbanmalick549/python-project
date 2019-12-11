#q1
print("q1")
n = int(input("enter value to be factorial\n  "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"the factorial of {n} is {factorial}")
#q2
print("q2")
inp = input("Enter the letter that you count upper & lower letter\n   ")
 
count1 = 0
count2 = 0
for i in inp:
	if i.isupper():
		count1 += 1
	elif i.islower():
		count2 +=1
	else:
		pass
print(f"the upper case letter is {count1}")
print(f"the lower case letter is {count2}")
#q3
print("q3")
a1 =int(input("Enter a number that even or not"))
b1 = a1%2
if b1 ==0:
	print("its even")
else:
	print("its not even")
#q5
print("q5")
inp = int(input("Enter a number to check its prime or not"))
a = inp/2
b = inp /3
c =inp/5
d =inp/7
e=inp/11
f=inp/13
g=inp/17
h =inp/23

if a ==1 or b==1 or c==1 or d==1 or e==1 or f ==1 or g ==1 or h==1:
	print("its prime")
else:
	print("not prime")
	
#q6
print("q6")
list=[]
inp = ""
print("Enter your shoping item")
print("if your shoping item is completed enter {ok}")
while True:
	inp = input("")
	if inp != "ok":
		list.append(inp)
	elif inp == "ok":
		break
print(list)