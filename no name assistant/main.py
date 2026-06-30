import spacy


def language_processing(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    actions=[]
    flag=True
    length=len(doc)
    num=1
    for token in doc:
        if token.pos_ =="VERB" and token.dep_ == "ROOT" or token.dep_ == "conj":
            if flag == False:
                actions.append(dict1)
            action= token.text
            dict1={"action": action,"target": None}
            flag= False
        if token.dep_ == "dobj":
            target= token.text
            dict1["target"]=target
        if num == length:
            actions.append(dict1)
        num+=1
    
    return actions
    # print(actions)
            
