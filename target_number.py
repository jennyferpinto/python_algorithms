# for a list of numbers and a target number, return the two numbers that add to target one

list_nums = [2,3,6,4,7]
target_num = 9


def number_checker(list_nums, target_num):
	dict_nums = {}
	for num in range(len(list_nums)):
		dict_nums[list_nums[num]] = target_num - list_nums[num]
		if dict_nums[list_nums[num]] in list_nums:
			print dict_nums[list_nums[num]]


def number_checker_2(list_nums, target_num):
	dict_nums = {}
	for num in range(len(list_nums)):
		dict_nums[list_nums[num]] = target_num - list_nums[num]
	for key, value in dict_nums.iteritems():
		if value in list_nums:
			print (key,value)

print number_checker(list_nums,target_num)

print number_checker_2(list_nums,target_num)
