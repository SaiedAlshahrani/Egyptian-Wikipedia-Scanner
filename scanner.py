import logging
import warnings
import wikipedia
import streamlit as st
from typing import List
from scanner_utils import *
from streamlit import caching
from xgboost import XGBClassifier
from streamlit_searchbox import st_searchbox
from transformers import logging as hflogging

logging.disable(logging.WARNING)
hflogging.set_verbosity_warning()

warnings.simplefilter(action='ignore', category=UserWarning)
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)

st.set_page_config(layout="centered", page_title="Egyptian Wikipedia Scanner", page_icon="🇪🇬")

wikipedia.set_lang("arz")


with open('.streamlit/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.markdown("""
            <h1 style='text-align: center';>Egyptian Arabic Wikipedia Scanner</h1>
            <h5 style='text-align: center';>Automatic Detection of Template-translated Articles in the Egyptian Wikipedia</h5>
            """, unsafe_allow_html=True)


st.markdown("", unsafe_allow_html=True)


def search_wikipedia(searchterm: str) -> List[any]:
    return wikipedia.search(searchterm) if searchterm else []


selected_title = st_searchbox(search_wikipedia, label="Search for an article in Egyptian Arabic Wikipedia:", 
                              placeholder="Search for an article", rerun_on_update=True, clear_on_submit=False, key="wiki_searchbox")


if selected_title:
    X, article, dataframe, selected_title = prepare_features(selected_title)

    st.write(f':black_small_square: Collected Metadata of **{selected_title}**')

    st.dataframe(dataframe, hide_index=True , use_container_width=True)

    loaded_xgb_classifier = XGBClassifier()

    loaded_xgb_classifier.load_model("XGBoost_camelbert_metadata+embeddings.model")

    id2label = {0:'Human-generated Article', 1:'Template-translated Article'}

    result = id2label[int(loaded_xgb_classifier.predict(X))]

    if result =='Human-generated Article':
        st.write(f":black_small_square: Automatic Classification of **{selected_title}**")
        st.success(result, icon="✅")

    else: 
        st.write(f":black_small_square: Automatic Classification of **{selected_title}**") 
        st.error(result, icon="🚨")

    st.write(f":black_small_square: Full Summary of **{selected_title}**")

    with st.expander(f'**{selected_title}**', expanded=True):
        st.markdown('<style>p {text-align: justify;}</style>', unsafe_allow_html=True)
        try:
            article_text = wikipedia.summary(selected_title)

        except wikipedia.exceptions.DisambiguationError as e:
            article_text = wikipedia.summary(e.options[0])
        st.write(article_text)
        st.write(f'> :globe_with_meridians: Read Full Text of **{selected_title}**: <br>{article.url}', unsafe_allow_html=True)
        
        caching.clear_cache()

    st.markdown('<br><br>', unsafe_allow_html=True)


footer="""
        <div class="footer"> <p class="p1">
        Copyright © 2024 by *********************<br>
        Hosted with Streamlit Community Cloud</p> </div>
"""
st.markdown(footer, unsafe_allow_html=True)
