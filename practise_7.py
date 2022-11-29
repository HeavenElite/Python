# Practise 7-4

prompt  = "\nPlease pick toppings for your pizza~"
prompt += "\nInput 'Quit' to submit this order.\n"

active = True
toppings = []

while active:
    select = input(prompt)
    select = select.lower()

    if select != 'quit':
        toppings.append(select)
        print(f"\n{select.title()} will be added.")

    else:
        print("\nSelection is done. Thank you!\n")
        active = False

print("All the toppings are:")
for topping in toppings:
    print(f"{topping.title()}")
print("\nWe are working on it.\n")

# Practise 7-5

prompt  = "\nWould you please tell me you age?"
prompt += "\nPlease input Quit, after it's done.\n"

active = True

while active:
    age = input(prompt)
    if age.lower() != 'quit':

        age = int(age)
        if age < 3:
            fee = 0
        elif age <= 12:
            fee = 10
        elif age > 12:
            fee = 15

        print(f"Your ticket price is ${fee}.")
    
    else:
        print("\nGood Bye~\n")
        break
