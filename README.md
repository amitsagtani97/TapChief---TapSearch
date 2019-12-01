# Description
An indexing based document finder for given set of documents - TapSearch

## Tech Stack
- Flask-Admin
- Material Kit
- Natural Language Toolkit (NLTK)

## Features
- Text Search
- PDF Search


## Instructions for running
The app is deployed on Heroku at - https://tapsearch034.herokuapp.com/


## Pre-processing improvements - 
To improve the query time for each word, what we can do is while preprocessing, for each word, store only top 10 documents sorted in decreasing order of count. In this way we will only process the documents in which the word is most frequent instead of iterating over all the documents. This will save iteration over documents which have very less frequency of that corresponding word. 
