import re
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from concurrent.futures import ThreadPoolExecutor
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to analyze sentiment using VADER
def analyze_text_vader(text):
    sentiment = analyzer.polarity_scores(text)
    return sentiment['compound']

# Function to assign sentiment labels based on VADER's compound score
def score_sentiment_vader(compound):
    if compound >= 0.5:
        return 'Positive'
    elif compound <= -0.5:
        return 'Negative'
    return 'Neutral'

# Function to clean text quickly using regex
def clean_text_fast(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.lower()

# Parallel sentiment analysis function
def analyze_sentiments_parallel(texts, max_workers=16):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(analyze_text_vader, texts))
    return results

# Analyze CSV in chunks (for large files)
@st.cache_data
def analyze_csv(file):
    chunks = pd.read_csv(file, encoding='utf-8', chunksize=5000, usecols=['tweet'], dtype={'tweet': 'str'})
    results = []

    for chunk in chunks:
        # Clean the tweets
        chunk['cleaned_tweet'] = chunk['tweet'].apply(clean_text_fast)
        # Analyze sentiment in parallel
        chunk['polarity'] = analyze_sentiments_parallel(chunk['cleaned_tweet'])
        # Assign sentiment labels
        chunk['analysis'] = chunk['polarity'].apply(score_sentiment_vader)
        results.append(chunk)

    # Concatenate all chunks together
    df = pd.concat(results)
    return df

# Streamlit app interface
st.title('Sentiment Analyzer')

# Text analysis
st.header('Text Analysis')
text = st.text_input('Type or paste the text you want to analyze:')
if text:
    cleaned_text = clean_text_fast(text)
    polarity = analyze_text_vader(cleaned_text)
    st.write('**Polarity:**', polarity)
    st.write('**Sentiment:**', score_sentiment_vader(polarity))

# Text cleaning
st.header('Text Cleaning')
pre = st.text_input('Type or paste the text you want to clean:')
if pre:
    cleaned = clean_text_fast(pre)
    st.write('**Cleaned Text:**', cleaned)

# CSV file uploader for sentiment analysis
st.header('CSV Sentiment Analysis')
upload = st.file_uploader('Upload CSV File', type=['csv'])

if upload:
    with st.spinner('Analyzing tweets...'):
        df = analyze_csv(upload)
    if df is not None:
        st.success('Analysis complete!')
        st.write(df.head(5))

        # Download the processed data
        @st.cache_data
        def convert_df_to_csv(df):
            return df.to_csv(index=False).encode('utf-8')

        csv = convert_df_to_csv(df)
        st.download_button(
            label="Download as a CSV file",
            data=csv,
            file_name="sentiment_analysis.csv",
            mime="text/csv"
        )

        # Add visuals in the expander
        with st.expander('Analysis Results and Visuals'):
            # Bar Chart of Sentiment Analysis Results
            sentiment_counts = df['analysis'].value_counts(dropna=False)
            if not sentiment_counts.empty:
                st.bar_chart(sentiment_counts)
            else:
                st.write("No sentiment data to display.")
            
            # Show percentages for better interpretation
            st.write('Percentage breakdown:')
            st.write((sentiment_counts / sentiment_counts.sum()) * 100)

            # Pie Chart for Sentiment Distribution
            st.header('Pie Chart of Sentiment Distribution')
            fig1, ax1 = plt.subplots()
            ax1.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig1)

            # Word Cloud for Most Common Words
            st.header('Word Cloud of Most Common Words')
            all_words = ' '.join(df['cleaned_tweet'])
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_words)
            fig2, ax2 = plt.subplots(figsize=(8, 4))
            ax2.imshow(wordcloud, interpolation='bilinear')
            ax2.axis('off')  # No axes for the word cloud
            st.pyplot(fig2)

            # Histogram of Polarity Scores
            st.header('Histogram of Polarity Scores')
            fig3, ax3 = plt.subplots()
            ax3.hist(df['polarity'], bins=20, edgecolor='black')
            ax3.set_title('Distribution of Polarity Scores')
            ax3.set_xlabel('Polarity Score')
            ax3.set_ylabel('Frequency')
            st.pyplot(fig3)
