# Sentiment Analyzer

A web application for analyzing the sentiment of text using VADER. This app allows users to input text or upload CSV files containing tweets, perform sentiment analysis, and visualize the results through various charts and graphs.

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

## Demo

**Try the live demo of this application [here](https://sentimentanalysistweets.streamlit.app/).**

**Sample CSV Files**: Two sample CSV files are provided for users to try out the sentiment analysis functionality. Upload them via the CSV file uploader to see how the app works with real data.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shubhruia/sentiment-analysis.git
   ```

2. **Install the required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

#### 1. Run the App: Launch the app by running the following command in your terminal:
```bash
streamlit run main.py
```
#### 2. Text Analysis:

- Navigate to the Text Analysis section.
- Type or paste the text you want to analyze. The app will display the polarity score and sentiment classification.

#### 3. Text Cleaning:

- In the Text Cleaning section, paste text to see the cleaned version.

#### 4. CSV Sentiment Analysis:

- Upload a CSV file containing a column labeled tweet. The app will analyze each tweet's sentiment and present the results.
- After analysis, download the processed data as a CSV file.

#### 5. Visual Results:

- The app provides visual representations of sentiment analysis results, including charts and word clouds.

## Contribution

Feel free to submit issues or pull requests if you find bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Resources

- **[pandas](https://pandas.pydata.org/)**: For data manipulation and analysis.
- **[streamlit](https://streamlit.io/)**: For building the web app interface.
- **[matplotlib](https://matplotlib.org/)**: For creating visualizations.
- **[wordcloud](https://amueller.github.io/word_cloud/)**: For generating word clouds.
- **[vadersentiment](https://github.com/cjhutto/vaderSentiment)**: For sentiment analysis.
