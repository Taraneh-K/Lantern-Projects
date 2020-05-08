# Analysis Outline:

In this project Sentiment of a Corpus text file is analyzed. The sentiment of each sentence is either negative(label_1) or positive(label_2). Random Forest is fitted to dataset to predict the sentiment of each sentence. Prior to fitting the models, text data was preprocessed which involves transforming raw data into an understandable format for NLP models: Preprocessing of text data involves transforming raw data into an understandable format for NLP models. 
1. Data cleaning and changing all the text content to lower case.
2. Tokenization to  break a stream of text into words, phrases, symbols, or other meaningful elements called tokens. The list of tokens becomes input for further processing.
3. Removing Punctuation and Stopwords
4. Word Lemmatization to reduce the inflectional forms of each word into a common base or root.
5. Word Vectorization using word count and TFIDF to turn a collection of text documents into numerical feature vectors
6. Feature Engineering
7. Adding new features to features
8. Splitting data into Train and Test datasets
9. Encoding labels to transform Categorical data of string type in the data set into numerical values which the model can understand.
10. Fitting Random Forest algorithm and optimizing the hyper parameters
