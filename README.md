# Sentiment Analyzer

A powerful web application for analyzing the sentiment of text using VADER (Valence Aware Dictionary and sEntiment Reasoner). This Streamlit-based app enables users to input text or upload CSV files containing tweets, perform sentiment analysis, and visualize the results through various interactive charts and graphs.

## Features

- **Text Analysis**: 
  - Input individual text snippets for quick sentiment analysis.
  - View polarity scores and sentiment classification (Positive, Negative, or Neutral).

- **Text Cleaning**: 
  - Clean input text by removing punctuation and extra spaces.
  - Compare original and cleaned text side-by-side.

- **CSV File Upload**: 
  - Upload CSV files containing multiple tweets for bulk analysis.
  - Analyze sentiment for each tweet in the dataset.

- **Sentiment Analysis**: 
  - Utilize VADER for accurate sentiment analysis.
  - Classify sentiment as Positive, Negative, or Neutral based on polarity scores.

- **Visualizations**:
  - Bar chart: Display counts of different sentiment categories.
  - Pie chart: Illustrate the distribution of sentiments.
  - Word cloud: Showcase the most common words in the analyzed tweets.
  - Histogram: Visualize the distribution of polarity scores.

- **Data Export**: 
  - Download processed data with sentiment analysis results as a CSV file.

## Demo

**Try the live demo of this application [here](https://sentimentanalysistweets.streamlit.app/).**

## Sample Data

To help you get started, we've provided two sample CSV files:
1. `sample_tweets_1.csv`
2. `sample_tweets_2.csv`

Upload these files via the CSV file uploader in the app to see how it handles real-world data.

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

1. **Launch the App**: 
   Run the following command in your terminal:
   ```bash
   streamlit run main.py
   ```

2. **Text Analysis**:
   - Navigate to the "Text Analysis" section.
   - Enter or paste the text you want to analyze.
   - The app will display the polarity score and sentiment classification.

3. **Text Cleaning**:
   - Go to the "Text Cleaning" section.
   - Paste your text to see the cleaned version with punctuation and extra spaces removed.

4. **CSV Sentiment Analysis**:
   - Upload a CSV file containing a column labeled "tweet".
   - The app will analyze the sentiment of each tweet and present the results.
   - After analysis, you can download the processed data as a CSV file.

5. **Explore Visual Results**:
   - Interact with the generated charts and word clouds to gain insights into the sentiment distribution and common themes in your data.

## Dependencies

- **[pandas](https://pandas.pydata.org/)**: Data manipulation and analysis
- **[streamlit](https://streamlit.io/)**: Web app interface
- **[matplotlib](https://matplotlib.org/)**: Creating visualizations
- **[wordcloud](https://amueller.github.io/word_cloud/)**: Generating word clouds
- **[vaderSentiment](https://github.com/cjhutto/vaderSentiment)**: Sentiment analysis

## Contribution

Feel free to submit issues or pull requests if you find bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- VADER sentiment analysis tool creators and contributors
- Streamlit team for their excellent framework
