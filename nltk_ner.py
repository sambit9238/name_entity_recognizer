from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import tree2conlltags
sentence = '''
        Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, therefore very
        close to the Manhattan Bridge which is visible from the window.
        '''
print(tree2conlltags(ne_chunk(pos_tag(word_tokenize(sentence)))))