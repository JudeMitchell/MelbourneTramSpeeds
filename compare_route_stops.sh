## convert PDF to HTML
touch pdf_file_names.txt

ls ./PDFS | cut -d '.' -f 1 > pdf_file_names.txt

cat pdf_file_names.txt | while read filename
do
	echo $filename
	pdf2txt.py -o ./HTMLS/$filename.html ./PDFS/$filename.pdf
done

rm pdf_file_names.txt


## pull out stops names from matching route pairs

touch html_file_names.txt

ls ./HTMLS | cut -d '.' -f 1 > html_file_names.txt

cat html_file_names.txt | while read html_file_name
do
	if [ "${html_file_name:0:4}" = "2010" ]
	then
		grep -q "2015Route${html_file_name:9}$" html_file_names.txt                                                                 
	    if [ $? -eq 0 ] ; then
	        echo ${html_file_name:9}
	        python compare_route_stops.py 	"./HTMLS/2010Route${html_file_name:9}.html" "./HTMLS/2015Route${html_file_name:9}.html" 
		fi
	fi
done

rm html_file_names.txt
