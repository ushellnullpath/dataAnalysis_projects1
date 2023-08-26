This is one of my many future data analysis projects. This particular project is focused on "MAMAA" stocks, aiming to provide valuable insights into the sentiment of news headlines related to these stocks. The sentiment analysis is carried out using the VADER sentiment analysis tool from the NLTK library. The results are then visualized in a bar chart, which shows the average sentiment scores for each stock ticker.

- LAST UPDATED (D/M/Y): 26/8/2023

Libraries Used:

    urllib
    BeautifulSoup
    nltk (VADER)
    pandas
    matplotlib

Usage:
The program collects news headlines for specific stock tickers ("META," "AAPL," "MSFT," "AMZN," "GOOG"), analyzes their sentiment, and generates a bar chart displaying the average sentiment scores.

How It Works:

    The program scrapes news headlines from the web for each stock ticker.
    Sentiment analysis is performed on the headlines using NLTK's VADER module.
    The average sentiment scores for each stock ticker are calculated.
    Results are visualized in a bar chart, with each ticker represented by a unique color.

CREDITS: Jim Cramer for renaming "FAANG" to "MAMAA".
