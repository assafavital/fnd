from sklearn.feature_extraction.text import CountVectorizer

sentences = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']

count_vector = CountVectorizer()

# configuring sklearn learn CountVectorizer to set all words to lower case,
# filter stop words and return max feature names
count_vector.lowercase = True
count_vector.stop_words = 'english'
count_vector.max_features = 10

# print(count_vector)

count_vector.fit(sentences)
print(count_vector.get_feature_names())




