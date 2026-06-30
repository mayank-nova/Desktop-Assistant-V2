import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(input())

for token in doc:
    print("Word:", token.text)
    print("Type of word:", token.pos_)
    print("Grammar role:", token.dep_)
    print("-" * 20)