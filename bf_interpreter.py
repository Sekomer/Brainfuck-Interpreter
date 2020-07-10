import sys


turing = [0]*30_000   # tape
arr = open(sys.argv[1], "r").read()  # reading data from arr

ptr = 0  # ptr


reading_index = 0
while reading_index < len(arr):
	command = arr[reading_index]
	
	if command == ">":
		ptr += 1
	
	elif command == "<":
		ptr -= 1
	
	elif command == "+":
		turing[ptr] += 1
		if turing[ptr] == 256:
			turing[ptr] = 0
	
	elif command == "-":
		turing[ptr] -= 1
		if turing[ptr] == -1:
			turing[ptr] = 255
	
	elif command == "[":
		if turing[ptr] == 0:
			reading_index += 1
			stack = []
			while reading_index < len(arr):
				if arr[reading_index] == "]" and not stack:
					break
				elif arr[reading_index] == "[":
					stack.append("[") 
				elif arr[reading_index] == "]":
					stack.pop()
				reading_index += 1

	elif command == "]":
		if turing[ptr] != 0:
			reading_index -= 1
			stack = []
			while reading_index > 0:
				if arr[reading_index] == "[" and not stack:
					break
				elif arr[reading_index] == "]":
					stack.append("]") 
				elif arr[reading_index] == "[":
					stack.pop()
				reading_index -= 1

	elif command == ".":
		print(chr(turing[ptr]), end="") 
	
	elif command == ",": 
		turing[ptr] = ord(input("enter val: "))

	reading_index += 1






