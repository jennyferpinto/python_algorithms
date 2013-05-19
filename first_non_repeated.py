# return the first non repeated character in a string

string = 'bananas'

def find_original(string):
	count_dict = {}
	order = []
	for char in string:
		if char in count_dict:
			count_dict[char] += 1
		else:
			count_dict[char] = 1
			order.append(char)
	for x in order:
		if count_dict[x] == 1:
			return x
	return None

print find_original(string)


def find_original_2(s):
	counts = {}
	for c in s:
		counts[c] = counts.get(c,1)
	print counts
	for c in s:
		if counts[c] == 1:
			return c

	return None

print find_original_2(string)