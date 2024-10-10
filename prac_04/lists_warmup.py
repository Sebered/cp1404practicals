numbers = [3, 1, 4, 1, 5, 9, 2]

"""
numbers[0]
3
numbers[-1]
2
numbers[3]
1
numbers[:-1]
:2 - [3, 1, 4, 1, 5, 9]
numbers[3:4]
1:5 - [1]
5 in numbers
3, 1, 4, 1, 5 - True
7 in numbers
3, 1, 4, 1, 5, 9, 2 - False
"3" in numbers
numbers[0] - False
numbers + [6, 5, 3]
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])
print(9 in numbers)