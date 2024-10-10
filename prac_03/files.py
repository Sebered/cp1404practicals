
# 1
name = str(input("Name: "))
name_file = open('name.txt', 'w')
name_file.write(name)
name_file.close()

# 2
name_file = open('name.txt', 'r')
name = name_file.read()
print(f"Hi {name}!")
name_file.close()

# 3
with open('numbers.txt', 'r') as numbers_file:
    number1 = numbers_file.readline()
    number2 = numbers_file.readline()
    number3 = int(number1) + int(number2)
    print(number3)

# 4
total_sum = 0
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        number = int(line)
        total_sum += number
print(total_sum)