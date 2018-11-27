from nltk.tokenize import sent_tokenize
mytext = "Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
mytext2 = "Hello Adam how are you I hope everything is going well Today is a good day see you dude"
print(sent_tokenize(mytext))
print(sent_tokenize(mytext2))
