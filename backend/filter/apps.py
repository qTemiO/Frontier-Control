from django.apps import AppConfig

import pandas as pd
import numpy as np
import re

import nltk
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer 

nltk.download('omw-1.4')

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from loguru import logger

STOPWORDS = set(stopwords.words('russian'))
MIN_WORDS = 4
MAX_WORDS = 200

PATTERN_S = re.compile("\'s;")  # matches `'s` from text
PATTERN_RN = re.compile("\\r\\n")  # matches `\r` and `\n`
PATTERN_PUNC = re.compile(r"[^\w\s]")  # matches all non 0-9 A-z whitespace


def clean_text(text):
    """
    Series of cleaning. String to lower case, remove non words characters and numbers.
    text (str): input text
    return (str): modified initial text
    """
    text = str(text).lower()  # lowercase text
    text = re.sub(PATTERN_S, ' ', text)
    text = re.sub(PATTERN_RN, ' ', text)
    text = re.sub(PATTERN_PUNC, ' ', text)
    return text


def tokenizer(sentence, min_words=MIN_WORDS, max_words=MAX_WORDS, stopwords=STOPWORDS, lemmatize=True):

    if lemmatize:
        stemmer = WordNetLemmatizer()
        tokens = [stemmer.lemmatize(w) for w in word_tokenize(sentence)]
    else:
        tokens = [w for w in word_tokenize(sentence)]
    token = [w for w in tokens if (len(w) > min_words and len(w) < max_words
                                    and w not in stopwords)]
    return tokens

def clean_sentences(df):
    """
    Remove irrelavant characters (in new column clean_sentence).
    Lemmatize, tokenize words into list of words (in new column tok_lem_sentence).
    """
    print('Cleaning sentences...')
    df['clean_sentence'] = df['OPISANIE_SPR'].apply(clean_text)
    df['tok_lem_sentence'] = df['clean_sentence'].apply(
        lambda x: tokenizer(x, min_words=MIN_WORDS, max_words=MAX_WORDS, stopwords=STOPWORDS, lemmatize=True))
    return df

def extract_best_indices(m, topk, mask=None):
    """
    Use sum of the cosine distance over all tokens.
    m (np.array): cos matrix of shape (nb_in_tokens, nb_dict_tokens)
    topk (int): number of indices to return (from high to lowest in order)
    """
    # return the sum on all tokens of cosinus for each sentence
    if len(m.shape) > 1:
        cos_sim = np.mean(m, axis=0)
    else:
        cos_sim = m
    index = np.argsort(cos_sim)[::-1]  # from highest idx to smallest score
    if mask is not None:
        assert mask.shape == m.shape
        mask = mask[index]
    else:
        mask = np.ones(len(cos_sim))
    # eliminate 0 cosine distance
    mask = np.logical_or(cos_sim[index] != 0, mask)
    best_index = index[mask][:topk]
    return best_index

def stemming(df):
    russian_stopwords = stopwords.words("russian")
    russian_stopwords.extend(['…', '«', '»', '...', 'т.д.', 'т', 'д'])

    stemmer = SnowballStemmer("russian") 
    stemmed_texts_list = []
    for text in df['clean_sentence']:
        tokens = word_tokenize(text)    
        stemmed_tokens = [stemmer.stem(token) for token in tokens if token not in russian_stopwords]
        text = " ".join(stemmed_tokens)
        stemmed_texts_list.append(text)
        
    return stemmed_texts_list

def get_recommendations_tfidf(sentence, tfidf_mat, vectorizer):
    
    """
    Return the database sentences in order of highest cosine similarity relatively to each 
    token of the target sentence. 
    """
    russian_stopwords = stopwords.words("russian")
    russian_stopwords.extend(['…', '«', '»', '...', 'т.д.', 'т', 'д'])
    stemmer = SnowballStemmer("russian")
    # Embed the query sentence
    sentence = sentence.upper()
    tokens = [str(tok) for tok in tokenizer(sentence)]
    stems = [stemmer.stem(token) for token in tokens if token not in russian_stopwords]    
    vec = vectorizer.transform(stems)
    # Create list with similarity between query and dataset
    mat = cosine_similarity(vec, tfidf_mat)
    # Best cosine distance for each token independantly
    print(mat.shape)
    best_index = extract_best_indices(mat, topk=35)
    return best_index

class FilterConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filter'

    VECTOR_FILTER_DATAFRAME = pd.read_csv(
        '../backend/filter/data/model_dataframe.csv', encoding='mbcs', sep=';')

    logger.debug(f'\n{VECTOR_FILTER_DATAFRAME}')

    VECTOR_FILTER_DATAFRAME = VECTOR_FILTER_DATAFRAME.drop_duplicates()

    VECTOR_FILTER_DATAFRAME = clean_sentences(VECTOR_FILTER_DATAFRAME)
    VECTOR_FILTER_DATAFRAME.dropna(inplace=True)
    # Adapt stop words
    token_stop = tokenizer(' '.join(STOPWORDS), lemmatize=False)
    # Fit TFIDF
    vectorizer = TfidfVectorizer(stop_words=token_stop, tokenizer=tokenizer)
    
    VECTOR_FILTER_DATAFRAME['stemmed_clean'] = stemming(VECTOR_FILTER_DATAFRAME)
    tfidf_mat = vectorizer.fit_transform(VECTOR_FILTER_DATAFRAME['stemmed_clean'].values) # -> (num_sentences, num_vocabulary)
    
    logger.success('All installed and prepared\nFZ data')

    def predict(query_sentence, tfidf_mat, df, vectorizer):
        best_index = get_recommendations_tfidf(query_sentence, tfidf_mat, vectorizer)
        return df[['KOD_TNVED_SPR', 'OPISANIE_SPR']].iloc[best_index][:10]

class FilterUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filter'

    VECTOR_USER_FILTER_DATAFRAME = pd.read_csv(
        '../backend/filter/data/user_dataframe.csv', encoding='mbcs', sep=';')

    VECTOR_USER_FILTER_DATAFRAME = VECTOR_USER_FILTER_DATAFRAME.drop(columns=['DATA'])
    VECTOR_USER_FILTER_DATAFRAME['OPISANIE_SPR'] = VECTOR_USER_FILTER_DATAFRAME['OPISANIE']
    VECTOR_USER_FILTER_DATAFRAME = VECTOR_USER_FILTER_DATAFRAME.drop(columns=['OPISANIE'])

    logger.debug(f'\n{VECTOR_USER_FILTER_DATAFRAME}')

    VECTOR_USER_FILTER_DATAFRAME = clean_sentences(VECTOR_USER_FILTER_DATAFRAME)
    VECTOR_USER_FILTER_DATAFRAME.dropna(inplace=True)

    # Adapt stop words
    token_stop = tokenizer(' '.join(STOPWORDS), lemmatize=False)
    # Fit TFIDF
    vectorizer = TfidfVectorizer(stop_words=token_stop, tokenizer=tokenizer)
    
    VECTOR_USER_FILTER_DATAFRAME['stemmed_clean'] = stemming(VECTOR_USER_FILTER_DATAFRAME)
    tfidf_mat = vectorizer.fit_transform(VECTOR_USER_FILTER_DATAFRAME['stemmed_clean'].values) # -> (num_sentences, num_vocabulary)
    
    logger.success('All installed and prepared\nUser data')

    def predict(query_sentence, tfidf_mat, df, vectorizer):
        best_index = get_recommendations_tfidf(query_sentence, tfidf_mat, vectorizer)
        return df[['TNVED', 'OPISANIE_SPR']].iloc[best_index][:10]
