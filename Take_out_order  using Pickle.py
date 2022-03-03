import pickle
from time import sleep
print("Hello sir, you are here to take a order. Please fill in the questions below!")
print("Loading...")
sleep(5)
print("Done!")
print()
print("----------------")
print()
Title = input("Mr/Miss: ")
Name = input("Enter your name: ")
Age = int(input("Please enter your age: "))

if Age >= 18:
    print("You are above the age of eighteen!")
else:
    print("You are not above the age of eighteen!")
    print("Please ask your parents to collect it!")

sleep(5)
print()
print("""

1.Pizza
2.Popcorn
3.Burgers
4.Fries

5. None of the above.
""")

Food = input("What food do you like from the selection above, please type the number: ")

if Food == int(1):
    print("You have chosen Pizza! Throw a pizza party.")
elif Food == int(2):
    print("Let us all got to the movies!")
elif Food == int(3):
    print("Burgers hmmm... would you like fries with that sir?") 
elif Food == int(4):
    print("You should had got the burger, oh well.")
elif Food == int(5):
    print("Ok that's fine by me.")


print("Ok",Title,Name,"Your order has been placed please check to see if it is there")

with open("Order.txt", "wb") as (Take_out_order):
    pickle.dump((Title,Name,Age,Food), (Take_out_order))

print("Press any key to end the program")
input()
    
    
    
