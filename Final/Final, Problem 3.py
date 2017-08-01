def sum_digits(s):
	""" Assumes s is a string
		Returns an int that is the sum of all of the digits in s.
		If there are no digits in s, it raises a ValueError exception. """

	sum = 0
	digitCount = 0
	for item in s:
		try:
			intItem = int(item)
		except ValueError:
			pass
		else:
			sum += intItem
			digitCount += 1

	if digitCount == 0:
		raise ValueError
	else:
		return sum