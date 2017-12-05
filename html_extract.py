from bs4 import BeautifulSoup
import re
# from sys import argv
from my_functions import *

# todo - read these in from a csv
stop1 = '1-University of Melbourne/Swanston St (Carlton)'
stop2 = '14-Arts Centre/St Kilda Rd (Southbank)'
html_file = "./HTMLS/2010Route1.html"

time_regex = r'\d{1,2}:\d{2}'
stop_name_regex = r'\d{1,3}-[A-Z][A-z\s\n/]+\([A-Z][A-z\s\n]+\)'

content = open(html_file, 'r')
soup = BeautifulSoup(content.read(), "html.parser")
tags = soup.find_all(["br", "span"])
span_tags = soup.find_all("span")

## DIRECTIONS
# todo - scrape these out
direction1 = "East Coburg to South Melbourne"
direction2 = "South Melbourne to East Coburg"

# possible_directions = []

# for i in range(len(span_tags)):
# 	if re.search(r"[A-z ]+ to [A-z ]+", str(span_tags[i])):
# 		print '\n\t\t***' + str(i)
# 		print span_tags[i].contents[0]



for i in range(len(tags)):
	contains_stops = re.search(stop_name_regex, str(tags[i]))
	if contains_stops:
		stops_tag_num = i
		break

stops_tag = str(tags[stops_tag_num])
stops_tag = stops_tag.replace('<br>', '')
stops_tag = stops_tag.replace('\n', ' ')

number_stops = len(re.findall(r'\d{1,3}-[A-Z]', stops_tag))
stop_names = re.findall(stop_name_regex, stops_tag)


# DETERMINE THE NUMBER OF COLUMNS OF TIMES
num_time_cols = 0

for i in range(stops_tag_num):
	if re.search('>am', str(tags[i])):
		num_time_cols += 1



## DIRECTION ONE

for i in range(len(span_tags)):
	if re.search(direction2, str(span_tags[i])):
		direction2_start_tag_num = i
		break



## GET INCOMPLETE TOP ROWS
tags_with_incomplete_rows = []

for i in range(stops_tag_num):
	if re.search(time_regex, str(tags[i])):
		tags_with_incomplete_rows.append(re.findall(time_regex, str(tags[i])))

incomplete_rows_as_cols = take_longest_lists(tags_with_incomplete_rows, True)

num_cols_blank_in_top_rows = num_time_cols - len(incomplete_rows_as_cols)

blank_cols_in_top_rows = []

for i in range (num_cols_blank_in_top_rows):
	blank_cols_in_top_rows.append(['-','-'])

incomplete_rows_as_cols = blank_cols_in_top_rows + incomplete_rows_as_cols

## GET BULK OF TIMETABLE DATA
tags_with_complete_rows= []

for i in range(stops_tag_num, direction2_start_tag_num - 1):
	if re.search(time_regex, str(tags[i])):
		tags_with_complete_rows.append(re.findall(time_regex, str(tags[i])))

cols_from_full_rows = take_longest_lists(tags_with_complete_rows, False)



print '***************************'
print '******** TEST AREA ********'
print '***************************'



print '***************************'
print '***************************'
print '***************************'





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