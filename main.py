from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext

# Function to analyze text sentiment
def analyze_text(text):
    blob = TextBlob(text)
    polarity = round(blob.sentiment.polarity, 2)
    subjectivity = round(blob.sentiment.subjectivity, 2)
    return polarity, subjectivity

# Function to clean text
def clean_text(text):
    return cleantext.clean(text, clean_all=False, extra_spaces=True, stopwords=True, lowercase=True, numbers=True, punct=True)

# Function to score sentiment
def score_sentiment(x):
    if x >= 0.5:
        return 'Positive'
    elif x <= 0.5:
        return 'Negative'
    else:
        return 'Neutral'

# Function to analyze CSV file
def analyze_csv(file):
    df = pd.read_csv(file)
    df['score'] = df['tweet'].apply(lambda x: TextBlob(x).sentiment.polarity)
    df['analysis'] = df['score'].apply(score_sentiment)
    return df

# User Interface
st.title('Sentiment Analyzer')

text = st.text_input('Type or paste the text you want to analyze: ')
if text:
    polarity, subjectivity = analyze_text(text)
    st.write('Polarity:', polarity)
    st.write('Subjectivity:', subjectivity)

pre = st.text_input('Type or paste the text you want to clean: ')
if pre:
    st.write(clean_text(pre))

upload = st.file_uploader('Upload File')

if upload:
    df = analyze_csv(upload)
    st.write(df.head(10))

    @st.cache_data
    def convert_df_to_csv(df):
        return df.to_csv().encode('utf-8')
    
    csv = convert_df_to_csv(df)

    st.download_button(
        label="Download as CSV file",
        data=csv,
        file_name="sentiment_analysis.csv",
        mime="text/csv"
    )

# Bar Chart of Sentiment Analysis Results
with st.expander('Sentiment Analysis Results'):
    if upload:
        st.bar_chart(df['analysis'].value_counts())
