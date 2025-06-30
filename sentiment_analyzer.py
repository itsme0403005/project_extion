import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
obj = SentimentIntensityAnalyzer()
def analyze_sentiment(text):
    score = obj.polarity_scores(text)
    compound = score['compound']
    
    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment, score
# Input from user
text = input("Enter a sentence for sentiment analysis: ")

# Analyze sentiment
sentiment, scores = analyze_sentiment(text)

# Output result
print(f"Sentiment: {sentiment}")
print(f"Scores: {scores}")