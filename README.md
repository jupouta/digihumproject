# digihumproject
Project made for the course "Introduction to digital humanities"

I used the newspaper collection (KLK) from the Korp API in this project. The collection contains newspaper articles from the 19th century to the 21st century. I chose two words, "maahanmuuttaja" and "pakolainen" for my little research, and searched them in the newspapers from the year 1970 to the present day.

I used Python to get the search results from Korp API with json.

To process the files, I used R. I preprocessed the data in order to get it in a usable form, and then I used it to create wordclouds for each word, "maahanmuuttaja" and "pakolainen".

The documents contain
- a Python file
- two separate files for "maahanmuuttaja" and "pakolainen"
- two R files for each word.

From the pictures created, one can see certain resemblance between the two words, but certain differences as well. I will list some of them here:
- maahanmuuttaja contains a lot of the word "klo", which is probably due to the TV program tables included in the data. Interesting though that apparently, there has been fairly many programs having something to do with immigrants.
- Kosovo has been mentioned more with pakolainen than with maahanmuuttaja.
- Both words include the city Mikkeli with its inflective forms.
