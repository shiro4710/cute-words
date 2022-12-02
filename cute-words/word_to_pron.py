import pandas as pd
from pykakasi import kakasi

word_list = pd.read_csv("data/original.csv")

kks = kakasi()

pron_list: list[str] = []

for row in word_list.values:
    pron = ""
    for result in kks.convert(row[0]):
        pron += result["hira"]
    pron_list.append(pron)

word_list["pron"] = pron_list

word_list.to_csv("data/word_pron.csv")
