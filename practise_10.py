# 练习 10-6 & 10-7

import functions

welcom_prompt  = "\nThis calculator will plus two numbers.\n"
welcom_prompt += "Are you ready?\n"
print(welcom_prompt)

while True:
    first_number = functions.input_collection()
    second_number = functions.input_collection()
    result = first_number + second_number
    print(f"The result is {result}")

    answer = functions.quit_confirmation()
    if answer == 'quit':
        break
    elif answer == 'continue':
        continue


# 练习 10.3~5

record_file = 'guest.txt'

while True:

    prompt = "Please input your name: \n"
    user_name = input(prompt)

    record_file = 'guest.txt'
    with open(record_file, 'a') as file_object:
        file_object.write(f"{user_name.lower()}\n")

    print("Your name is recorded in system.")
    prompt  = "Would you need input more names?\n"
    prompt += "Please answer Y or N.\n"
    decision = input(prompt)

    if decision.lower() == 'y':
        continue
    elif decision.lower() == 'n':
        break
    else:
        print("Error input, Program is about to quit.")
        break

print("Please is all the name records in system:\n")
with open(record_file) as file_object:
    content = file_object.read()
    print(content)
print("Good Buy.")


# 练习 10-2

target_file = 'learning_python.txt'

with open(target_file) as file_object:
    for line in file_object:
        line = line.replace('Python', 'C++')
        print(line.rstrip())


# 练习 10-1

file_path = 'learning_python.txt'

with open(file_path) as file_object:
    content = file_object.read()
    print(content)

with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(file_path) as file_object:    
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())