import dataclasses
from dataclasses import field
import pprint


@dataclasses.dataclass
class PronModel:
    pron: str
    total: int = 0
    chain_list: list[tuple[float, str, int]] = field(default_factory=list)

    def add_pron(self, pr: str):
        self.total += 1
        has_flag = False
        for i, chain in enumerate(self.chain_list):
            _, pron, total = chain
            if pron == pr:
                has_flag = True
                total += 1
            self.chain_list[i] = (total / self.total, chain[1], total)
        if not has_flag:
            self.chain_list.append((1 / self.total, pr, 1))


@dataclasses.dataclass
class Model:
    pron_map: dict[str, PronModel] = field(default_factory=dict)

    def add_pron(self, from_pron: str, to_pron: str):
        if from_pron not in self.pron_map.keys():
            self.pron_map[from_pron] = PronModel(pron=from_pron)
        self.pron_map[from_pron].add_pron(to_pron)
