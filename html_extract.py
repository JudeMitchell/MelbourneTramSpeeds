from bs4 import BeautifulSoup
import re
# from sys import argv
from my_functions import *
import csv

time_regex = r'\d{1,2}:\d{2}'
stop_name_regex = r'\d{1,3}-[A-Z][A-z\s\n/]+\([A-Z][A-z\s\n]+\)'

# todo - read these in from a csv
# stop1 = '1-University of Melbourne/Swanston St (Carlton)'
# stop2 = '14-Arts Centre/St Kilda Rd (Southbank)'
html2010 = "./HTMLS/2010Route1.html"
html2015 = "./HTMLS/2015Route1.html"
htmls = [html2010, html2015]
compare_csv = "stop_comparison_csvs/compare_stops_" + str(re.search(r'Route\d{1,3}', html2010).group(0)) + ".csv"

## DIRECTIONS
# todo - scrape these out
direction1 = "East Coburg to South Melbourne"
direction2 = "South Melbourne to East Coburg"

stops2010 = []
stops2015 = []
stops = [stops2010, stops2015]

for i in range(len(htmls)):
	content = open(htmls[i], 'r')
	soup = BeautifulSoup(content.read(), "html.parser")
	tags = soup.find_all(["br", "span"])
	span_tags = soup.find_all("span")

	for j in range(len(tags)):
		contains_stops = re.search(stop_name_regex, str(tags[j]))
		if contains_stops:
			stops_tag_num = j
			break

	stops_tag = str(tags[stops_tag_num])
	stops_tag = stops_tag.replace('<br>', '')
	stops_tag = stops_tag.replace('\n', ' ')

	number_stops = len(re.findall(r'\d{1,3}-[A-Z]', stops_tag))
	stop_names = re.findall(stop_name_regex, stops_tag)

	stops[i] = stop_names

start_suburb2010 = re.search(r"\([A-z ]+\)", stops[0][0]).group(0)
start_suburb2015 = re.search(r"\([A-z ]+\)", stops[1][0]).group(0)

if start_suburb2010 != start_suburb2015:
	stops[1].reverse()

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