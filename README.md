# digihumproject
_This is a project made for the course "Introduction to Digital Humanities"_

## Data
I used the newspaper collection (KLK) from the [Korp API](https://kitwiki.csc.fi/twiki/bin/view/FinCLARIN/KielipankkiHelpKorpWebService) in this project. The collection contains newspaper articles from the 19th century to the 21st century. I searched two words, **_maahanmuuttaja_** and **_pakolainen_**, in the newspapers from the year 1970 to the present day.

## What I did with it
First, I used Python to get the search results from Korp API with json. This data was then filtered to get only the results of the needed sentences.

To process the files, I used R. I preprocessed the data in order to get it in a usable form, e.g. deleted stopwords and punctuation, and then I used it to create wordclouds for each word, _maahanmuuttaja_ and _pakolainen_. [Here](https://rstudio-pubs-static.s3.amazonaws.com/31867_8236987cf0a8444e962ccd2aec46d9c3.html)'s the webpage I used for reference to do all this.

The documents contain
  - a Python file
  - two separate image files of the search results of _maahanmuuttaja_ and _pakolainen_
  - two R files of the code for each word.

## What the results show
In the pictures created, one can see certain resemblance between the two words, but certain differences as well. I will list some of them here:

Maahanmuuttaja: https://github.com/jupouta/digihumproject/blob/master/R/maahanmuuttaja_plot.pdf

Pakolainen: https://github.com/jupouta/digihumproject/blob/master/R/pakolainen_plot.pdf

  - _maahanmuuttaja_ contains a lot of the word _klo_, which is probably due to the TV program tables included in the data. Interesting though that apparently, there has been fairly many programs having something to do with immigrants.
  - Kosovo has been mentioned more with _pakolainen_ than with _maahanmuuttaja_. The same goes with UN (YK in Finnish), which means that when refugees are discussed, it has something to do with international events.
  - Both words include the city of Mikkeli with its inflective forms.
  - In _maahanmuuttaja_, the words with the highest frequency have something to do with either Finland or the Finnish people, which seem to somehow be opposites to each other. This is also a difference between _pakolainen_ and _maahanmuuttaja_ (mentioned above).
  - The stopwords list in R isn't sufficient enough, since e.g. _hänen_, _sen_, and _hän_ can be seen on the final results. This could be solved by manually adding a list of words that shouldn't be included in the analysis, but that is a) a lot of work and b) a bit difficult with Finnish. I did "delete" some of the words, for instance _myös_, since it twisted the results a bit. 
