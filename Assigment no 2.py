# q1
s1 = int(input(" physics\n"))
s2 = int(input(" chemistry\n"))
s3 = int(input(" maths\n"))
s4 = int(input(" urdu\n"))
s5 = int(input(" english\n"))

all_sub = (s1+s2+s3+s4+s5)/5
if all_sub >= 80 and all_sub <= 100 :
    print(" percentage")
    print(all_sub)
    print(" Grade- A+")
elif all_sub >= 70 and all_sub <= 80 :
    print(" percentage")
    print(all_sub)
    print(" Grade- A")
elif all_sub >= 60 and all_sub <= 70 :
    print(" percentage")
    print(all_sub)
    print(" Grade- B")
elif all_sub >= 50 and all_sub <= 60 :
    print(" percentage")
    print(all_sub)
    print(" Grade- C")
elif all_sub >= 40 and all_sub <= 50 :
    print(" percentage")
    print(all_sub)
    print(" Grade- E")
elif all_sub >= 33 and all_sub <= 40 :
    print(" percentage")
    print(all_sub)
    print(" Only Pass")
elif all_sub < 33 :
    print(" percentage")
    print(all_sub)
    print(" Fail")
else:
    print(" invalid answer")


# q2 
h = int(input("write number\n "))
if h%2 == 0 :
    print("this is even number")
else:
    print("this is odd number")


# q3
list = []
num = int(input("how many number you enter"))
for n in range(num):
    number = int(input("enter number"))
    list.append(number)
print("list=", list)
print("counting of list =", len(list))


#q4
list = []
num = int(input("how many number"))
for n in range(num):
    number = int(input("enter number"))
    list.append(number)
print(list)
print("sum of all list", sum(list))


# q5
list = []
num = int(input("how many number"))
for n in range(num):
    number = int(input("enter number"))
    list.append(number)
print("list = ", list)
print("large number= ", max(list))

# q6 exp a [1,3,5,8,99,5,66,44,]
list = []
num = int(input("how many number"))
for n in range(num):
    number = int(input("enter number"))
    list.append(number)
print("list=", list)
for i in list:
    if i <= 5:
        print(i)
