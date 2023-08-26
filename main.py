'''
Project: dataAnalysis_projects1
By: ushellnullpath
Description:
This project is a data analysis project for "MAMAA" stocks that provides insights into the sentiment of the stock's news headlines. 
The sentiment analysis is performed using the VADER sentiment analysis tool from the NLTK library. 
The results are then visualized in a bar chart, showing the average sentiment scores for each stock ticker.
Different libraries that have been used are urllib, BeautifulSoup, nltk, pandas and matplotlib.
Last updated on (D/M/Y): 26/8/2023
'''

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

#defining a dictionary for different ticker colors
ticker_colors = {
    "META": 'skyblue',
    "AAPL": 'orange',
    "MSFT": 'green',
    "AMZN": 'red',
    "GOOG": 'purple'
}

def scrape_and_analyze_news(ticker):
    '''A function that scrapes stocks news headlines and perform sentiment analysis using NLTK's VADER (Valence Aware Dictionary for Sentiment Reasoning) module.'''
    url = f'https://finviz.com/quote.ashx?t={ticker}'
    request = Request(url=url, headers={'user-agent': 'MAMAA_OSNSA_VIZ'})
    response = urlopen(request)
    html = BeautifulSoup(response, features='lxml')
    news_table = html.find(id='news-table')
    
    vader = SentimentIntensityAnalyzer()
    
    parsed_data = []
    for row in news_table.findAll('tr'):
        title = row.a.get_text()
        sentiment_score = vader.polarity_scores(title)['compound']
        parsed_data.append([ticker, title, sentiment_score])
    
    return parsed_data

def main():
    '''Main function to analyze sentiment and create a bar chart.'''
    tickers = ["META", "AAPL", "MSFT", "AMZN", "GOOG"]
    parsed_data = []

    for ticker in tickers:
        data = scrape_and_analyze_news(ticker)
        parsed_data.extend(data)
    
    df = pd.DataFrame(parsed_data, columns=['ticker', 'title', 'compound'])
    avg_sentiment = df.groupby('ticker')['compound'].mean()

    plt.figure(figsize=(10, 6))
    avg_sentiment.plot(kind='bar', color=[ticker_colors[ticker] for ticker in avg_sentiment.index], edgecolor='black')
    plt.title('Average Sentiment Analysis of "MAMAA" Stock News Headlines')
    plt.xlabel('Stock Ticker(s)')
    plt.ylabel('Average Sentiment Score(s)')
    plt.xticks(rotation=45)
    plt.axhline(y=0, color='black', linestyle='--')
    plt.tight_layout()
    plt.show()

#initializing the main() function
if __name__ == "__main__":
    main()