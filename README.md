# Sentiment Analyzer

This is a simple sentiment analysis tool built with Python using Streamlit and TextBlob. The application allows users to analyze the sentiment of text data either by directly inputting text or by uploading a CSV file containing text data (e.g., tweets). The sentiment analysis is based on polarity scores generated by TextBlob.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sentiment-analysis.git
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Running the Application

Execute the following command to run the Streamlit web app:
```bash
streamlit run main.py
```

### 2. Functionality

- **Text Input for Analysis**: Input or paste the text you want to analyze directly into the text box. The sentiment (polarity and subjectivity) of the text will be displayed.

- **Text Cleaning**: Clean the text by removing unwanted elements such as extra spaces, stopwords, punctuation, and numbers.

- **CSV File Upload**: Upload a CSV file containing text data (e.g., tweets). The application will perform sentiment analysis on the text data and display the results in a table. You can also download the analyzed data as a CSV file.

- **Sentiment Analysis Results**: View the distribution of sentiment analysis results (Positive, Negative, Neutral) in a bar chart.

## Dependencies

- [TextBlob](https://textblob.readthedocs.io/en/dev/): Used for natural language processing tasks, including sentiment analysis.
- [pandas](https://pandas.pydata.org/): Library for data manipulation and analysis.
- [streamlit](https://streamlit.io/): Open-source framework for building data-driven web apps.
- [cleantext](https://pypi.org/project/cleantext/): Library for cleaning and preprocessing text data.

### Demo link

https://sentimentanalysistweets.streamlit.app/

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
