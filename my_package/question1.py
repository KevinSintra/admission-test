# Question1
# find find max value of a array of numbers
def find_max(numbers): 
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

# find position of a number in a array of numbers and return -1 if not found
def find_position(numbers, number): 
    for i in range(len(numbers)):
        if numbers[i] == number:
            return i
    return -1