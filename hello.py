for i in range(5):
    print("Hello")
name = "Alice"
name = input("what is your name? ")
print(name)
print("Hello "+name)
age=int(input("How old are you?"))
if age<10:
    print("damn kid!")
elif age<18:
    print("have a precious night<3")
else:
    print("You can help me!")
weather=input("Is it raining?").lower()
if weather=="yes":
    print("Take an umbrella")
else:
    print("Winner,Winner,Checken Dinner!")