from nerd import ner

doc = ner.name( '''
        Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, therefore very
        close to the Manhattan Bridge which is visible from the window.
        ''', language='en_core_web_sm')
text_label = [(X.text, X.label_) for X in doc]
print(text_label)