import pron_markov as pm
import pprint
import pandas as pd

word_list = []
for v in pd.read_csv("data/word_pron.csv").values:
    word_list.append(v[2])


model = pm.train(word_list)

print("input:", len(word_list))
print("model:", model.total)
# pprint.pprint(model)

words = []
while True:
    gen = pm.run(model)
    if len(gen) < 2:
        continue
    words.append(gen)

    if 30 <= len(words):
        break
pprint.pprint(words)
