#!/usr/bin/env python
# coding: utf-8

# In[8]:


from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.naive_bayes import MultinomialNB
from gensim import corpora
from nltk import word_tokenize
from gensim.corpora import Dictionary
import spacy
import re
import string
from pattern.en import lemma, lexeme
#loading spacy -en
#from sklearn.externals import joblib
import pickle
nltk.download('punkt')


# In[9]:


# load the model from disk
filename = 'final-lda-model.pkl'
lda = pickle.load(open(filename, 'rb'))
with open('stop_words_amazon', 'rb') as f:
    stop_words = pickle.load(f)

with open('lda_dictionary', 'rb') as f:
    dct_lda = pickle.load(f)


# In[ ]:


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
             6:'Sweet Snacks(Chocolates)',7:'Beverages (Juices)',8:'Gifts/High Calorie Foods', 9:'Spicy Food/ Soups',10:'A Baking Recipe',11:'Pet Issues',
             12:'Tea(s)',13:'Salty Snacks(Crackers)', 14:'Hair Products/ Cat Issues', 15: 'Coffee'}
    
    #nlp = spacy.load('en_core_web_sm')



    def clean_text(text):
        text = text.lower() #lower-casing
        text = [i for i in word_tokenize(text) if i not in stop_words] #remvoving stop-words
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
        doc_vector_lda = dct_lda.doc2bow(word_tokenize(document))
        topic1,perc1 = sorted(lda[doc_vector_lda],key = lambda x:x[1],reverse = True)[0]
        return lda_theme[topic1]
        #print("LDA predicts this document to be talking about",'\x1b[1;31m'+ lda_theme[topic1]  +'\x1b[0m')
        
    if request.method == 'POST':
        message = request.form['message']
        data = message
        #vect = cv.transform(data).toarray()
        my_prediction = predict_topic(data)
    return render_template('home.html',prediction_text = 'Your review is about ' + my_prediction)



if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




