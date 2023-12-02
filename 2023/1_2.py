'''
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
'''

## advent of code 2023 day 1 part two
# Sandra Castilho

input_file = "1.input"

def is_number(word):
	return word in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or word in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

number_dict = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}

NUMBER_MIN_LETTERS = 3
NUMBER_MAX_LETTERS = 5

with open(input_file, "r") as file:
	sum = 0
	lines = file.read().splitlines() # lines with '\n' trimmed
	for line in lines:
		calibration_value = ""
		for i in range(len(line)):
			char = line[i]
			if is_number(char): # 1,2,3, etc...
				if len(calibration_value) == 0: # first number
					calibration_value += char
				else:
					calibration_value = calibration_value[0] + char
				continue # next number
			else: # building the buffer
				buffer = ""
				for c in line[i:i+NUMBER_MAX_LETTERS]:
					buffer += c
					if len(buffer) < NUMBER_MIN_LETTERS: # can't yet be a number
						continue
					elif len(buffer) > NUMBER_MAX_LETTERS: # can no longer be a number
						break
					else: # NUMBER_MIN_LETTERS <= buffer <= NUMBER_MAX_LETTERS
						if is_number(buffer): # one, two, etc...
							if len(calibration_value) == 0: # firstnumber
								calibration_value += number_dict[buffer]
							else:
								calibration_value = calibration_value[0] + number_dict[buffer]
							break # number found, next
		if len(calibration_value) == 1: # line with only one number
			calibration_value = calibration_value[0] + calibration_value[0]
		sum += int(calibration_value)

print(sum)
