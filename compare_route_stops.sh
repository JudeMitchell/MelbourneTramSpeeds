touch pdf_file_names.txt

ls ./PDFS | cut -d '.' -f 1 > pdf_file_names.txt

cat pdf_file_names.txt | while read filename
do
	echo $filename
	pdf2txt.py -o ./HTMLS/$filename.html ./PDFS/$filename.pdf
done

rm pdf_file_names.txt
