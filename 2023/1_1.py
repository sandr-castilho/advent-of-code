'''
--- Day 1: Trebuchet?! ---

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
'''

## advent of code 2023 day 1 part one
# Sandra Castilho

input_file = "inputs/1"

def is_number(char):
	return char in ['1', '2', '3', '4', '5', '6', '7', '8', '9']

with open(input_file, "r") as file:
	sum = 0
	lines = file.readlines()
	for line in lines:
		calibration_value = ""
		for char in line[:-1]: # trim '\n'
			if is_number(char):
				if len(calibration_value) == 0: # first number
					calibration_value += char
				else:
					calibration_value = calibration_value[0] + char
		if len(calibration_value) == 1: # line with only one number
			calibration_value = calibration_value[0] + calibration_value[0]
		sum += int(calibration_value)

print(sum)
