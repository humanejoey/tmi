my_list = [17, 92, 18, 33, 58, 7, 33, 42]

def find_max(num_list):
	max_index = 0
	for i in range(len(num_list)):
		if num_list[i] > num_list[max_index]:
			max_index = i

	return max_index, num_list[max_index]

print find_max(my_list)
