import yake

# Input Text
text = "Kalam was elected as the 11th president of India in 2002 with the support of both the ruling Bharatiya Janata Party and 
the then-opposition Indian National Congress. Widely referred to as the "People's President", he returned to his civilian life of education, 
writing and public service after a single term. He was a recipient of several prestigious awards, including the Bharat Ratna, 
India's highest civilian honor."

# Specifying Parameters
language = "en"
max_ngram_size = 3
deduplication_thresold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 20

custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(text)

for kw in keywords:
    print(kw)
