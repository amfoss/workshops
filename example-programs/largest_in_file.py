# Find the largest number from a file

file = open('number.txt', 'r')

line = file.readline()

numbers = line.split(' ')

largest = int(numbers[0])

for number in numbers:
    num = int(number)
    if num > largest:
        largest = num

print("Largest value {0}".format(largest))

