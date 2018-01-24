route_number = "1"
year1 = "2010"
year2 = "2015"

north_direction = "South Melbourne to East Coburg"
north_stops = {
	'stopa_year1' : "",
	'stopa_year2' : "",
	'stopb_year1' : "",
	'stopb_year2' : "",
}

south_direction = "East Coburg to South Melbourne"
south_stops = {
	'stopa_year1' : "",
	'stopa_year2' : "",
	'stopb_year1' : "",
	'stopb_year2' : "",
}

html_year1 = open("./HTMLS/" + year1 + "Route" + route_number + ".html", 'r')
html_year2 = open("./HTMLS/" + year2 + "Route" + route_number + ".html", 'r')

htmls = [html_year1, html_year2]
both_tags = []

for i in range(len(htmls)):
	tags = soup.find_all(["br", "span"])

	doc_directions = []
	doc_directions_tag_numbers = []

	for i in range(len(tags)):
		if re.search(r"[A-z ]+ to [A-z ]+", str(tags[i])):
			if not re.search('(day|times)', str(tags[i])):
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

	stops_tagA = stops_tagA.replace('\n', ' ')
	stops_tagA = stops_tagA.replace('<br>', '')
	stops_tagB = str(tags[stops_tag_numB]) 
	stops_tagB = stops_tagB.replace('\n', ' ')
	stops_tagB = stops_tagB.replace('<br>', '')

	stop_namesA = re.findall(stop_name_regex, stops_tagA)
	stop_namesB = re.findall(stop_name_regex, stops_tagB)

	stops.append(stop_namesA)
	stops.append(stop_namesB)



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