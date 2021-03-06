# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2014
#
# License: MIT

import unittest
import os
import numpy as np
import csv

import sys
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

from core.textutils.feature_extraction import FeatureExtractor

DOCUMENTS = ['O rato roeu a roupa do rei de roma',
             'O rato e um mau carater',
             'A roupa do rei e legal', 
             'O rei e um rato mau',
             'A roupa e bacana', 
             'Eu gosto de batata',
             'Salve o rei da inglaterra: o rato!!',
             'Ratos trazem doencas',
             'A peste negra foi proveniente da pulga do rato, rato pulguento!!',
             'Batata e bom',
             'Eu gosto de estudar e batata',
             'Batata e um turbeculo',
             'Sera que a batata e uma raiz ?',
             'Tem gente que nao gosta de batata',
             'Batata frita e muito bom']

class TestFeatureExtraction(unittest.TestCase):

    def test_count_vectorizer(self):

        fe = FeatureExtractor(DOCUMENTS, max_features=3)
        X, vocabulary, feature_names = fe.count_vectorizer()
        lines, columns = X.shape
        self.assertGreaterEqual(3, columns)

    def test_hashing_vectorizer(self):

        fe = FeatureExtractor(DOCUMENTS, max_features=3)
        X = fe.hashing_vectorizer()
        lines, columns = X.shape
        self.assertGreaterEqual(3, columns)

    def test_tfidf_vectorizer(self):

        fe = FeatureExtractor(DOCUMENTS)

        # the most common word rato should not
        # be present in more than 50% of the documents
        X, vocabulary, feature_names = fe.tfidf_vectorizer()

        for word in feature_names:
            print(word)

        print()
        print()

        for word in vocabulary.keys():
            print(word)
    
        self.assertNotIn("rato", vocabulary.keys())
    

    def test_get_top_words(self):

        file_name = r"C:\Users\Allan\Documents\Visual Studio 2013\Projects\twitter_analysis\twitter_analysis\tweets\tweets_dilma.csv"
        tweets = []
        with open(file_name, newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f, delimiter=';', quotechar='|')
            for tweet in csv_reader:
                tweets.append(tweet[2])

        fe = FeatureExtractor(tweets, ngram_range=(2,2), max_features=20)
        X, vocabulary, feature_names = fe.count_vectorizer()
        top_words = fe.get_top_words(vocabulary, X, max_words=20)
        print(top_words)
        self.assertGreaterEqual(20, len(top_words))

if __name__ == '__main__':
    unittest.main()