# the file

script.dir <- dirname(sys.frame(1)$ofile)

cname <- file.path(script.dir, "../Tiedostot", 
                   "saneet_maahanmuuttaja.txt")

library(tm)

# pre-processing
sana <- readLines(cname, encoding = "UTF-8")
docs <- Corpus(VectorSource(sana))

docs <- tm_map(docs, removePunctuation)
docs <- tm_map(docs, removeWords, stopwords("finnish"))
docs <- tm_map(docs, removeNumbers)
docs <- tm_map(docs, tolower)

# removes words that begin with "maahanmuuttaj" and "myös"
for(w in seq(docs))
{
  docs[[w]] <- gsub("maahanmuuttaj\\S*", "", docs[[w]])
  docs[[w]] <- gsub("myös\\S*", "", docs[[w]])
}

docs <- tm_map(docs, stripWhitespace)
docs <- tm_map(docs, PlainTextDocument)

# stage

dtm <- DocumentTermMatrix(docs)
tdm <- TermDocumentMatrix(docs)

# frequencies

freq <- colSums(as.matrix(dtm))
ord <- order(freq)

dtms <- removeSparseTerms(dtm, 0.1)

freq <- colSums(as.matrix(dtms))
freq <- sort(colSums(as.matrix(dtm)), decreasing=TRUE)

# the plot: not needed to do the wordcloud, but is useful for seeing the frequencies
library(ggplot2)
wf <- data.frame(word=names(freq), freq=freq)

p <- ggplot(subset(wf, freq>15), aes(word, freq))    
p <- p + geom_bar(stat="identity")   
p <- p + theme(axis.text.x=element_text(angle=45, hjust=1))

# the wordcloud
library(wordcloud)

set.seed(142)   
wordcloud(names(freq), freq, min.freq=15)
