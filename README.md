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

# Modelling

1. K-Means - Identified 15 topics using k-means. Evaluated topics using SSE

![kmeans](https://user-images.githubusercontent.com/45079009/87081668-99798580-c1de-11ea-80ab-04ace390316c.PNG)

2. LDA - Identified 16 topics using LDA. Evaluated the topics using coherence scores  

![lda_final_vis](https://user-images.githubusercontent.com/45079009/87081814-d5ace600-c1de-11ea-98fb-0d43d31225ee.PNG)

3. NMF - Identified 11 topics using NMF. Evaluated the topics using coherence scores  

# Conclusion

LDA does a better job here. Both the models have been good picking the topics for majority of documents but LDA takes a slight edge, so I'm gonna use it as my final model here. The final LDA model was deployed using Flask and Heroku.
