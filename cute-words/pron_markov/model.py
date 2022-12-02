from __future__ import annotations
import dataclasses
from dataclasses import field


@dataclasses.dataclass
class PronModel:
    pron: str
    total: int = 0
    chain_list: dict[str, int] = field(default_factory=dict)

    def add_pron(self, pr: str):
        self.total += 1

        if pr not in self.chain_list.keys():
            self.chain_list[pr] = 1
        else:
            self.chain_list[pr] += 1

    def add_model(self, model: PronModel):
        self.total += model.total

        for pr in model.chain_list.keys():
            if pr not in self.chain_list.keys():
                self.chain_list[pr] = model.chain_list[pr]
            else:
                self.chain_list[pr] += model.chain_list[pr]


@dataclasses.dataclass
class Model:
    pron_map: dict[str, PronModel] = field(default_factory=dict)

    def add_pron(self, from_pron: str, to_pron: str):
        if from_pron not in self.pron_map.keys():
            self.pron_map[from_pron] = PronModel(pron=from_pron)

        self.pron_map[from_pron].add_pron(to_pron)

    def add_model(self, model: Model):
        for pron in model.pron_map.keys():
            if pron not in self.pron_map.keys():
                self.pron_map[pron] = PronModel(pron=pron)

            self.pron_map[pron].add_model(model.pron_map[pron])
