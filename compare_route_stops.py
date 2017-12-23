from bs4 import BeautifulSoup
import re
from sys import argv
from my_functions import *
import csv

time_regex = r'\d{1,2}:\d{2}'
stop_name_regex = r'\d{1,3}-[A-Z][A-z\s\n/]+\([A-Z][A-z\s\n]+\)'

html2010 = argv[1]
html2015 = argv[2]
htmls = [html2010, html2015]
# compare_csv = "stop_comparison_csvs/compare_stops_" + str(re.search(r'Route\d{1,3}', html2010).group(0)) + ".csv"

stops = []
directions = []
stops_tags = []

error_log = open('error_log.txt', 'w')

for i in range(len(htmls)):
	content = open(htmls[i], 'r')
	soup = BeautifulSoup(content.read(), "html.parser")
	tags = soup.find_all(["br", "span"])
	# span_tags = soup.find_all("span")

	doc_directions = []
	doc_directions_tag_numbers = []

	for i in range(len(tags)):
		if re.search(r"[A-z ]+ to [A-z ]+", str(tags[i])):
			if not re.search('(day|[Ww]eek|times)', str(tags[i])):
				doc_directions.append(str(tags[i].contents[0]).replace('\n', ''))
				doc_directions_tag_numbers.append(i)

	doc_directions = [doc_directions[0], doc_directions[-1]]
	directions.append(doc_directions)

	for j in range(len(tags)):
		contains_stopsA = re.search(stop_name_regex, str(tags[j]))
		if contains_stopsA:
			stops_tags.append(str(tags[j]))
			stops_tag_numA = j
			break

	for k in range(doc_directions_tag_numbers[int(round(len(doc_directions_tag_numbers),0)/2+2)], len(tags)):
		contains_stopsB = re.search(stop_name_regex, str(tags[k]))
		if contains_stopsB:
			stops_tags.append(str(tags[k]))
			stops_tag_numB = k
			break

	stops_tagA = str(tags[stops_tag_numA])
	stops_tagA = stops_tagA.replace('<br>', '')
	stops_tagA = stops_tagA.replace('\n', ' ')
	stops_tagB = str(tags[stops_tag_numB])
	stops_tagB = stops_tagB.replace('<br>', '')
	stops_tagB = stops_tagB.replace('\n', ' ')

	# number_stops = len(re.findall(r'\d{1,3}-[A-Z]', stops_tag))
	stop_namesA = re.findall(stop_name_regex, stops_tagA)
	stop_namesB = re.findall(stop_name_regex, stops_tagB)


	stops.append(stop_namesA)
	stops.append(stop_namesB)

# DETERMINE ORDERS OF DIRECTIONS
print '***************************'
print '******** TEST AREA ********'
print '***************************'

for i in range(len(stops_tags)):
	print "\t" + str(i)
	print stops_tags[i]
quit()

directions_lists = [[re.search(r'([A-z ]+) to ([A-z ]+)', directions[0][0]).group(1), 
					re.search(r'([A-z ]+) to ([A-z ]+)', directions[0][0]).group(2)], 
					[re.search(r'([A-z ]+) to ([A-z ]+)', directions[1][0]).group(1),
					re.search(r'([A-z ]+) to ([A-z ]+)', directions[1][0]).group(2)]]

if directions_lists[0][0] == directions_lists[1][0]:
	order_matching = "FIRST AND FIRST"
	directionA_stops2010 = extract_stops_list()
	directionB_stops2010 = extract_stops_list()
	directionA_stops2015 = extract_stops_list()
	directionB_stops2015 = extract_stops_list()

elif directions_lists[0][0] == directions_lists[1][1]:
	order_matching = "FIRST AND SECOND"

elif directions_lists[0][1] == directions_lists[1][0]:	
	order_matching = "SECOND AND FIRST"

elif directions_lists[0][1] == directions_lists[1][1]:
	order_matching = "SECOND AND SECOND"
else:
	#TODO print route names to a spreadsheet with cannot determine directions warning
	print "*** CANNOT IDENTIFY ROUTE DIRECTION MATCH FOR " + str(html2010) + " AND " + str(html2015) + "!!****"
	error_log.write("Cannot identify route direction match for " + html2010 + " and " + html2015)

print order_matching

for i in range(doc_directions_tag_numbers[-1], 15000):
	contains_stops_later = re.search(stop_name_regex, str(tags[i]))
	if contains_stops_later:
		# stops_tags.append(str(tags[j]))
		print 'LATER**************'
		print i
		print str(tags[i])



print '***************************'
print '*********** END ***********'
print '***************************'

quit()

