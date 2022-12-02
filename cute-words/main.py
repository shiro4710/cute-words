import pron_markov as pm
import pprint
import pandas as pd

word_list = []
for v in pd.read_csv("data/word_pron.csv").values:
    word_list.append(v[2])


model = pm.train(word_list)

pprint.pprint(model)
