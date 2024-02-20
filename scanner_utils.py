import re
import requests
import wikipedia
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from transformers import AutoModel
from transformers import BertTokenizer


def clean_page_text(text):
    text = re.sub(r'[^\w\s]', ' ', text) #Replaces the non-alphanumeric characters with spaces.
    text = re.sub(r'[^\u0600-\u06FF]', ' ', text) #Replaces the non-Arabic characters with spaces.
    text = re.sub(r'\s+', ' ', text) #Replaces extra spaces with a single space.
    return text

@st.cache_resource
def encode_page_text(page_text):
    tokenizer = BertTokenizer.from_pretrained('CAMeL-Lab/bert-base-arabic-camelbert-mix-pos-egy')
    model = AutoModel.from_pretrained('CAMeL-Lab/bert-base-arabic-camelbert-mix-pos-egy')

    tokenized_page_text  = tokenizer(page_text, return_tensors='pt', max_length=512, truncation=True)
    encoded_page_text = model(**tokenized_page_text)[0][0][0].tolist()

    return encoded_page_text


def get_page_info(title):
    page_info = f"https://xtools.wmcloud.org/api/page/articleinfo/arz.wikipedia.org/{title}?format=json"

    creation_date = eval(str(BeautifulSoup(requests.get(page_info).content, "html.parser")).replace('null', 'None'))['created_at']
    creator_name = eval(str(BeautifulSoup(requests.get(page_info).content, "html.parser")).replace('null', 'None'))['author']
    total_edits = eval(str(BeautifulSoup(requests.get(page_info).content, "html.parser")).replace('null', 'None'))['revisions']
    total_editors = eval(str(BeautifulSoup(requests.get(page_info).content, "html.parser")).replace('null', 'None'))['editors']

    return creation_date, creator_name, total_edits, total_editors


def get_page_prose(title):
    page_prose = f"https://xtools.wmcloud.org/api/page/prose/arz.wikipedia.org/{title}?format=json"

    total_bytes = eval(str(BeautifulSoup(requests.get(page_prose).content, "html.parser")).replace('null', 'None'))['bytes']
    total_words = eval(str(BeautifulSoup(requests.get(page_prose).content, "html.parser")).replace('null', 'None'))['words']
    total_chars = eval(str(BeautifulSoup(requests.get(page_prose).content, "html.parser")).replace('null', 'None'))['characters']

    return total_bytes, total_words, total_chars


def prepare_features(selected_title):
    dataframe = get_metadata_features(selected_title)
    
    try:
        article = wikipedia.page(selected_title)
        full_article_text = clean_page_text(article.content)
    
    except wikipedia.exceptions.DisambiguationError as e:
        selected_title = e.options[0]
        article = wikipedia.page(selected_title)
        full_article_text = clean_page_text(article.content)

    encode_full_article_text = encode_page_text(full_article_text)

    X = []
    
    for i in range(dataframe.shape[0]):
        x = [] 
        x.append(dataframe['Total Edits'][i])
        x.append(dataframe['Total Editors'][i])
        x.append(dataframe['Total Bytes'][i])
        x.append(dataframe['Total Characters'][i])
        x.append(dataframe['Total Words'][i])
        
        # Both page_metadata + page_text_embeddings
        X.append(np.hstack([x, list(encode_full_article_text)])) 

    return X, article, dataframe, selected_title


def get_metadata_features(selected_title):
    creation_date, creator_name, total_edits, total_editors = get_page_info(selected_title)
    total_bytes, total_words, total_chars = get_page_prose(selected_title)
    
    data = {'Total Edits':[total_edits], 'Total Editors':[total_editors], 'Total Bytes':[total_bytes],
            'Total Characters':[total_chars], 'Total Words':[total_words], 'Creator Name':[creator_name],
            'Creation Date':[creation_date]}  
    
    dataframe = pd.DataFrame(data)

    return dataframe
