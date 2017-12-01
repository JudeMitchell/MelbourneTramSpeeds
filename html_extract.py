from bs4 import BeautifulSoup
import re

print '***************************'
print '******** TEST AREA ********'
print '***************************'



print '***************************'
print '***************************'
print '***************************'

stop1 = '1-University of Melbourne/Swanston St (Carlton)'
stop2 = '14-Arts Centre/St Kilda Rd (Southbank)'
html_file = "./HTMLS/2010Route1.html"

content = open(html_file, 'r')
soup = BeautifulSoup(content.read(), "html.parser")

tags = soup.find_all(["br", "span"])

for x in range(len(tags)):
	contains_stops = re.search(r'\d{1,3}-[A-Z][A-z /]+\([A-Z][A-z ]+\)', str(tags[x]))
	if contains_stops:
		stops_tag_num = x
		break

stops = re.findall(r'\d{1,3}-[A-Z][A-z /]+\([A-Z][A-z ]+\)', str(tags[stops_tag_num]))

number_stops = len(stops)

stop1_num = stops.index(stop1)

print stop1_num

# determine the number of rows in each little table

# determine the row values for each stop 