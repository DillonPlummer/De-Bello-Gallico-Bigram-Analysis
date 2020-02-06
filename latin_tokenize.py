import nltk

file = './clean/de_bello_gallico_clean_combined.txt'

with open(file) as f:
    text = f.read()

    # tokenize words
    tokens = nltk.word_tokenize(text)
    print('Total No. Tokens:', len(tokens))
    word_fd = nltk.FreqDist(tokens)
    most_common = word_fd.most_common(25)
    print('MOST COMMON WORDS:')
    print(most_common)

    #get bigrams
    bgs = nltk.bigrams(tokens)
    bg_fd = nltk.FreqDist(bgs)
    bg_common = bg_fd.most_common(55)

    # print bigram frequency
    print('MOST COMMON BIGRAMS:')
    for key, val in bg_common:
        print(key, val)
