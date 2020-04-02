def get_lcm(num_list): # function to get least common multiple
	greatest = max(num_list) # set greatest as maximum in list
	while True: # while loop until lcm is found
		found = True
		for i in num_list:
			if greatest % i != 0: # lcm must be a multiple of all numbers in given list
				found = False
				break

		if found:
			lcm = greatest
			break

		greatest += 1 # increase number untill lcm is found

	return lcm


def get_gcd(num_list): # function of get greatest common divider
	smallest = min(num_list) # set smallest as minimum in list
	while True: # while loop until gcd is found
		found = True
		for i in num_list:
			if i % smallest != 0: # all numbers in given list must be multiples of gcd
				found = False
				break

		if found:
			gcd = smallest
			break

		smallest -= 1 # decrease number until gcd is found

	return gcd


print get_lcm([2, 4, 5])
print get_gcd([65, 35, 125])