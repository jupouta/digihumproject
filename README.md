# digihumproject
_This is a project made for the course "Introduction to Digital Humanities"_

(The documents contain
  - a Python file
  - two separate image files of the search results of _maahanmuuttaja_ and _pakolainen_
  - two R files of the code for each word.)

## Data
I used the newspaper collection (KLK) from the [Korp API](https://kitwiki.csc.fi/twiki/bin/view/FinCLARIN/KielipankkiHelpKorpWebService) in this project. The collection contains newspaper articles from the 19th century to the 21st century. I searched two words, **_maahanmuuttaja_** and **_pakolainen_**, in the newspapers from the year 1970 to the present day.

## What I did with it
First, I used Python to get the search results from Korp API with json. This data was then filtered to get only the results of the needed sentences. [Here](https://github.com/jupouta/digihumproject/blob/master/Python%20/korp_file.py)'s the code.

To process the files, I used R. I preprocessed the data in order to get it in a usable form, e.g. deleted stopwords and punctuation, and then I used it to create wordclouds for each word, _maahanmuuttaja_ and _pakolainen_. [Here](https://rstudio-pubs-static.s3.amazonaws.com/31867_8236987cf0a8444e962ccd2aec46d9c3.html)'s the webpage I used for reference to do all the code for _maahanmuuttaja_ and for _pakolainen_, which can be seen [here](https://github.com/jupouta/digihumproject/blob/master/R/tutkimuskoodi_maahanmuuttaja.R) and [here](https://github.com/jupouta/digihumproject/blob/master/R/tutkimuskoodi_pakolainen.R).

## What the results show
Here are links to the pictures of the created wordclouds:
[maahanmuuttaja] (https://github.com/jupouta/digihumproject/blob/master/R/maahanmuuttaja_plot.pdf) and [pakolainen](https://github.com/jupouta/digihumproject/blob/master/R/pakolainen_plot.pdf)

In the pictures created, one can see certain resemblance between the two words, but certain differences as well. I will list some of them here:

  - A quite an important difference between _pakolainen_ and _maahanmuuttaja_ seems to be the fact that _pakolainen_ is more related to international events, e.g. Kosovo and UN (YK in Finnish), and refugees, while _maahanmuuttaja_ has something to do with either Finland of the Finnish people (and it seems that they are somehow opposites to immigrants).
  - _maahanmuuttaja_ contains the city of Mikkeli with its inflective forms; in _pakolainen_, Länsisavo is mentioned, the area where Mikkeli is located.
  - _maahanmuuttaja_ contains a lot of the word _klo_, which is probably due to the TV program tables included in the data. Interesting though that apparently, there has been fairly many programs having something to do with immigrants.
  - Both seem to talk about different kinds of amounts (probably about people), words like percentage, thousands, more, a lot.
  - The stopwords list in R isn't sufficient enough, since e.g. _hänen_, _sen_, and _hän_ can be seen on the final results. This could be solved by manually adding a list of words that shouldn't be included in the analysis, but that is a) a lot of work and b) a bit difficult with Finnish. I did "delete" some of the words, for instance _myös_, since it twisted the results a bit.
  - Other important words related to _maahanmuuttaja_ are society, work, Sweden, language, and to _pakolainen_ war, border, country, government, against (vastaan in Finnish, don't know how to translate it without context).
