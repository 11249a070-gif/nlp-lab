from nltk.stem import WordNetLemmatizer
lemmetizer = WordNetLemmatizer()
print(lemmetizer.lemmatize("cast"))
print(lemmetizer.lemmatize("cacti"))
print(lemmetizer.lemmatize("greese"))
print(lemmetizer.lemmatize("rocks"))
print(lemmetizer.lemmatize("python"))
print(lemmetizer.lemmatize("better",pos = "a"))
print(lemmetizer.lemmatize("happy",pos = "a"))
