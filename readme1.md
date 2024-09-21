# Sentiment Analyzer

A web application for analyzing the sentiment of text using VADER sentiment analysis. This app allows users to input text or upload CSV files containing tweets, perform sentiment analysis, and visualize the results through various charts and graphs.

## Features

- **Text Analysis**: Input text for quick sentiment analysis.
- **Text Cleaning**: Clean input text by removing punctuation and extra spaces.
- **CSV File Upload**: Upload CSV files to analyze multiple tweets at once.
- **Sentiment Analysis**: Analyze sentiment using VADER and classify it as Positive, Negative, or Neutral.
- **Visualizations**:
  - Bar chart of sentiment counts.
  - Pie chart of sentiment distribution.
  - Word cloud of the most common words in the tweets.
  - Histogram of polarity scores.

## Installation

To run this application locally, ensure you have Python installed. Then, you can install the required libraries by running:

```bash
pip install streamlit pandas matplotlib wordcloud vaderSentiment
