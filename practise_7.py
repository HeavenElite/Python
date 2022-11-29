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