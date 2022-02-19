def get_wrod_freqs(): # get most common words in sentance 
    import spacy
    from collections import Counter

    text = """
        Hello guys i,am ibrahim Moammed ibarhim , guys are you know who i,am
        please if you know my guys tell me now please !! 
        for again did you guys understand what i,am saying ?
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]

    word_frq = Counter(words)
    common_words = word_frq.most_common(5)

    print(common_words)


get_wrod_freqs()


def computing_similarity(): # get precentage of sentance similarity 
    import spacy

    nlp = spacy.load("en_core_web_sm")
    target = nlp("Cats are beautiful animals ")

    doc1 = nlp("Dogs are bad")
    doc2 = nlp("Some gorgeous creature are felines ")
    doc3 = nlp("Dolphines are swimming animals")

    print(target.similarity(doc1))
    print(target.similarity(doc2))
    print(target.similarity(doc3))


def name_entity_recongnition():  # discover ner stand for this <==
    import spacy

    nlp = spacy.load("en_core_web_sm")
    doc = nlp("Next week I,ll be in madrid")

    for token in doc.ents :
        print(token.text , token.label_)

def lemmatization(): # get the root of the orginal word 
    import spacy 
    nlp = spacy.load("en_core_web_sm")

    doc = nlp("I have Cars and insurance and toward looking and men and women")

    for token in doc :
        print(token.text  , token.lemma_ ,token.lemma)




def detecting_name(): # find or discover the name in each word in sentances 
    import spacy

    nlp = spacy.load("en_core_web_sm")
    doc = nlp("MY NAME IS IBRAHIM I HAVE CAR AND ABLITY TOWARD THE SUN")

    for chunk in doc.noun_chunks:
        print(chunk)


from lib2to3.pgen2 import token

def pos_pair(): # put the pos or part of speech tagging in tuples format
    import spacy

    nlp = spacy.load("en_core_web_sm")

    doc = nlp("All is well that ends well")

    [(token.text) for token in doc]



from pydoc import doc
def part_ofspeech(): # show the part of speech in sentance 
    import spacy

    nlp = spacy.load("en_core_web_sm")
    doc = nlp("Apple is looking at buying U.K startup for $1 billion")

    for token in doc :
        print(token.text , token.lemma_ , token.pos_ , token.is_stop)

def remove_stopwords(): # eleminate the word un meaniful in sentance

        from spacy.lang.en import English

        nlp = English()

        text = """
                when get start learning data science , you should have the ablitiy to stay 
                focues and they are no time to setbacks any more !
        """

        doc = nlp(text)

        filtered_list = []

        for remove in doc:
            if remove.is_stop == False:
                filtered_list.append(remove)

        print(filtered_list)

def tokenize_words(): # sparate the word in sentance in differnt number of word 

    from spacy.lang.en import English

    nlp = English()

    text = """

            when learning data science , you shoudn,t get discourged !
            challenges and setbacks are,t failure they are just part of your juorney
            you h,ve got this !   

    """

    doc = nlp(text)
    token_text = []
    for token in doc:
        token_text.append(token.text)

        print((token_text))

#about 135 line code in one hour and half
#do yo think this is amazing thanks  