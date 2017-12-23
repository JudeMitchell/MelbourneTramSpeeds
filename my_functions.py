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


def extract_stops_list(tags):
	stop_name_regex = r'\d{1,3}-[A-Z][A-z\s\n/]+\([A-Z][A-z\s\n]+\)'

	for i in range(len(tags)):
		contains_stops = re.search(stop_name_regex, str(tags[i]))
		if contains_stops:
			stops_tags.append(str(tags[j]))
			print str(tags[j])
			stops_tag_num = j
			break

	stops_tag = str(tags[stops_tag_num])
	stops_tag = stops_tag.replace('<br>', '')
	stops_tag = stops_tag.replace('\n', ' ')

	number_stops = len(re.findall(r'\d{1,3}-[A-Z]', stops_tag))
	stop_names = re.findall(stop_name_regex, stops_tag)

	return stop_names