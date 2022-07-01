# Sentiment Analysis
# By Bryan Lee (Student Number: 251070487) - CS 1026A
# This program reads 2 files, one containing tweets and the other containing keywords,
# and then evaluates the happiness value of tweets from 4 regions across the US
# The program mainly makes use of functions, exceptions, file reading, and loops


# Importing sentiment_analysis.py to main.py to use the function that calculates the happiness value of the tweets
from sentiment_analysis import compute_tweets


# Beginning of main function
def main():

    # Beginning of try block
    try:
        # User input to get the names of the files
        tweet = input('Name of the tweet file? ')
        keywords = input('Name of the keyword file? ')

        # Function call to get the average happiness values, tweets containing keywords, and tweets from each region
        tweetSentiment = compute_tweets(tweet, keywords)

        # Output to screen
        print()
        print()
        print('Eastern Time Zone Results: Sentiment Average = %.3f, Tweets with keywords = %d, Tweets = %d' % (tweetSentiment[0][0], tweetSentiment[0][1], tweetSentiment[0][2]))
        print('Central Time Zone Results: Sentiment Average = %.3f, Tweets with keywords = %d, Tweets = %d' % (tweetSentiment[1][0], tweetSentiment[1][1], tweetSentiment[1][2]))
        print('Mountain Time Zone Results: Sentiment Average = %.3f, Tweets with keywords = %d, Tweets = %d' % (tweetSentiment[2][0], tweetSentiment[2][1], tweetSentiment[2][2]))
        print('Pacific Time Zone Results: Sentiment Average = %.3f, Tweets with keywords = %d, Tweets = %d' % (tweetSentiment[3][0], tweetSentiment[3][1], tweetSentiment[3][2]))

    # Except block in case if the user inputs the files backwards resulting in the print statements crashing
    except IndexError:
        print([])

# End of main function


# Function call to begin program
main()
