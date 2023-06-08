import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def perform_sentiment_analysis(text):
    # Create a SentimentIntensityAnalyzer object
    sid = SentimentIntensityAnalyzer()

    # Perform sentiment analysis
    sentiment_scores = sid.polarity_scores(text)

    # Interpret the sentiment scores
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    # Return the sentiment and scores
    return sentiment, sentiment_scores

# Test the function
input_text = input("Enter a text for sentiment analysis: ")
sentiment, scores = perform_sentiment_analysis(input_text)

print(f'Sentiment: {sentiment}')
print(f'Sentiment Scores: {scores}')
