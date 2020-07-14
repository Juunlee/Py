from lingpy import *
from lingpy.tests.util import test_data

wl = Wordlist(test_data('KSL.qlc'))

def to_ccm(tokens):
    cv = tokens2class(tokens, 'cv')
    cl = tokens2class(tokens, 'dolgo')
    dolgo = ''
    if cv[0] == 'V': 
        dolgo += 'H'
    else:
        dolgo += cl[0]
    for c, v in zip(cv[1:], cl[1:]):
        if c == 'C':
            dolgo += v
    if len(dolgo) == 1:
        dolgo += 'H'
    return dolgo[:2]

wl.add_entries(
    'cog', 
    'tokens,concept', 
    lambda x, y : x[y[1]]+'-'+to_ccm(x[y[0]]))

wl.renumber('cog', override=True)
