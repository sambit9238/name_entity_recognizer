from polyglot.text import Text
blob = '''
        Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, therefore very
        close to the Manhattan Bridge which is visible from the window.
        '''
text = Text(blob)

print(text.entities)