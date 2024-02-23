import streamlit as st
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from wordcloud import WordCloud
import os
import re 
import json
import spacy
from spacy import displacy
from dotenv import load_dotenv

# load the GOOGLE / OPENAI- API KEY FROM .env 
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""


#Generalised function for prompting!
model = ChatGoogleGenerativeAI(model="gemini-pro")

def prompt_func(Question,Context):

    response=model.invoke(Question+"\n"+Context)
    return response.content

# function for extracting the key points from the context
def extract_key_points(input_text):
    response = prompt_func("Please find the key insights from the below text in maximum of 3 bullet points:",
    input_text)

    return response

# function for generating most_positive_words
def most_positive_words(text):
    response = prompt_func("Please extract the most positive keywords from the below text\n",text)

    return response

#function for generating the word cloud
def generate_wordcloud(text):
    # Create and generate a word cloud image
    wordcloud = WordCloud(width=800, height=800,
    background_color='black', min_font_size=10).generate(text)
    # Save the wordcloud image to disk
    wordcloud.to_file("wordcloud.png")
    # Return the image path
    return "wordcloud.png"




def ner(text):

# # Specify the path to the local cache directory
#     custom_data_path = r"E:\Langchain\GenerativeAI\TextAnalysis\cache"
# # Set the SPACY_DATA environment variable to the custom data path
#     os.environ['SPACY_DATA'] = custom_data_path
# # Load the spaCy model
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    html =displacy.render(doc, style='ent')
    html = html.replace("\n\n","\n")
    st.write(HTML_WRAPPER.format(html),unsafe_allow_html=True)
 


# Streamlit code
st.set_page_config(layout="wide")
st.title("Ai powered Text Analysis App :page_with_curl:")

with st.expander("About this application"):
    st.markdown("This app is built using the [Google Gemini](https://ai.google.dev/), Streamlit, and Spacy.")

input_text = st.text_area("Enter your text to analyze")


if input_text is not None:
    if st.button("Analyze Text"):
        st.markdown("**Input Text**")
        st.info(input_text)
        
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.markdown("**Output Text**")
            st.image(generate_wordcloud(input_text))
        with col1:
            st.markdown("**Key Findings based on your Text**")
            st.success(extract_key_points(input_text))
        with col3:
            st.markdown("**Most Positive Words**")
            st.success(most_positive_words(input_text))
        
        st.markdown("**Named Entity Recognition**")
        ner(input_text)
