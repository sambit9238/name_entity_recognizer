import spacy
nlp = spacy.load('en_core_web_sm') 
sentence = '''
        Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, therefore very
        close to the Manhattan Bridge which is visible from the window.
        '''
  
doc = nlp(sentence) 
  
for ent in doc.ents: 
    print(ent.text, ent.start_char, ent.end_char, ent.label_) 