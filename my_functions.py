def take_longest_lists(raw_lists, top_rows):

	longest_list_len = len(raw_lists[0])
	if top_rows:
		longest_list_len += 1

	number_raw_lists = len(raw_lists)

	clean_lists = []
	previous_length = 0

	for i in range(number_raw_lists):
		if top_rows:
			if i % longest_list_len == 1:
				clean_lists.append(raw_lists[i])
		else:
			if len(raw_lists[i]) > previous_length:
				clean_lists.append(raw_lists[i])

			previous_length = len(raw_lists[i])

	return clean_lists
