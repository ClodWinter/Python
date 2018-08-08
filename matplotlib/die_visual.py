from die import Die

die = Die()

results = []

for number in range(1,1000):
	result = die.roll()
	results.append(result)

frequencies = []

for value in range(1,die.num_sides + 1):
	frequency = results.count(value)
	frequencies.append(frequency)

print(frequencies)