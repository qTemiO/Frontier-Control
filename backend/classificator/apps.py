from django.apps import AppConfig

from loguru import logger
from joblib import load

import pandas as pd
import numpy as np
import string
import nltk
import re
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import *

from string import punctuation
from pymystem3 import Mystem

from filter.apps import FilterUserConfig

nltk.download('stopwords')

def remove_punctuation(text):
    return "".join([ch if ch not in string.punctuation else ' ' for ch in text])

def remove_numbers(text):
    return ''.join([i if not i.isdigit() else ' ' for i in text])

def remove_multiple_spaces(text):
    return re.sub(r'\s+', ' ', text, flags=re.I)

mystem = Mystem() 
russian_stopwords = nltk.corpus.stopwords.words('russian')
russian_stopwords.extend(['…', '«', '»', '...', 'т.д.', 'т', 'д','а','и','\n'])

def lemmatize_text(text):
    tokens = mystem.lemmatize(text.lower())
    tokens = [token for token in tokens if token not in russian_stopwords and token != " "]
    text = " ".join(tokens)
    return text

def remove_stop_words(text):
    tokens = word_tokenize(text) 
    tokens = [token for token in tokens if token not in russian_stopwords and token != ' ']
    return " ".join(tokens)

class ClassificatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'classificator'

    logreg = 0
    with open('../backend/classificator/model/probility.joblib', 'rb') as fid:
        logreg = load(fid)

    df_res = FilterUserConfig.VECTOR_USER_FILTER_DATAFRAME

    def predict(text, df_res, logreg):
        tech_text = remove_multiple_spaces(remove_numbers(remove_punctuation(text.lower())))
        tech_text = remove_stop_words(tech_text)
        tech_text = lemmatize_text(tech_text)

        my_tags=df_res['TNVED'].unique()
        tech_pred = logreg.predict_proba([tech_text])

        data_res=pd.DataFrame()
        data_res['class']=my_tags
        data_res['predict']=np.round(tech_pred[0],4)
        return data_res.sort_values(by='predict',ascending=False)[:5]

    logger.success('Classificator is ready!')