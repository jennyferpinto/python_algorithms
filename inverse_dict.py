# inverting a dictionary with two different methods

d = {'a': 2, 'b': 4, 'c': 2, 'd': 4, 'f': 0}

def invert_dict(d):
	inverse = {}
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse

print invert_dict(d)

def invert_dict_2(dictionary):
	inverse = {}
	for key, val in dictionary.iteritems():
		inverse.setdefault(val, []).append(key)
	return inverse

print invert_dict_2(d)

# if__name__ == '__main__':
# 	d = dict(a=1, b=2, c=3, z=1)
# 	inverse = invert_dict_2(d)
# 	for val, keys in inverse.iteritems():
# 		print val, keys