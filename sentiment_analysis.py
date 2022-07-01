# Sentiment Analysis
# By Bryan Lee (Student Number: 251070487) - CS 1026A
# This file contains the functions that calculate the happiness value of the tweets


# Importing the punctuation library to strip the longitude, latitude, and tweets of beginning and ending punctuation
from string import punctuation


# Function that reads the files the user inputted, gathers necessary values, formats them, determines their region,
# and calculates the sentiment value
# Beginning of compute_tweets function
def compute_tweets(tweets, keywords):

    # Local variables

    # These variables show the number of tweets in a certain region that have keywords in them
    eastSentTweets = 0
    centralSentTweets = 0
    mountainSentTweets = 0
    pacificSentTweets = 0

    # These variables show the number of tweets in a certain region
    eastTweets = 0
    centralTweets = 0
    mountainTweets = 0
    pacificTweets = 0

    # These variables hold the sentiment value of each tweet in a certain region
    eastValue = []
    centralValue = []
    mountainValue = []
    pacificValue = []

    # This try block separates the keywords into lists based on the sentiment value attached to the word
    # Beginning of outer try block
    try:
        # Opening keywords file for reading
        keyFile = open(keywords, "r", encoding="utf‐8")

        # Beginning of inner try block
        try:
            # These variables hold keywords based on their sentiment value
            sent1 = []
            sent2 = []
            sent3 = []
            sent4 = []
            sent5 = []
            sent6 = []
            sent7 = []
            sent8 = []
            sent9 = []
            sent10 = []

            # For loop to determine the sentiment value of each word and to append it to the correct list
            # Beginning of for loop
            for line in keyFile:

                # Separating each line into the word and the sentiment value
                lstKeywords = line.split(',')
                sentWord = lstKeywords[0]
                sentValue = int(lstKeywords[1])

                # If/else statement to determine which list each word belongs in based on its sentiment value
                if sentValue == 1:
                    sent1.append(sentWord)

                elif sentValue == 2:
                    sent2.append(sentWord)

                elif sentValue == 3:
                    sent3.append(sentWord)

                elif sentValue == 4:
                    sent4.append(sentWord)

                elif sentValue == 5:
                    sent5.append(sentWord)

                elif sentValue == 6:
                    sent6.append(sentWord)

                elif sentValue == 7:
                    sent7.append(sentWord)

                elif sentValue == 8:
                    sent8.append(sentWord)

                elif sentValue == 9:
                    sent9.append(sentWord)

                else:
                    sent10.append(sentWord)

            # End of for loop

            # Variable to hold all of the lists of words based on their sentiment value in one list
            sentLists = [sent1, sent2, sent3, sent4, sent5, sent6, sent7, sent8, sent9, sent10]

        # End of inner try block

        # Finally block to close the keywords file
        finally:
            keyFile.close()

    # End of outer try block

    # Except block in case the user inputs an invalid keywords file name
    except IOError:
        return []

    # Except block in case the user inputs the files backwards resulting in sentValue crashing when trying to convert to int
    except ValueError:
        return []

    # This try block reads the tweets, calculates the sentiment value, and separates them into a list based on the region
    # Beginning of outer try block
    try:
        # Opening the tweets file for reading
        tweetsFile = open(tweets, "r", encoding="utf‐8")

        # Beginning of inner try block

        try:
            # While loop to check to see if the line contains any characters
            # Beginning of while loop
            while line != '':

                # For loop to iterate over each line in the tweets file
                # Beginning of outer for loop
                for line in tweetsFile:

                    # Variable to hold the formatted tweet
                    formatTweet = ''

                    # Variables to separate the tweet and get the longitude, latitude, and the tweet
                    splitTweet = line.split()
                    lat = float(splitTweet[0].strip(punctuation))
                    long = float(splitTweet[1].strip(punctuation)) * -1
                    sentence = splitTweet[5:len(line)]

                    # For loop to add formatted words to a new string
                    # Beginning of inner for loop
                    for word in sentence:

                        # Formatting the tweet into lowercase with no beginning or ending punctuation
                        formatTweet = formatTweet + ' ' + word.strip(punctuation).lower()
                        formatTweet = formatTweet.strip()

                    # End of inner for loop

                    # Turning the tweet into a list so each word can be checked against the keywords
                    formatTweet = formatTweet.split()

                    # Nested if/else statements to determine the region the tweet originated from
                    if 24.660845 <= lat <= 49.189787 and -87.518395 <= long <= -67.444574:
                        eastTweets += 1
                        tweetValue = sentCalc(formatTweet, sentLists)

                        if tweetValue > 0:
                            eastValue.append(tweetValue)
                            eastSentTweets += 1

                    elif 24.660845 <= lat <= 49.189787 and -101.998892 <= long <= -87.518395:
                        centralTweets += 1
                        tweetValue = sentCalc(formatTweet, sentLists)

                        if tweetValue > 0:
                            centralValue.append(tweetValue)
                            centralSentTweets += 1

                    elif 24.660845 <= lat <= 49.189787 and -115.236428 <= long <= -101.998892:
                        mountainTweets += 1
                        tweetValue = sentCalc(formatTweet, sentLists)

                        if tweetValue > 0:
                            mountainValue.append(tweetValue)
                            mountainSentTweets += 1

                    elif 24.660845 <= lat <= 49.189787 and -125.242264 <= long <= -115.236428:
                        pacificTweets += 1
                        tweetValue = sentCalc(formatTweet, sentLists)

                        if tweetValue > 0:
                            pacificValue.append(tweetValue)
                            pacificSentTweets += 1

                # End of outer for loop

                # Variables that show the average sentiment, number of tweets with keywords, and number of tweets in each region
                easternTZ = regionCalcs(eastValue, eastSentTweets, eastTweets)
                centralTZ = regionCalcs(centralValue, centralSentTweets, centralTweets)
                mountainTZ = regionCalcs(mountainValue, mountainSentTweets, mountainTweets)
                pacificTZ = regionCalcs(pacificValue, pacificSentTweets, pacificTweets)

                return [easternTZ, centralTZ, mountainTZ, pacificTZ]

            # End of while loop

        # End of inner try block

        # Finally block to close the tweets file
        finally:
            tweetsFile.close()

    # End of outer try block

    # Except block in case the user inputs an invalid file name
    except IOError:
        return []

