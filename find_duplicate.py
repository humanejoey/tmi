my_list = ["tom", "jerry", "mike", "tom"]

def find_duplicates(name_list):
	dup_set = set()
	for i in range(len(name_list)):
		if name_list[i] in my_list[i+1:]:
			dup_set.add(name_list[i])

	return dup_set

print find_duplicates(my_list)
