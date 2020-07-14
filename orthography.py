from lexibank_deepadungpalaung import Dataset
from lingpy import *
wl = Wordlist.from_cldf(Dataset().cldf_dir.joinpath('cldf-metadata.json'))
for idx, tokens in wl.iter_rows('tokens'):
    for segment in tokens.n:
        if not segment:
            print(idx, tokens)
