def read_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines_split = [line.split(',') for line in lines]
    return [item.strip() for sublist in lines_split for item in sublist]
data = read_lines_from_file('puzzle_input.txt')
# Create a list of numbers that contains all digits of the numbers in 'data' seperated into individual lists
digits = []
all_digits = []
for number in data:
        digits.extend([int(digit) for digit in str(number)])
        all_digits.append(digits)
        digits = []
print(all_digits)

banks = []
# Select 12 numbers from the list in order, to create the highest 2 digit number possible and keeping the order they appear in the list
for numbers in all_digits:
        possible_combinations = []
        highest_numbers = []
        for i in range(len(numbers)-1):
                first_num = numbers[i]

                for j in range(len(numbers)-i-1):
                      possible_combinations.append(int(str(first_num) + str(numbers[i+j+1])))

                highest_numbers.append(max(possible_combinations))
                print(set(highest_numbers))
        banks.append(max(highest_numbers))
                

print(banks)
result = sum(banks)
print(result)