# start_suburb2010 = re.search(r"\([A-z ]+\)", stops[0][0]).group(0)
# start_suburb2015 = re.search(r"\([A-z ]+\)", stops[1][0]).group(0)

# if start_suburb2010 != start_suburb2015:
# 	stops[1].reverse()

stops_intersect = (set(stops[0]) & set(stops[1]))

if len(stops[0]) != len(stops[1]):
	if len(stops[0]) > len(stops[1]):	
		stops[1] = stops[1] + ([""] * (len(stops[0]) - len(stops[1])))
	else:
		stops[0] = stops[0] + ([""] * (len(stops[1]) - len(stops[0])))

stops_intersect = list(stops_intersect) + ([""] * (len(stops[0]) - len(stops_intersect)))

compare_csv_file = open(compare_csv, "wb")
csv_writer = csv.writer(compare_csv_file, delimiter=",")
csv_writer.writerow(['Matched Segment List', '2010', '2015'])

for i in range(len(stops[0])):
	csv_writer.writerow([stops_intersect[i], stops[0][i], stops[1][i]])

compare_csv_file.close()
error_log.close()


# possible_directions = []

# for i in range(len(span_tags)):
# 	if re.search(r"[A-z ]+ to [A-z ]+", str(span_tags[i])):
# 		print '\n\t\t***' + str(i)
# 		print span_tags[i].contents[0]



# print stops



# # DETERMINE THE NUMBER OF COLUMNS OF TIMES
# num_time_cols = 0

# for i in range(stops_tag_num):
# 	if re.search('>am', str(tags[i])):
# 		num_time_cols += 1



# ## DIRECTION ONE

# for i in range(len(span_tags)):
# 	if re.search(direction2, str(span_tags[i])):
# 		direction2_start_tag_num = i
# 		break



# ## GET INCOMPLETE TOP ROWS
# tags_with_incomplete_rows = []

# for i in range(stops_tag_num):
# 	if re.search(time_regex, str(tags[i])):
# 		tags_with_incomplete_rows.append(re.findall(time_regex, str(tags[i])))

# incomplete_rows_as_cols = take_longest_lists(tags_with_incomplete_rows, True)

# num_cols_blank_in_top_rows = num_time_cols - len(incomplete_rows_as_cols)

# blank_cols_in_top_rows = []

# for i in range (num_cols_blank_in_top_rows):
# 	blank_cols_in_top_rows.append(['-','-'])

# incomplete_rows_as_cols = blank_cols_in_top_rows + incomplete_rows_as_cols

# ## GET BULK OF TIMETABLE DATA
# tags_with_complete_rows= []

# for i in range(stops_tag_num, direction2_start_tag_num - 1):
# 	if re.search(time_regex, str(tags[i])):
# 		tags_with_complete_rows.append(re.findall(time_regex, str(tags[i])))

# cols_from_full_rows = take_longest_lists(tags_with_complete_rows, False)

# for i in range(0,20):
# 	print cols_from_full_rows[i]


# print '***************************'
# print '******** TEST AREA ********'
# print '***************************'

# print stop_names


# html_file2 = "./HTMLS/2017Route1.html"

# content2 = open(html_file2, 'r')
# soup2 = BeautifulSoup(content2.read(), "html.parser")
# tags2 = soup2.find_all(["br", "span"])
# span_tags2 = soup2.find_all("span")


# for i in range(len(tags2)):
# 	contains_stops2 = re.search(stop_name_regex, str(tags2[i]))
# 	if contains_stops2:
# 		stops_tag_num2 = i
# 		break

# stops_tag2 = str(tags2[stops_tag_num2])
# stops_tag2 = stops_tag2.replace('<br>', '')
# stops_tag2 = stops_tag2.replace('\n', ' ')



# number_stops2 = len(re.findall(r'\d{1,3}-[A-Z]', stops_tag2))
# stop_names2 = re.findall(stop_name_regex, stops_tag2)

# print stop_names2

# print "\n\n INTERSECT"

# print list(set(stop_names) & set(stop_names2))

# print '***************************'
# print '***************************'
# print '***************************'





# text_file = open('direction1_dump.txt', 'w')

# for i in range(direction2_start_tag_num):
# 	if re.search(r'\d{1,2}:\d{2}', str(tags[i])):
# 		text_file.write('\n\t\t***' + str(i))
# 		text_file.write(str(tags[i]))

# text_file.close()






# make sense of the times
# good freaking luck





# stop1_num = stops.index(stop1)
# stop2_num = stops.index(stop2)

# do I need to know that there was that dodgy stop in there - count the number of lines in the stops tag?