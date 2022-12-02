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


def run(model: Model) -> str:
    ret = ""

    i_pr = _start_flag
    ii_pr = ""

    while True:
        next_pr = []
        # 一文字の探索
        pr_model = model.pron_map[i_pr]
        r = random.randrange(pr_model.total)
        sum = 0
        for k, v in pr_model.chain_list.items():
            sum += v
            if r < sum:
                next_pr.append(k)
                break
        # 二文字の探索
        if ii_pr != _start_flag:
            pr_model = model.pron_map[ii_pr + i_pr]
            r = random.randrange(pr_model.total)
            sum = 0
            for k, v in pr_model.chain_list.items():
                sum += v
                if r < sum:
                    next_pr.append(k)
                    break

        # 2:1ぐらいで一文字:二文字の遷移が選択される
        r = random.randrange(len(next_pr) + 1)
        ii_pr = i_pr
        if r < 2:
            i_pr = next_pr[0]
        else:
            i_pr = next_pr[1]

        if i_pr == _end_flag:
            break

        ret += i_pr

    return ret
