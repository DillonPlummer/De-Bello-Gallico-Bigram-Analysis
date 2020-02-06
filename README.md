# Caesar's De Bello Gallico: Bigram Analysis
A Python program written with NLTK to find and sort bigrams in Caesar's famous De Bello Gallico (The Gallic War).

PROCESS:
1. I wrote and ran regex_cleanup.py to clean up the data,  using regular expressions to remove the section numbers and footnote numbers with their brackets.

2. I then combined all of the cleaned text into one file, de_bello_gallico_clean_combined.txt

3. Next, I tokenized both the English and (cleaned) Latin texts.  When forming frequency distributions, the Latin text presented an added challenge because it’s a highly-inflected language: it has inflectional morphemes attached to the end of nouns to mark their case (declensions). I worked around this by using more regular expressions to approximate taking off the inflectional endings.

OVERALL ORDER FOR RUNNING ON THE COMMAND LINE:
1. regex_cleanup.py files
2. latin_tokenize.py (this prints the most common bigrams)
3. latin.tokenize.py | grep -i caesar*
4. latin.tokenize.py | grep -i propter*
5. latin.tokenize.py | grep Galli*
