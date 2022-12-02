from pron_markov.model import *
import random

_start_flag = "__start"
_end_flag = "__end"


def train(train_data: list[str]) -> Model:
    model = Model()
    for word in train_data:
        sep_word = list(word)
        sep_word.append(_end_flag)

        for i, c in enumerate(sep_word):
            if i == 0:
                model.add_pron(_start_flag, c)
                continue
            model.add_pron(word[i - 1], c)

            if i != 1:
                model.add_pron(word[i - 2 : i], c)
    return model
