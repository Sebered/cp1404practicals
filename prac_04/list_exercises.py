list_of_inputs = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

for i in range(5):
    number_input = int(input("Number: "))
    list_of_inputs.append(number_input)

print(list_of_inputs)
print(f"The first number is {list_of_inputs[0]}")
print(f"The last number is {list_of_inputs[-1]}")
print(f"The smallest number is {min(list_of_inputs)}")
print(f"The largest number is {max(list_of_inputs)}")
mean = sum(list_of_inputs)/len(list_of_inputs)
print(f"The average of the numbers is {mean}")

username_input = str(input("What is your username? "))
if username_input in usernames:
    print("Access granted")
    print(f"Hello {username_input}")
else:
    print("Access denied")