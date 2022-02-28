# ? Don't change the code below ?
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# ? Don't change the code above ?

#Write your code below this line ?
lower_case_name1=name1.lower()
lower_case_name2=name2.lower()

num1=0
for char1 in ["t","r",'u','e']:
    num1=num1+lower_case_name1.count(char1)

print(num1)
num2=0
for char2 in ["l","o",'v','e']:
    num2=num2+lower_case_name2.count(char2)
print(num2)
result=num1*10+num2

if result>90 or result<10:
    print(f'Your score is {result}, you go together like coke and mentos.')
elif result >40 or result<50:
    print(f'Your score is {result}, you are alright together.')
else:
    print(f"Your score is {result}.")
    
    
