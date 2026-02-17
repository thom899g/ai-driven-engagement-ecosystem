from typing import Dict, Any
import logging
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    """Analyzes sentiment from user interactions."""
    
    def __init__(self, config: Dict[str, Any]) -> None:
        """Initialize the sentiment analyzer with configuration settings."""
        self.config = config
        self.analyzer = SentimentIntensityAnalyzer()
        logging.info("Sentiment Analyzer initialized.")
        
    def get_sentiment(self, text: str) -> float:
        """Return sentiment score for a given text."""
        try:
            return self.analyzer.polarity_scores(text)['compound']
        except Exception as e:
            logging.error(f"Error analyzing sentiment: {str(e)}")
            raise