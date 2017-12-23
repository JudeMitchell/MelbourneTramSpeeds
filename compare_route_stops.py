from bs4 import BeautifulSoup
import re
from sys import argv
from my_functions import *

time_regex = r'\d{1,2}:\d{2}'
stop_name_regex = r'\d{1,3}-[A-Z][A-z\s\n/]+\([A-Z][A-z\s\n]+\)'

html2010 = argv[1]
html2015 = argv[2]
htmls = [html2010, html2015]
compare_csv = "stop_comparison_csvs/compare_stops_" + str(re.search(r'Route\d{1,3}', html2010).group(0)) + ".csv"

stops = []
directions = []
stops_tags = []

error_log = open('error_log.txt', 'w')

for i in range(len(htmls)):
	content = open(htmls[i], 'r')
	soup = BeautifulSoup(content.read(), "html.parser")
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

directions_lists = [[re.search(r'([A-z ]+) to ([A-z ]+)', directions[0][0]).group(1), 
					re.search(r'([A-z ]+) to ([A-z ]+)', directions[0][0]).group(2)], 
					[re.search(r'([A-z ]+) to ([A-z ]+)', directions[1][0]).group(1),
					re.search(r'([A-z ]+) to ([A-z ]+)', directions[1][0]).group(2)]]

if directions_lists[0][0] == directions_lists[1][0]:
	order_matching = "FIRST AND FIRST"
	compare_stop_lists(stops[0], stops[2], html2010, directions[0][0])
	compare_stop_lists(stops[1], stops[3], html2010, directions[0][1])

elif directions_lists[0][0] == directions_lists[1][1]:
	order_matching = "FIRST AND SECOND"
	compare_stop_lists(stops[0], stops[3], html2010, directions[0][0])
	compare_stop_lists(stops[1], stops[2], html2010, directions[0][1])

elif directions_lists[0][1] == directions_lists[1][0]:	
	order_matching = "SECOND AND FIRST"
	compare_stop_lists(stops[1], stops[2], html2010, directions[0][1])
	compare_stop_lists(stops[0], stops[3], html2010, directions[0][0])

elif directions_lists[0][1] == directions_lists[1][1]:
	order_matching = "SECOND AND SECOND"
	compare_stop_lists(stops[1], stops[3], html2010, directions[0][1])
	compare_stop_lists(stops[0], stops[2], html2010, directions[0][0])
else:
	print "*** CANNOT IDENTIFY ROUTE DIRECTION MATCH FOR " + str(html2010) + " AND " + str(html2015) + "!!****"
	error_log.write("Cannot identify route direction match for " + html2010 + " and " + html2015)

error_log.close()