# End of compute_tweets function


# Function to calculate the sentiment value of each tweet
# Beginning of sentCalc function
def sentCalc(tweet, sentWords):

    # Local variables
    tweetValue = 0
    keywords = 0

    # For loop to check to see if each word in a tweet is one of the keywords
    # Beginning of for loop
    for word in tweet:

        # If/Else block to check each word against the keywords list and adds the value of the keyword to the tweet value
        if word in sentWords[0]:
            tweetValue = tweetValue + 1
            keywords += 1

        elif word in sentWords[1]:
            tweetValue = tweetValue + 2
            keywords += 1

        elif word in sentWords[2]:
            tweetValue = tweetValue + 3
            keywords += 1

        elif word in sentWords[3]:
            tweetValue = tweetValue + 4
            keywords += 1

        elif word in sentWords[4]:
            tweetValue = tweetValue + 5
            keywords += 1

        elif word in sentWords[5]:
            tweetValue = tweetValue + 6
            keywords += 1

        elif word in sentWords[6]:
            tweetValue = tweetValue + 7
            keywords += 1

        elif word in sentWords[7]:
            tweetValue = tweetValue + 8
            keywords += 1

        elif word in sentWords[8]:
            tweetValue = tweetValue + 9
            keywords += 1

        elif word in sentWords[9]:
            tweetValue = tweetValue + 10
            keywords += 1

    # If/Else statement to see if there were any keywords in the tweet and if there are, then determines the happiness value of the tweet
    if keywords > 0:
        tweetValue = tweetValue / keywords
        return tweetValue

    else:
        return 0

# End of sentCalc function


# Function to calculate the average sentiment of a region and create the tuple that contains the necessary info for the program
# Beginning of regionCalcs function
def regionCalcs(value, sentTweets, tweets):

    # Summing the happiness values of the region value list and averaging it
    if sentTweets > 0:
        value = sum(value)
        avg = value / sentTweets

    else:
        avg = 0

    # Creating the tuple that holds the necessary info for the program
    regionInfo = (avg, sentTweets, tweets)

    return regionInfo

# End of regionCalcs function
