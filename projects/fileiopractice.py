with open("input.txt", "r") as file:
	numbers = [int(line.strip()) for line in file if line]
	counter = 0

	for i in range(1, len(numbers)):
		if numbers[i] > numbers[i-1]:
			counter += 1

	print(counter)
