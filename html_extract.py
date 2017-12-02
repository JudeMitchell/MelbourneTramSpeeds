from bs4 import BeautifulSoup
import re

# print '***************************'
# print '******** TEST AREA ********'
# print '***************************'



# print '***************************'
# print '***************************'
# print '***************************'

stop1 = '1-University of Melbourne/Swanston St (Carlton)'
stop2 = '14-Arts Centre/St Kilda Rd (Southbank)'
html_file = "./HTMLS/2010Route1.html"

content = open(html_file, 'r')
soup = BeautifulSoup(content.read(), "html.parser")
tags = soup.find_all(["br", "span"])

for x in range(len(tags)):
	contains_stops = re.search(r'\d{1,3}-[A-Z][A-z\s\n/]+\([A-Z][A-z\s\n]+\)', str(tags[x]))
	if contains_stops:
		stops_tag_num = x
		break

stops_tag = str(tags[stops_tag_num])
stops_tag = stops_tag.replace('<br>', '')
stops_tag = stops_tag.replace('\n', ' ')

number_stops = len(re.findall(r'\d{1,3}-[A-Z]', stops_tag))
stop_names = re.findall(r'\d{1,3}-[A-Z][A-z\s\n/]+\([A-Z][A-z\s\n]+\)', stops_tag)

# extract the stops

# stop1_num = stops.index(stop1)
# stop2_num = stops.index(stop2)

# do I need to know that there was that dodgy stop in there - count the number of lines in the stops tag?