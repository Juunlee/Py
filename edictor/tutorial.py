# import relevant modules
from segments.tokenizer import Tokenizer

# load the tokenizer object
tk = Tokenizer('data/P_simple-profile.tsv')

# convert a string to test it
print(tk('čathashadhža'))
print(tk('čathashadhža', column='IPA'))


from lingpy import *
from segments.tokenizer import Tokenizer
wl = Wordlist('data/P_input-file.tsv')
op = Tokenizer('data/P_modified-profile.tsv')
wl.add_entries('tokens', 'ipa', op, column='IPA')
wl.output('tsv', filename='data/P_output-file2', ignore='all', prettify=False)
for idx, doculect, form, tokens in wl.iter_rows('doculect', 'ipa', 'tokens'):
    if form != tokens.replace(' ', ''):
        print('{0:10} {1:10} {2:15}'.format(doculect, form, tokens))

wl = Wordlist('data/P_input-file.tsv')
op = Tokenizer('data/P_modified-context-profile.tsv')
wl.add_entries('tokens', 'ipa', lambda x: op('^'+x+'$', column='IPA'))
wl.output('tsv', filename='data/P_output-file', ignore='all', prettify=False)
for idx, doculect, form, tokens in wl.iter_rows('doculect', 'ipa', 'tokens'):
    if form != tokens.replace(' ', ''):
        print('{0:10} {1:10} {2:15}'.format(doculect, form, tokens))

lex = LexStat('data/P_output-file.tsv')
lex.cluster(method='sca', threshold=0.45, ref='cogid')
lex.output(
    'tsv', 
    filename='data/P_cognate-file', 
    subset=True, 
    prettify=False, 
    ignore='all'
)

alm = Alignments(lex, ref='cogid')
alm.align()
alm.output(
    'tsv', 
    filename='data/P_alignment-file', 
    subset=True, 
    cols=['doculect', 'concept', 'ipa', 'tokens', 'cogid', 'alignment'], 
    prettify=False, 
    ignore='all'
)
