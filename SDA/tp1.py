import shutil
import os
from random import randint
from enum import Enum

MENANG = True
KALAH = False


class Penyihir(Enum):
    Tara = 1
    Kenneth = 2

    def invert(self):
        if self == Penyihir.Tara:
            return Penyihir.Kenneth
        return Penyihir.Tara


class Solve:
    def __init__(self):
        pass

    def solve(self, orang_yang_dapat_giliran_pertama: str, cawan_pertama: int, cawan_kedua: int):
        if orang_yang_dapat_giliran_pertama == "Kenneth":
            giliran_pertama = Penyihir.Kenneth
        else:
            giliran_pertama = Penyihir.Tara

        if self.apakah_bisa_menang(giliran_pertama, cawan_pertama, cawan_kedua):
            return giliran_pertama
        return giliran_pertama.invert()

    def apakah_bisa_menang(self, penyihir: Penyihir, cawan_pertama: int, cawan_kedua: int) -> bool:
        if cawan_pertama > 0:  # Mantra A
            # jika musuh tidak bisa menang
            if not self.apakah_bisa_menang(penyihir.invert(), cawan_pertama - 1, cawan_kedua):
                return MENANG

        if cawan_kedua > 0:  # Mantra B
            # jika musuh tidak bisa menang
            if not self.apakah_bisa_menang(penyihir.invert(), cawan_pertama, cawan_kedua - 1):
                return MENANG

        if cawan_kedua > 0 and cawan_pertama > 0:  # Mantra C
            # jika musuh tidak bisa menang
            if not self.apakah_bisa_menang(penyihir.invert(), cawan_pertama - 1, cawan_kedua - 1):
                return MENANG

        if cawan_pertama >= 2:  # Mantra D
            # jika musuh tidak bisa menang
            if not self.apakah_bisa_menang(penyihir.invert(), cawan_pertama - 2, cawan_kedua):
                return MENANG

        if cawan_kedua >= 2:  # Mantra E
            # jika musuh tidak bisa menang
            if not self.apakah_bisa_menang(penyihir.invert(), cawan_pertama, cawan_kedua - 2):
                return MENANG

        return KALAH


def solve(nama, ki, ka):
    solver = Solve()
    penyihir = Penyihir.Tara
    if nama == "Kenneth":
        penyihir = Penyihir.Kenneth
    elif nama != "Tara":
        raise Exception()

    if solver.apakah_bisa_menang(penyihir, ki, ka):
        return penyihir.name
    else:
        return penyihir.invert().name


nama = input()
ki, ka = map(int, input().split())
print(solve(nama, ki, ka))
