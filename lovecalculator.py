# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined=name1 + name2
lower_text= combined.lower()
t=lower_text.count("t")
r=lower_text.count("r")
u=lower_text.count("u")
e=lower_text.count("e")
true=t+r+u+e
l=lower_text.count("l")
o=lower_text.count("o")
v=lower_text.count("v")
e=lower_text.count("e")
love=l+o+v+e
total=int(str(true) + str(love))
if total<10 or total>90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total>40 and total<50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")