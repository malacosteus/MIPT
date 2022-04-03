from __future__ import annotations

from collections import defaultdict


class Organisation:

    def __init__(self, professions={"CEO": 1}, vacancies={}) -> None:

        self.prf: defaultdict[str, int] = defaultdict(int, professions)
        self.vac: defaultdict[str, int] = defaultdict(int, vacancies)
        self.sz = sum(self.prf.values())

    def add(self, prf_add: dict[str, int]) -> None:
        '''
        Add employees to corporation
        Input data:
        -----------
            prd_add - number of workers to add to each profession
        Example:
        -------
            corp = Organisation({"driver: 1"})
            corp
            >> Number of drivers is equal to 1
            corp.add({"manager": 100, "programmer": 2"})
            >> Number of drivers is equal to 1
            >> Number of managers is equal to 100
            >> Number of programmers is equal to 2
        '''
        for name, val in prf_add.items():
            self.prf[name] += val
            self.sz += val

    def add_vacancie(self, vac_add: dict[str, int]) -> None:
        '''
        Add vacancie for corporation
        Input data:
        -----------
            vac_add - number of needed workers to add into vacancies list
        '''
        for name, val in vac_add.items():
            self.vac[name] += val

    def intersect(self, other: Organisation) -> dict[str, int]:
        intrsct = self.vac.keys() & other.vac.keys()
        ret_dct: defaultdict[str, int] = defaultdict(int)
        for vac_name in intrsct:
            ret_dct[vac_name] += min(self.vac[vac_name], other.vac[vac_name])
        return ret_dct

    def union(self, other: Organisation) -> dict[str, int]:
        ret_dct: defaultdict[str, int] = defaultdict(int)
        for vac_name in self.vac.keys():
            ret_dct[vac_name] += self.vac[vac_name]
        for vac_name in other.vac.keys():
            ret_dct[vac_name] += other.vac[vac_name]
        return ret_dct

    def difference(self, other: Organisation) -> dict[str, int]:
        diff = self.vac.keys() - other.vac.keys()
        ret_dct: defaultdict[str, int] = defaultdict(int)
        for vac_name in diff:
            ret_dct[vac_name] += self.vac[vac_name]
        return ret_dct

    def __eq__(self, other) -> bool:
        return self.sz == other.sz

    def __lt__(self, other: Organisation) -> bool:
        return self.sz < other.sz

    def __le__(self, other: Organisation) -> bool:
        return self.sz <= other.sz

    def __ne__(self, other) -> bool:
        return self.sz != other.sz

    def __gt__(self, other: Organisation) -> bool:
        return self.sz > other.sz

    def __ge__(self, other: Organisation) -> bool:
        return self.sz >= other.sz


def compare_corp(corp_1: Organisation, corp_2: Organisation) -> None:
    # 1 - compare companies by staff size
    if corp_1 > corp_2:
        print("Corp 1 have gretaer staff size than corp 2")
    elif corp_1 == corp_2:
        print("Corp 1 have same staff size as corp 2")
    else:
        print("Corp 1 have smaller staff size than corp 2")


def prnt_dct(dct: dict) -> None:
    if not dct:
        print("None")
        return
    for name, val in dct.items():
        print(f"{name}: {val}")


if __name__ == "__main__":
    corp_1 = Organisation({"manager": 1, "driver": 100, "accountant": 5})
    corp_2 = Organisation({"manager": 1000, "programmer": 15, "accountant": 3, "cleaner": 9})
    corp_1.add_vacancie({"Uber driver": 1000000000, "cleaner": 8, "accountant": 2})
    corp_2.add_vacancie(
        {
            "programmer ": 1000,
            "cleaner": 19,
            "accountant": 90,
            "cleaner": 6,
            "tester": 25,
        }
    )
    # 1. compare companies by staff size
    compare_corp(corp_1, corp_2)
    print("Let's increase staff size of Corp 2")
    corp_1.add({"driver": 1000000000})
    compare_corp(corp_1, corp_2)
    print("\n")

    # 2. Get companies vacancies list difference/union/intersection
    # Difference
    print("corp_1 - corp_2:")
    dct = corp_1.difference(corp_2)
    prnt_dct(dct)
    print("\n")

    print("corp_2 - corp_1:")
    dct = corp_2.difference(corp_1)
    prnt_dct(dct)
    print("\n")

    print("corp_2 - corp_2:")
    dct = corp_2.difference(corp_2)
    prnt_dct(dct)
    print("\n")

    # Union
    print("Union of corp_1 and corp_2:")
    dct = corp_1.union(corp_2)
    prnt_dct(dct)
    print("\n")

    # Intersection
    print("Intersection of corp_1 and corp_2:")
    dct = corp_1.intersect(corp_2)
    prnt_dct(dct)
