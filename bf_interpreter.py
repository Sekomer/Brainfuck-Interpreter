import sys

stack =[]
turing = [0]*100000   # tape
arr = open(sys.argv[1], "r").read()  # reading data from arr

ptr = 1  # ptr
stack_index_counter = 0
stack_index = [0]


reading_index = 0
while reading_index < len(arr):
	command = arr[reading_index]
	if command == ">":
		ptr += 1
	
	elif command == "<":
		ptr -= 1
	
	elif command == "+":
		turing[ptr] += 1
	
	elif command == "-":
		turing[ptr] -= 1
	
	elif command == "[":
		if not len(stack)==0:
			stack_index_counter += 1
		stack_index[stack_index_counter] = reading_index

	elif command == "]":
		if turing[ptr] == 0:
			stack_index_counter -= 1
		else:
			reading_index = stack_index[stack_index_counter]

	elif command == ".":
		print(chr(turing[ptr]), end="") 
	
	elif command == ",": 
		turing[ptr] = int(input("enter val: "))

	reading_index += 1






