def max_val(t):
	""" t, tuple or list
		Each element of t is either an int, a tuple, or a list.
		No tuple or list is empty.
		Returns the maximum in in t or (recusively) in an element of t. """

	def flatten(input_list):
		output_list = []
		for element in input_list:
			if type(element) == list or type(element) == tuple:
				output_list.extend(flatten(element))
			else:
				output_list.append(element)
		return output_list

	newList = flatten(t)
	return max(newList)