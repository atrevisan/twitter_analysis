# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

import re

def declutter_tweet_text(tweet_text):
    """Remove clutter from text prior to saving it.
    
     Parameters
     ----------
     tweet_text : string
        the text extracted from a given tweet.

     Returns
     -------
     tweet_text : string
        the pre-processed tweet text.
    """

    #Convert www.* or https?://* to URL
    tweet_text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL', tweet_text)

    #Convert @username to AT_USER
    tweet_text = re.sub('@[^\s]+','AT_USER', tweet_text)    

    #Remove additional white spaces
    tweet_text = re.sub('[\s]+', ' ', tweet_text)

    #Trim
    tweet_text = tweet_text.strip('\'"')

    # Removing other messy characters
    tweet_text = tweet_text.replace('\n', '')
    tweet_text = tweet_text.replace('\'', '')
    tweet_text = tweet_text.replace('\"', '')
    tweet_text = tweet_text.replace(';', '')
    tweet_text = tweet_text.replace('|', '')
    #tweet_text = tweet_text.replace(':', '')
    tweet_text = tweet_text.replace('.', '')
    tweet_text = tweet_text.replace('?', '')
    tweet_text = tweet_text.replace('!', '')
    tweet_text = tweet_text.replace('\\', '')
    tweet_text = tweet_text.replace(',', '')
    tweet_text = tweet_text.replace('/', '')

    return tweet_text

def pre_process_tweet_text(tweet_text):
    """Removes uninformative words and characters from a tweet prior to extract features for machine learning.
    
     Parameters
     ----------
     tweet_text : string
        the text extracted from a given tweet.

     Returns
     -------
     tweet_text : string
        the pre-processed tweet text.
    """

    #Convert to lower case
    tweet_text = tweet_text.lower()

    #Replace #word with word
    tweet_text = re.sub(r'#([^\s]+)', r'\1', tweet_text)
    
    #Look for 2 or more repetitions of character
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL) 
    tweet_text = pattern.sub(r"\1\1", tweet_text)
    
    return tweet_text
#end

def get_stopwords_list(stopwords_filename):
    """Read stopwords from txt file to a list
    
    Parameters
    -------
    stopwords_filename : string
        path to a txt file containing stopwords

    Returns
    -------
    stopwords : list
        list containing stopwords
    """
    
    stopwords = []
    stopwords.append('at_user')
    stopwords.append('url')
    stopwords.append('rt')
    stopwords.append('gt')

    with open(stopwords_filename, 'r') as f:
        
        line = f.readline()
        while line:
            word = line.strip()
            stopwords.append(word)
            line = f.readline()
        return stopwords