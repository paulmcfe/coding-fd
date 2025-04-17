import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

while True:
    text = input("\nType some text for sentiment analysis (q to quit): ")

    if text == "q":
        break

    scores = analyzer.polarity_scores(text)
    print("\nHere's the text you entered:")
    print(text)
    print("\nHere are the sentiment scores:")
    print(scores)
