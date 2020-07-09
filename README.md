# Topic-Modelling-Amazon-Fine-Food-Reviews

We encounter such huge texts of documents time and again. But, before reading the documents, if we can get an overview of what the documents are about, it would make the job so much easy. For example, before watching a movie, if we can watch its trailer, it can help us decide if the movie is worth it. Similarly, we can decide if the documents are worth the effort?

Or, alternatively, if we have a bunch of documents and we can identify each document with their "topic", we can shortlist the documents based on topic of interest - without having to read through all the documents.

In Machine Learning and Natural Language Processing, Topic Models, a type of statistical model, gives us the ability to discover topics from a collection of documents.

# Hereko based App

Below you can find the link to the app, where you can provide your own reviews and find out what the review is about? Please keep in mind the algorithm works best for food/beverages based products that can be commonly found for Amazon's fine foods.

App - https://topic-modelling-amzon-reviews.herokuapp.com/

# DATA

For the project, I used publicly available Amazon's Fine Food reveiws data. It can be accessed [here](http://snap.stanford.edu/data/web-FineFoods.html). The data contains approx. 569,000 reviews from 256,000 users.

![data](https://user-images.githubusercontent.com/45079009/84345478-56d27800-ab62-11ea-9d5d-29df1aea7280.PNG)

This is what a sample from all the words look like.

![xyz](https://user-images.githubusercontent.com/45079009/84370567-4683c280-ab8d-11ea-8e6e-d787b398d864.png)

There is quite a range of words in this. From coffee to chocolate to dog. It is hard to read what kind of topics or themes are actually in the reviews.

# Text Normalization

Cleaning the textual data was very important to get good topics from the reviews. The process involved following steps:

* Removing HTML tags
* Correcting grammar contractions
* Lowercasing the reviews
* Removing numbers and additional white spaces
* Removing Punctuations
* Tokenization
* Remving stopwords (using a long list of words from rank.nl and domain specific words)
* Removing Whitespaces
* Lemmatizing all reviews


