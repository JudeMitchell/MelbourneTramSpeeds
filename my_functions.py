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


def compare_stop_lists(stopsA, stopsB, html_year1, direction):
	import re
	import csv

	stops_intersect = []
	for stop in stopsA:
		if stop in stopsB:
			stops_intersect.append(stop)

	if len(stopsA) != len(stopsB):
		if len(stopsA) > len(stopsB):	
			stopsB = stopsB + ([""] * (len(stopsA) - len(stopsB)))
		else:
			stopsA = stopsA + ([""] * (len(stopsB) - len(stopsA)))

	stops_intersect = list(stops_intersect) + ([""] * (len(stopsA) - len(stops_intersect)))

	compare_csv = "stop_comparison_csvs/compare_stops_" + str(re.search(r'Route\d{1,3}', html_year1).group(0)) + "_" + direction + ".csv"
	compare_csv_file = open(compare_csv, "wb")
	csv_writer = csv.writer(compare_csv_file, delimiter=",")
	csv_writer.writerow(['Matched Segment List', '_year1', '_year2'])

	for i in range(len(stopsA)):
		csv_writer.writerow([stops_intersect[i], stopsA[i], stopsB[i]])

	compare_csv_file.close()
