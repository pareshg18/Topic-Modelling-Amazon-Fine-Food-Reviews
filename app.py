#!/usr/bin/env python
# coding: utf-8

#Topic- Modelling app by Paresh Gupta

from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.naive_bayes import MultinomialNB
from gensim import corpora
#from nltk import word_tokenize
from gensim.corpora import Dictionary
#import spacy
import re
import string
from pattern.en import lemma, lexeme
#loading spacy -en
#from sklearn.externals import joblib
import pickle
#import nltk
#nltk.download('punkt')


# In[9]:


# load the model from disk
filename = 'final-lda-model.pkl'
lda = pickle.load(open(filename, 'rb'))
with open('stop_words_amazon', 'rb') as f:
    stop_words = pickle.load(f)

with open('lda_dictionary', 'rb') as f:
    dct_lda = pickle.load(f)

file2 = 'topic_distribution.pkl'
topic_distribution = pickle.load(open(file2, 'rb'))

file3 = 'reviews_original.pkl'
reviews = pickle.load(open(file3, 'rb'))
    

file4 = 'indexes.pkl'
indexes = pickle.load(open(file4, 'rb'))


#cv=pickle.load(open('tranform.pkl','rb'))


# In[10]:


app = Flask(__name__)


# In[ ]:


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])

def predict():
    
    
    lda_theme = {0:'Delivery/ Order Related Issues',1:'Breakfast Food',2:'Chewing Gums/ Dog Treats',3:'Bad Products',4:'Energy Drinks/ Sports Drinks',5:'Packaging Bags',
             6:'Sweet Snacks (like Chocolates?)',7:'Beverages (Juices)',8:'Gifts/High Calorie Foods', 9:'Spicy Food/ Soups',10:'A Baking Recipe',11:'Pet Issues',
             12:'Tea(s)',13:'Salty Snacks (lie Crackers?)', 14:'Hair Products/ Cat Issues', 15: 'Coffee'}
    
    #nlp = spacy.load('en_core_web_sm')



    def clean_text(text):
        text = text.lower() #lower-casing
        text = [i for i in text.split(" ") if i not in stop_words] #remvoving stop-words
        #doc = nlp(' '.join(text))
        #text = [token.lemma_ for token in doc] #lemmatizing the reviews
        text = [lemma(wd) for wd in text]
    
        text = ' '.join(text)    
        text = re.sub(r'\d+','',text) #removing numbers
        #removing punctuation
        punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        text = ''.join([i for i in text if i not in punctuation])
        
        #text = text.translate(str.maketrans('','',string.punctuation)) #removing punctuation
        text = text.strip() #removing white-spaces
        return text
    
    #predicting LDA topic
    def predict_topic(document):
        document = clean_text(document)        
        doc_vector_lda = dct_lda.doc2bow(document.split(" "))
        topic1,perc1 = sorted(lda[doc_vector_lda],key = lambda x:x[1],reverse = True)[0]
        no_docs = topic_distribution.total_documents[topic_distribution.topic_no == topic1]
        temp = no_docs.at[topic1]
        return [lda_theme[topic1],temp,topic1]
    
    def get_reviews(topic):
        temp = []
        for j in range(3):
            temp.append(reviews.review[reviews.indexing == indexes[topic][1][j]].values[0])
        return temp

              
    if request.method == 'POST':
        message = request.form['message']
        if len(message) == 0:
            return render_template('home.html',prediction_text1 = 'Please provide an input')        
        
        data = message
        
        output = predict_topic(data)
        rev = get_reviews(output[2])
        pred1 = output[0]
        pred2 = output[1]
    return render_template('home.html',prediction_text1 = 'Your review is about ' + pred1, prediction_text2 = 'There are a total of ' + "{:,.0f}".format(pred2) + ' reviews available on ' + pred1 + '. Here are the top 3 reviews closest to your review:',prediction_text3 = '1. ' + rev[0],prediction_text4 = '2. ' + rev[1],prediction_text5 = '3. ' + rev[2])


if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




